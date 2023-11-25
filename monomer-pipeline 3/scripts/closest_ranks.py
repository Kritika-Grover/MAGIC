import os
import argparse
import numpy as np
from Bio.SVDSuperimposer import SVDSuperimposer
from itertools import product

## Kritika's comments:
## The command line usage for this script is: python closest_ranks.py residue_number -w wild_type_dir -v variant_dir -o outputfile.name 
## This script will compare the xyz coordinate distance for the residue number for each wild_type.pdb and variant.pdb predicted by Alphafold2
##  it will go over all 25 possibilites and the outputfile will have the closest pair and the distance between the superimposed residue  

def read_coordinates(pdb_path, residue_number):
    coordinates = []
    with open(pdb_path, 'r') as pdb_file:
        for line in pdb_file:
            if line.startswith('ATOM'):
                atom_residue_number = int(line[22:26])
                if atom_residue_number == residue_number:
                    x = float(line[30:38])
                    y = float(line[38:46])
                    z = float(line[46:54])
                    coordinates.append((x, y, z))
    return np.array(coordinates)

def calculate_average_coordinates(coords_list):
    return np.mean(coords_list, axis=0)

def calculate_distance(coord1, coord2):
    return np.linalg.norm(coord1 - coord2)


def main():
    parser = argparse.ArgumentParser(description="Compare average coordinates of a specific residue between wild type and variant PDB files.")
    parser.add_argument("residue_number", type=int, help="Index of the residue to compare")
    parser.add_argument("-w", "--wildtype_directory", help="Directory containing wild type PDB files", required=True)
    parser.add_argument("-v", "--variant_directory", help="Directory containing variant PDB files", required=True)
    parser.add_argument("-o", "--output_file", help="Output file to store the results", required=True)
    args = parser.parse_args()

    wildtype_files = [os.path.join(args.wildtype_directory, filename) for filename in os.listdir(args.wildtype_directory) if filename.endswith('.pdb')]
    variant_files = [os.path.join(args.variant_directory, filename) for filename in os.listdir(args.variant_directory) if filename.endswith('.pdb')]

    wildtype_coords = [read_coordinates(file, args.residue_number) for file in wildtype_files]
    variant_coords = [read_coordinates(file, args.residue_number) for file in variant_files]

    if not wildtype_coords or not variant_coords:
        print("No matching pairs of structures found for comparison.")
        return

    min_distance = float('inf')
    closest_wildtype_file = None
    closest_variant_file = None

    common_atom_names = ["N", "CA", "C", "O", "NH1", "NH2", "CA", "CB"]  

    for wild_idx, variant_idx in product(range(len(wildtype_coords)), repeat=2):
        wild_coords = wildtype_coords[wild_idx]
        current_variant_coords = variant_coords[variant_idx] 

    # Extract coordinates for the common atoms only
        wild_common_coords = [coord for atom_name, coord in zip(common_atom_names, wild_coords) if atom_name in common_atom_names]
        variant_common_coords = [
            coord for atom_name, coord in zip(common_atom_names, current_variant_coords) 
            if atom_name in common_atom_names
        ]

    # Check if the number of common coordinates is the same for wild type and variant
        if len(wild_common_coords) != len(variant_common_coords):
            continue  # Skip this comparison if the number of common coordinates is different

        superimposer = SVDSuperimposer()
        superimposer.set(np.array(wild_common_coords), np.array(variant_common_coords))
        superimposer.run()

        rmsd = superimposer.get_rms()
        if rmsd < min_distance:
            min_distance = rmsd
            closest_wildtype_file = wildtype_files[wild_idx]
            closest_variant_file = variant_files[variant_idx]
            
    output_content = f"{closest_wildtype_file}\n{closest_variant_file}\nClosest pair: Wild type: {closest_wildtype_file}, Variant: {closest_variant_file}\n"
    output_content += f"RMSD between residues: {min_distance}\n"

    with open(args.output_file, 'w') as output:
        output.write(output_content)

    print(f"Output written to {args.output_file}")

if __name__ == "__main__":
    main()


