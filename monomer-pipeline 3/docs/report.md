# Missense Mutation Analysis Report Generator
This Python script automates the generation of a missense mutation analysis report. The report includes various metrics like H-bonds, energetics, and RMSD values to provide insights into the differences between wild type and missense mutations. It creates an HTML table to visualize these metrics, generates a PDF report, and writes the data into a CSV file.

## Requirements
- Python 3.x
- `glob` library
- `os` library
- `argparse` library
- `csv` library
- `re` library
- `weasyprint` library (For generating PDFs)

You can install `weasyprint` using pip:
```bash
pip install weasyprint
```

## Usage
To run the script, use the following command:
```bash
python script_name.py <input_folder>
```
- `script_name.py`: Name of this Python script file.
- `<input_folder>`: Path to the folder containing the analysis files like `.ranks`, `.rmsd`, `.txt`, and `.png`.

## Output
- PDF report: A PDF file that includes an HTML table with all the metrics and differences between the wild type and missense mutations.
- CSV file: A CSV file containing the same metrics in tabular form.

## Limitations
- The input folder must contain specific file types (`.ranks`, `.rmsd`, `.txt`, `.png`) with specific naming conventions for the script to work correctly.
- Only the first file that matches the given pattern is used for each type of metric.

## Functions

### `read_file(file_path)`
Reads a file and returns its content as a string after stripping any leading and trailing whitespaces.

#### Parameters
- `file_path`: The full path to the file to read.

#### Returns
- The content of the file as a string.

---

### `get_hbonds(input_folder, file_pattern, regex_pattern)`
Searches for hydrogen bonds (H-bonds) in the provided folder based on a file pattern and a regular expression.

#### Parameters
- `input_folder`: The folder where the file should be searched for.
- `file_pattern`: A pattern that filenames should match (wildcards like `*` can be used).
- `regex_pattern`: A regular expression pattern that filenames should match.

#### Returns
- The number of H-bonds as an integer if found, otherwise `None`.

---

### `main(input_folder)`
The main function that orchestrates the entire flow of reading files, calculating metrics, and generating reports.

#### Parameters
- `input_folder`: Path to the folder containing the analysis files.

#### Returns
- None, but it generates a PDF report and a CSV file.

## Example Usage
Let's say you have an input folder at `/path/to/input_folder` that contains all the required analysis files. Run the script as follows:
```bash
python script_name.py /path/to/input_folder
```
This will generate a PDF report and a CSV file in the same input folder.

## Notes
- The script expects specific naming conventions for the files. Make sure your input files follow these.
- The styles for the HTML content are supposed to be in a file named `styles.css` in the same directory as this script.

## TODO
- Make the script more flexible to accept different file naming conventions.
- Allow custom styling for the HTML content.
- Implement error-handling to make the script more robust.