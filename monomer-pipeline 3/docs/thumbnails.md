# PDB File Visualization and Export Using PyMOL
This Python script uses PyMOL to load two Protein Data Bank (PDB) files, visualize them, and then export them as PNG images. The output PNG files are saved to a specified output folder.

## Requirements
- Python 3.x
- `os` library
- `argparse` library
- `pymol` package

You can install `pymol` from PyPI using pip, but the process might be different depending on your system.

## Usage
To run the script, execute the following command:
```bash
python script_name.py <pdb_path1> <pdb_path2> <output_folder>
```
- `script_name.py`: The name of this Python script.
- `<pdb_path1>`: Path to the first PDB file.
- `<pdb_path2>`: Path to the second PDB file.
- `<output_folder>`: Path to the folder where the PNG images will be saved.

## Output
- PNG files: Visualizations of the loaded PDB files, saved in the specified output folder.

## Limitations
- The script is designed to work with PDB files only.
- Only supports exporting as PNG images.

## Functions

### `load_and_export_pdb(pdb_path1, pdb_path2, output_folder)`
Loads and exports two PDB files as PNG images.

#### Parameters
- `pdb_path1`: Path to the first PDB file.
- `pdb_path2`: Path to the second PDB file.
- `output_folder`: Path to the output folder where the PNG files will be saved.

#### Returns
- None, but it saves PNG files to the output folder.

---

### `process_pdb_file(pdb_path, molecule_id, output_folder)`
Helper function within `load_and_export_pdb`. It loads a PDB file, zooms in, exports a PNG image, and then deletes the molecule from PyMOL's frame to clear it for the next molecule.

#### Parameters
- `pdb_path`: Path to the PDB file to process.
- `molecule_id`: Identifier for the molecule within PyMOL.
- `output_folder`: Directory where to save the PNG files.

#### Returns
- None, but it saves a PNG file to the output folder.

---

### `main(pdb_path1, pdb_path2, output_folder)`
Initializes PyMOL, sets it to quiet mode, ensures the output folder exists, and then calls `load_and_export_pdb`.

#### Parameters
- `pdb_path1`: Path to the first PDB file.
- `pdb_path2`: Path to the second PDB file.
- `output_folder`: Path to the folder where PNG images will be saved.

#### Returns
- None, but it initializes PyMOL and triggers the loading and exporting process.

## Example Usage
Let's say you have two PDB files located at `/path/to/file1.pdb` and `/path/to/file2.pdb`, and you want to save the PNGs in `/path/to/output_folder`. Execute the following command:
```bash
python script_name.py /path/to/file1.pdb /path/to/file2.pdb /path/to/output_folder
```
This will generate PNG visualizations in the output folder.

## Notes
- PyMOL is set to "quiet mode" and the background is set to white for cleaner images.
- If the specified output folder doesn't exist, the script will create it.

## TODO
- Add more options for file types to export (e.g., JPG, GIF).
- Allow customization of the PyMOL settings like colors and rendering options.
- Implement error handling to make the script more robust.