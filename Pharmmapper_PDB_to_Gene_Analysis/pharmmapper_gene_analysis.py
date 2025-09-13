import csv
import requests

# --- 1. CSV dosyası ---
csv_file = "pharmmapper_result.csv"

pdb_ids = []

with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # Başlık satırını atla

    for row in reader:
        if len(row) < 3:
            continue
        try:
            fit_score = float(row[2].strip())
            if fit_score >= 2.5:
                pharma_model = row[0].strip()
                pdb_id = pharma_model.split('_')[0]  # İlk 4 harf = PDB ID
                pdb_ids.append(pdb_id)
        except Exception as e:
            # Satır hatalıysa atla
            continue

# --- 2. PDB ID'leri kaydet ---
with open("pdb_ids.txt", "w") as f:
    for pid in pdb_ids:
        f.write(pid + "\n")

print(f"{len(pdb_ids)} tane PDB ID kaydedildi -> pdb_ids.txt")

# --- 3. PDBe API ile Organism ve Gene Name al ---
analysis_lines = []

for pid in pdb_ids:
    url = f"https://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/{pid.lower()}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        if pid.lower() in data:
            for mol in data[pid.lower()]:
                # Organism
                organism = mol.get("source_organism_common_name", ["N/A"])
                if isinstance(organism, list):
                    organism = organism[0] if organism else "N/A"

                # Gene Name
                gene_names = mol.get("gene_name", ["N/A"])
                if isinstance(gene_names, str):
                    gene_names = [gene_names]
                elif not isinstance(gene_names, list):
                    gene_names = ["N/A"]

                line = f"{pid}\tOrganism: {organism}\tGene: {', '.join(gene_names)}"
                analysis_lines.append(line)
                break  # sadece ilk molecule
    else:
        analysis_lines.append(f"{pid}\tVeri alınamadı")

# --- 4. Analiz sonuçlarını kaydet ---
with open("analysis.txt", "w", encoding="utf-8") as f:
    for line in analysis_lines:
        f.write(line + "\n")

print("Analiz tamamlandı -> analysis.txt")
