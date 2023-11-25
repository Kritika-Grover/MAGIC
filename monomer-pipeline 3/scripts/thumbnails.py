import os
import argparse
from pymol import cmd

def load_and_export_pdb(pdb_path1, pdb_path2, output_folder):

    cmd.bg_color("white")
    cmd.set("ray_opaque_background", "off")

    # Load the first PDB file
    def process_pdb_file(pdb_path, molecule_id, output_folder):
        # Load the PDB file
        print(f"Loading the {molecule_id} PDB file...")
        cmd.load(pdb_path, molecule_id)
    
        # Zoom in to fill the frame
        print(f"Zooming in on the {molecule_id} PDB file...")
        cmd.zoom(molecule_id)
    
        # Export PNG for the molecule
        print(f"Exporting PNG for the {molecule_id} PDB file...")
        cmd.png(os.path.join(output_folder, os.path.basename(pdb_path).split(".")[0] + '.png'), ray=1)
        
        # Delete the molecule to clear the frame
        print(f"Clearing the {molecule_id} PDB file...")
        cmd.delete(molecule_id)

    # Process the first PDB file
    process_pdb_file(pdb_path1, 'molecule1', output_folder)

    # Process the second PDB file
    process_pdb_file(pdb_path2, 'molecule2', output_folder)

def main(pdb_path1, pdb_path2, output_folder):
    # Initialize PyMOL
    print("Initializing PyMOL...")
    cmd.reinitialize()

    # Set to quiet mode
    print("Setting PyMOL to quiet mode...")

    # Make sure the output folder exists
    if not os.path.exists(output_folder):
        print(f"Creating output folder at {output_folder}...")
        os.makedirs(output_folder)
    
    # Perform the load and export operations
    load_and_export_pdb(pdb_path1, pdb_path2, output_folder)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load and export PDB files using PyMOL.")
    parser.add_argument("pdb_path1", help="Path to the first PDB file")
    parser.add_argument("pdb_path2", help="Path to the second PDB file")
    parser.add_argument("output_folder", help="Path to the output folder")
    args = parser.parse_args()
    main(args.pdb_path1, args.pdb_path2, args.output_folder)

