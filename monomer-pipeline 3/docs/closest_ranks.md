# Closest Ranks for Residue Coordinates Script
The Closest Ranks for Residue Coordinates Script is a Python script designed to compare the XYZ coordinates of a specific residue across multiple PDB files for wild type and variant proteins. The script uses the BioPython library's SVDSuperimposer to superimpose the structures and find the pair with the closest RMSD (Root Mean Square Deviation).

## Requirements
1. Python 3.x
2. BioPython library installed (`pip install biopython`)
3. NumPy library installed (`pip install numpy`)

## Usage
The script can be run from the command line using the following format:

```bash
python closest_ranks.py <residue_number> -w <wild_type_dir> -v <variant_dir> -o <output_file>
```

- `<residue_number>`: The residue number to be compared across the PDB files.
- `<wild_type_dir>`: Directory containing the wild type PDB files.
- `<variant_dir>`: Directory containing the variant PDB files.
- `<output_file>`: Name of the output file where the results will be saved.

## Output
The script generates a single output file specified by the `<output_file>` argument. This file contains the names of the PDB files with the closest RMSD and the RMSD value itself.

## Limitations
- The script assumes that BioPython and NumPy are properly installed.
- Errors during execution are reported to the console, but the script does not attempt to recover or retry failed processes.

## Functions
### `read_coordinates(pdb_path, residue_number)`
- Description: Reads the XYZ coordinates of a specific residue from a PDB file.
- Arguments:
  - `pdb_path`: Path to the PDB file.
  - `residue_number`: The residue number to be read.
- Output: A NumPy array containing the XYZ coordinates.

### `calculate_average_coordinates(coords_list)`
- Description: Calculates the average coordinates from a list of coordinates.
- Arguments:
  - `coords_list`: List of coordinates.
- Output: A NumPy array containing the average coordinates.

### `calculate_distance(coord1, coord2)`
- Description: Calculates the Euclidean distance between two sets of coordinates.
- Arguments:
  - `coord1`: First set of coordinates.
  - `coord2`: Second set of coordinates.
- Output: The Euclidean distance.

### `main()`
- Description: The main function that parses command-line arguments, reads coordinates from PDB files, and finds the pair with the closest RMSD.
- Input: Command-line arguments for the residue number, directories, and output file name.

## Example Usage
```bash
python closest_ranks.py 42 -w wild_type_pdb_files -v variant_pdb_files -o closest_ranks_output.txt
```

## Notes
- Ensure that BioPython and NumPy are properly installed and configured for the script to run successfully.
- This script can be extended or modified to accommodate additional comparison metrics or different superimposition methods.

## TODO
- Currently, there are no pending tasks.