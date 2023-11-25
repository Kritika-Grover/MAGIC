import sys
from pymol import cmd

## Kritika's comments
## This calculates the RMSD of two pdb files and returns the RSMD in an output file
## The usuage is: python RMSD.py pdb_file1 pdb_file2 outputfile.name"

def calculate_rmsd(pdb_file1, pdb_file2):
    cmd.load(pdb_file1, "reference")
    cmd.load(pdb_file2, "mobile")
    rmsd = cmd.align("mobile", "reference")[0]
    cmd.delete("mobile")
    cmd.delete("reference")
    return rmsd

def main():
    if len(sys.argv) != 4:
        print("not enough arguments")
        return

    pdb_file1 = sys.argv[1]
    pdb_file2 = sys.argv[2]
    output_file = sys.argv[3]

    rmsd = calculate_rmsd(pdb_file1, pdb_file2)

    with open(output_file, 'w') as file:
        file.write(f"RMSD between {pdb_file1} and {pdb_file2}: {rmsd:.4f} Å\n")

    cmd.quit()

    print(f"RMSD calculated and saved to {output_file}")

if __name__ == "__main__":
    main()
