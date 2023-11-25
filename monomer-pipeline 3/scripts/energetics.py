import argparse
import subprocess
import os

def run_evoef(pdb_path, evoef, output_file):
    cmd_list =  [evoef, '--command=ComputeStability', f'--pdb={pdb_path}']
    print(" ".join(cmd_list))
    try:
        # Run the evoef command and capture stdout
        with open(output_file, 'w') as stdout_file:
            subprocess.run(
                cmd_list,
                stdout=stdout_file,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
        print(f"EvoEF command completed successfully for {pdb_path}. Output saved to '{output_file}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing evoef command for {pdb_path}. Return code: {e.returncode}")
        print("Error Output:")
        print(e.stderr)
    except Exception as e:
        print(f"An error occurred for {pdb_path}:", str(e))

def extract_total_energy(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
            for line in lines:
                if line.startswith("Total"):
                    total_energy = float(line.split('=')[1].strip())
                    with open(output_file, 'a') as outfile:
                        outfile.write(f"{total_energy}\n")    
                    print(f"Total energy {total_energy} extracted and written to {output_file}")
                    return
            print("Line starting with 'Total' not found in the input file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description='Run EvoEF1 command on two PDB files and filter the output.')

    parser.add_argument('-w', '--wildtype-pdb', help='Path to wildtype PDB file.', required=True)
    parser.add_argument('-v', '--variant-pdb', help='Path to variant PDB file.', required=True)
    parser.add_argument('-f', '--evoef', help='Path to the EvoEF1 executable.', required=True)
    
    args = parser.parse_args()

    args = parser.parse_args()
    
    run_evoef(args.wildtype_pdb, args.evoef, 'energetics_WT.txt')
    run_evoef(args.variant_pdb, args.evoef, 'energetics_V.txt')
    
    extract_total_energy('energetics_WT.txt', 'filtered_energetics_WT.txt')
    extract_total_energy('energetics_V.txt', 'filtered_energetics_V.txt')

if __name__ == "__main__":
    main()
