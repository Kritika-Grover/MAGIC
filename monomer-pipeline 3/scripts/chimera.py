import os
import subprocess
import argparse

def run_chimera_hbonds(pdbs_dir, output_folder='./output', chimera='chimera'):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through PDB files in the input folder
    for filename in os.listdir(pdbs_dir):
        if filename.endswith(".pdb"):
            pdb_path = os.path.join(pdbs_dir, filename)

            # Run ChimeraX command to count hydrogen bonds
            chimera_cmd = f'{chimera} --nogui --cmd "open {pdb_path} ; hbonds ; exit"'

            # Execute the ChimeraX command using subprocess
            try:
                result = subprocess.run(
                    chimera_cmd,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )

                # Extract and parse the hydrogen bond count from the ChimeraX output
                output_lines = result.stdout.strip().split("\n")
                hydrogen_bond_count = 0
                for line in output_lines:
                    if "hydrogen bonds found" in line:
                        hydrogen_bond_count = int(line.split(" ")[0].strip())
                        break

                # Create a new text file with the hydrogen bond count
                output_filename = os.path.splitext(filename)[0] + ".txt"
                output_path = os.path.join(output_folder, output_filename)

                # Write the entire stdout to a log file
                log_filename = os.path.splitext(filename)[0] + "_log.txt"
                log_path = os.path.join(output_folder, log_filename)
                with open(log_path, 'w') as log_file:
                    log_file.write(result.stdout)

                # Write the hydrogen bond count to the output file
                with open(output_path, 'w') as output_file:
                    output_file.write(f"Number of Hydrogen Bonds: {hydrogen_bond_count}\n")

                print(f"Processed {filename}: {hydrogen_bond_count} hydrogen bonds")

            except Exception as e:
                print(f"Error processing {pdb_path}: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run ChimeraX to count hydrogen bonds for PDB files.")
    parser.add_argument("pdbs_dir", help="Directory containing the PDB files.")
    parser.add_argument("--output_folder", default="./output", help="Output folder for results.")
    parser.add_argument("--chimera", required=True, help="Path to the ChimeraX executable.")

    args = parser.parse_args()

    run_chimera_hbonds(args.pdbs_dir, args.output_folder, args.chimera)
