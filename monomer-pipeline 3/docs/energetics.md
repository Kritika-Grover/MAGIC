# EvoEF Protein Stability Analysis Script
The EvoEF Protein Stability Analysis Script is a Python script designed to automate the analysis of protein stability using the EvoEF computational tool. This script performs two primary tasks: running EvoEF stability analysis on two protein structure files (wildtype and variant) and filtering specific output data from the EvoEF results.

## Requirements
1. Python 3.x
2. EvoEF executable installed and accessible via the command line.

## Usage
The script can be run from the command line using the following format:

```bash
python energetics.py -w <wildtype_pdb> -v <variant_pdb> -f <evoef_executable>
```

- `<wildtype_pdb>`: Path to the wildtype protein structure PDB file.
- `<variant_pdb>`: Path to the variant protein structure PDB file.
- `<evoef_executable>`: Path to the EvoEF executable.

## Output
The script generates the following output files:

1. `energetics_WT.txt`: Output file containing the EvoEF stability analysis results for the wildtype protein.
2. `energetics_V.txt`: Output file containing the EvoEF stability analysis results for the variant protein.
3. `filtered_energetics_WT.txt`: Filtered output file containing selected data from the EvoEF results for the wildtype protein.
4. `filtered_energetics_V.txt`: Filtered output file containing selected data from the EvoEF results for the variant protein.

## Limitations
- This script assumes that EvoEF is properly installed and accessible via the provided 'evoef_executable`.
- It is designed to work with EvoEF output formats as of the script's creation date and may require adjustments for future EvoEF versions.
- Errors during execution are reported to the console, but the script does not attempt to recover or retry failed processes.

## Functions
### `run_evoef(pdb_path, evoef_path, output_file)`
- Description: Runs the EvoEF stability analysis on a protein structure and saves the output to a file.
- Arguments:
  - `pdb_path`: Path to the input PDB file (wildtype or variant).
  - `evoef_path`: Path to the EvoEF executable.
  - `output_file`: Path to the output file for EvoEF results.
- Output: EvoEF results saved to the specified output file.

### `filter_output(input_file, output_file)`
- Description: Filters specific lines from a EvoEF output file.
- Arguments:
  - `input_file`: Path to the input EvoEF output file.
  - `output_file`: Path to the filtered output file.
- Output: Filtered output saved to the specified output file.

### `main()`
- Description: The main function that parses command-line arguments, runs EvoEF analysis for both wildtype and variant PDB files, and filters the output.
- Input: Command-line arguments for PDB files and EvoEF executable.

## Example Usage
```bash
python energetics.py -w wildtype.pdb -v variant.pdb -f /path/to/EvoEF_executable
```

## Notes
- Ensure that EvoEF is properly configured and available in the system's PATH for the script to run successfully.
- This script can be extended or modified to accommodate changes in EvoEF or additional processing steps.

## TODO
- Currently, there are no pending tasks.