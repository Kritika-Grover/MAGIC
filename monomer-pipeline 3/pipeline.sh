#!/bin/bash

# Function to display usage information
usage() {
    echo "Usage: ./pipeline.sh -d <pdbs_dir> -r <residue_number> -n <name> -c <chimera_path> -e <evoef_path> -o <output_folder>"
    echo ""
    echo "Options:"
    echo "-d <pdbs_dir>       Directory containing PDB files"
    echo "-r <residue_number> Residue number"
    echo "-n <name>           Name"
    echo "-c <chimera_path>   Path to Chimera executable"
    echo "-e <evoef_path>     Path to EvoEF2 script"
    echo "-o <output_folder>  Output folder path"
    exit 1
}

# Parse command line arguments
while getopts ":d:r:n:c:e:o:" opt; do
  case ${opt} in
    d ) pdbs_dir=$OPTARG;;
    r ) residue_number=$OPTARG;;
    n ) name=$OPTARG;;
    c ) chimera_path=$OPTARG;;
    e ) evoef_path=$OPTARG;;
    o ) output_folder=$OPTARG;;
    \? ) usage;;
    : ) echo "Invalid option: $OPTARG requires an argument" 1>&2; exit 1;;
  esac
done
shift $((OPTIND -1))

# Check if all required command line arguments are provided
if [[ -z $pdbs_dir || -z $residue_number || -z $name || -z $chimera_path || -z $evoef_path || -z $output_folder ]]; then
    usage
fi

# Python scripts folder
# Get the absolute path of the current script file
current_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Absolute path to the scripts folder
scripts_folder="$current_dir/scripts"

# Step 1: Run closest_ranks.py to determine
#         closest PDBs around missense resi.
python "${scripts_folder}/closest_ranks.py" $residue_number -w "${pdbs_dir}/wt" -v "${pdbs_dir}/ms" -o "${name}.ranks"

# Check if closest_ranks.py succeeded
if [ $? -ne 0 ]; then
    echo "Error in running closest_ranks.py"
    exit 1
fi

# Extract the first two lines (paths to two files from wt and ms) from name.ranks
wt_file=$(sed -n '1p' "${name}.ranks")
ms_file=$(sed -n '2p' "${name}.ranks")

# Create a new directory called 'tmp' and copy wt and ms files into it
mkdir -p tmp
cp $wt_file "tmp/wt_$(basename $wt_file)"
cp $ms_file "tmp/ms_$(basename $ms_file)"

# Run Steps 2, 3, and 4 in the background
python3.11 "${scripts_folder}/RMSD.py" "tmp/wt_$(basename $wt_file)" "tmp/ms_$(basename $ms_file)" "${name}.rmsd" &
PID1=$!

python "${scripts_folder}/energetics.py" -w "tmp/wt_$(basename $wt_file)" -v "tmp/ms_$(basename $ms_file)" -f $evoef_path &
PID2=$!

python "${scripts_folder}/chimera.py" tmp --chimera $chimera_path --output_folder $output_folder &
PID3=$!

# Wait for all background processes to complete
wait $PID1 $PID2 $PID3

# Check if any of the processes failed
if [ $? -ne 0 ]; then
    echo "Error in one of the parallel steps."
    exit 1
fi

# Create the output folder if it doesn't exist
mkdir -p $output_folder

# Move contents of 'tmp' into the new directory
mv tmp/* "$output_folder/"
rm -r tmp

# Move energetics output to the new folder
mv energetics_WT.txt energetics_V.txt filtered_energetics_WT.txt filtered_energetics_V.txt "$output_folder/"

# Move {name}.ranks and {name}.rmsd into the new directory
mv "${name}.ranks" "${name}.rmsd" "$output_folder/"

python3.11 ${scripts_folder}/thumbnails.py ${output_folder}/wt_*.pdb ${output_folder}/ms_*.pdb $output_folder/

python3.11 ${scripts_folder}/report/report.py $output_folder/ 

# Clean up output folder
mkdir -p ${output_folder}/raw_output
cd $output_folder

shopt -s extglob
find . -maxdepth 1 -type f ! -name '*.pdf' ! -name '*.csv' -exec mv {} raw_output \;


echo "Pipeline completed successfully."