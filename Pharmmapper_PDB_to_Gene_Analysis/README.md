# README.md for PharmMapper Gene Analysis

# PharmMapper Gene Analysis

`pharmmapper_gene_analysis.py` is a Python script that automates the extraction and analysis of target proteins from PharmMapper results. It filters high fit-score models, extracts PDB IDs, and retrieves organism and gene information using the PDBe API.

## Features

- Reads PharmMapper CSV output.
- Filters models with fit score >= 2.5.
- Extracts PDB IDs from selected models.
- Fetches organism and gene names via PDBe API.
- Saves PDB IDs to `pdb_ids.txt` and analysis results to `analysis.txt`.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/pharmmapper_gene_analysis.git
   ```
2. Install required packages (Python 3.x):
   ```bash
   pip install requests
   ```

## Usage

1. Place your PharmMapper CSV file in the project directory and name it `pharmmapper_result.csv`.
2. Run the script:
   ```bash
   python pharmmapper_gene_analysis.py
   ```
3. Outputs:
   - `pdb_ids.txt` -> List of filtered PDB IDs.
   - `analysis.txt` -> Organism and gene information for each PDB ID.

## Example Output

```
1abc    Organism: Human    Gene: TP53
2xyz    Organism: Mouse    Gene: Mdm2
...
```

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
