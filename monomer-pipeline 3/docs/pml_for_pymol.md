# PyMOL Script Generator
The PyMOL Script Generator is a Python script designed to automate the creation of a PyMOL script for visualizing and comparing two protein structures (WT and Variant). The generated script will superimpose the structures and color them differently for easy comparison. The output is a directory containing the `.pml` script.

## Requirements
1. Python 3.x
2. PyMOL installed and accessible via the command line.

## Usage
The script can be run from the command line using the following format:

```bash
python pml_for_pymol.py <pdb_file_a> <pdb_file_b> <residue> <output_folder>
```

- `<pdb_file_a>`: Path to the first protein structure PDB file (usually the wildtype).
- `<pdb_file_b>`: Path to the second protein structure PDB file (usually the variant).
- `<residue>`: The residue number to be highlighted in the visualization.
- `<output_folder>`: The name of the output folder where the `.pml` script will be saved.

## Output
The script generates a folder specified by the `<output_folder>` argument. This folder will contain the `.pml` script for PyMOL.

## Limitations
- The script assumes that PyMOL is properly installed and accessible via the command line.
- Errors during execution are reported to the console, but the script does not attempt to recover or retry failed processes.

## Functions
### `generate_pymol_script(pdb_file_a, pdb_file_b, residue, output_folder)`
- Description: Generates a PyMOL script for visualizing and comparing two protein structures.
- Arguments:
  - `pdb_file_a`: Path to the first input PDB file (usually the wildtype).
  - `pdb_file_b`: Path to the second input PDB file (usually the variant).
  - `residue`: The residue number to be highlighted.
  - `output_folder`: The name of the output folder where the `.pml` script will be saved.
- Output: A `.pml` script saved in the specified output folder.

## Example Usage
```bash
python pml_for_pymol.py protein_wildtype.pdb protein_variant.pdb 42 output_folder_name
```

## Notes
- Ensure that PyMOL is properly installed and configured for the script to run successfully.
- After generating the `.pml` script, move or copy the PDB files into the output folder. Then, run the `.pml` script in PyMOL to automatically load and visualize the structures.
- This script can be extended or modified to accommodate additional visualization options or different alignment methods.

## TODO
- Consider adding functionality to automatically copy the PDB files into the output folder to simplify the process further.