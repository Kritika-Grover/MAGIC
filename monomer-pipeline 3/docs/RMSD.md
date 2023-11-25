# RMSD Calculation Script
The RMSD Calculation Script is a Python script designed to automate the calculation of the Root Mean Square Deviation (RMSD) between two protein structures. The script uses PyMOL's built-in `cmd` library to perform the RMSD calculation and saves the result to an output file.

## Requirements
1. Python 3.x
2. PyMOL installed and its `cmd` library accessible in the Python environment.

## Usage
The script can be run from the command line using the following format:

```bash
python RMSD.py <pdb_file1> <pdb_file2> <output_file>
```

- `<pdb_file1>`: Path to the first protein structure PDB file.
- `<pdb_file2>`: Path to the second protein structure PDB file.
- `<output_file>`: Name of the output file where the RMSD value will be saved.

## Output
The script generates a single output file specified by the `<output_file>` argument. This file contains the calculated RMSD value between the two input PDB files.

## Limitations
- The script assumes that PyMOL and its `cmd` library are properly installed.
- Errors during execution are reported to the console, but the script does not attempt to recover or retry failed processes.

## Functions
### `calculate_rmsd(pdb_file1, pdb_file2)`
- Description: Calculates the RMSD between two protein structures and returns the RMSD value.
- Arguments:
  - `pdb_file1`: Path to the first input PDB file.
  - `pdb_file2`: Path to the second input PDB file.
- Output: Returns the calculated RMSD value.

### `main()`
- Description: The main function that parses command-line arguments, calculates RMSD for the input PDB files, and saves the result to an output file.
- Input: Command-line arguments for the two PDB files and the output file name.

## Example Usage
```bash
python RMSD.py protein1.pdb protein2.pdb rmsd_output.txt
```

## Notes
- Ensure that PyMOL is properly installed and configured for the script to run successfully.
- This script can be extended or modified to accommodate additional processing steps or different RMSD calculation methods.

## TODO
- Currently, there are no pending tasks.