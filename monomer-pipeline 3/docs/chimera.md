# ChimeraX Hydrogen Bond Counting Script
This script automates the process of counting hydrogen bonds in Protein Data Bank (PDB) files using the ChimeraX molecular visualization and analysis software. It takes a directory containing PDB files as input and generates a text file for each PDB file with the number of hydrogen bonds found. Additionally, it creates log files to capture the entire ChimeraX output for each PDB file processed.

## Requirements
1. Python 3.x
2. ChimeraX installed and accessible via the command line.

## Usage
The script can be run from the command line using the following format:

```bash
python chimera.py <pdbs_dir> [--output_folder <output_folder>] --chimera <chimera_executable>
```

- `<pdbs_dir>`: The directory containing the PDB files to be processed.
- `--output_folder <output_folder>` (optional): The folder where the script will store the output files (default is "./output").
- `--chimera <chimera_executable>`: The path to the ChimeraX executable.

## Output
The script generates the following output:

1. Text files (one per input PDB file) containing the number of hydrogen bonds found.
2. Log files (one per input PDB file) capturing the entire ChimeraX output.

## Limitations
- This script assumes that ChimeraX is installed and accessible via the command line with the provided `chimera_executable`.
- It works with PDB files only and assumes a specific ChimeraX command format, which may change with future ChimeraX updates.
- Errors during processing are reported to the console, but the script does not attempt to recover or retry failed PDB files.

## Functions
### `run_chimera_hbonds(pdbs_dir, output_folder='./output', chimera='chimera')`
- Description: Counts hydrogen bonds in PDB files using ChimeraX and creates output and log files.
- Arguments:
  - `pdbs_dir`: The directory containing the input PDB files.
  - `output_folder`: The folder where output and log files will be saved (default is "./output").
  - `chimera`: The path to the ChimeraX executable.
- Output: Text and log files for each processed PDB file.

## Example Usage
```bash
python chimera.py /path/to/pdb_files --output_folder /path/to/output --chimera /path/to/chimera_executable
```

## Notes
- Ensure that ChimeraX is properly configured and available in the system's PATH for the script to run successfully.
- This script can be extended or modified to accommodate changes in ChimeraX or additional processing steps.

## TODO
- Currently, there are no pending tasks.