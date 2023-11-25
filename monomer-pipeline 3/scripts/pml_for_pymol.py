import sys
import os

## Kritika's comments: 
## This script creates a pymol script for you with the WT and Variant strucutres superimposed and coloured!
## pdb_file_a will be pink and pdb_file_b will be blue 
## Output will be a directory that include the .pml script, move/copy pdb_file_a and pdb_file_b into the directory then run the .pml
##   script in pyMOL - it will automically load the structures for you :) 
## (you can modify it to copy the pdb files into the directory to simplify this even more)

def generate_pymol_script(pdb_file_a, pdb_file_b, residue, output_folder):
    script = f'''
# Load PDB files
load {pdb_file_a}, pdb_file_a
load {pdb_file_b}, pdb_file_b

# Select residues
select res_a, (pdb_file_a and chain A and resi {residue})
select res_b, (pdb_file_b and chain A and resi {residue})

# Align chains
align pdb_file_b and chain A, pdb_file_a and chain A

# Change colors
color lightpink, pdb_file_a
color lightblue, pdb_file_b
color hotpink, res_a
color blue, res_b

# Show residues in stick form
show sticks, res_a
show sticks, res_b

# Center view on aligned structures
center (all)

# Save the session
save {output_folder}/aligned_structure.pse
'''

    with open(f'{output_folder}/pymol_script.pml', 'w') as f:
        f.write(script)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python pml_for_pymol.py pdb_file_a.pdb pdb_file_b.pdb residue output_folder")
        sys.exit(1)

    pdb_file_a = sys.argv[1]
    pdb_file_b = sys.argv[2]
    residue = sys.argv[3]
    output_folder = sys.argv[4]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    generate_pymol_script(pdb_file_a, pdb_file_b, residue, output_folder)
    print(f"PyMOL script generated in '{output_folder}' folder")
