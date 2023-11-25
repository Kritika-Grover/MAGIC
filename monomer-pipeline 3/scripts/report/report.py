import os
import argparse
from glob import glob
import csv
import re
from weasyprint import HTML

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()

def get_hbonds(input_folder, file_pattern, regex_pattern):
    hbonds_files = [f for f in glob(os.path.join(input_folder, file_pattern)) if re.match(regex_pattern, os.path.basename(f))]
    if hbonds_files:
        hbonds_file = hbonds_files[0]
        return int(read_file(hbonds_file).split(': ')[1])
    return None

def main(input_folder):
    input_folder = os.path.abspath(input_folder)

    ranks_file = glob(os.path.join(input_folder, '*.ranks'))[0]
    rmsd_file = glob(os.path.join(input_folder, '*.rmsd'))[0]
    report_name = os.path.basename(ranks_file).split('.')[0]

    wt_image_path = glob(os.path.join(input_folder, 'wt_ranked_*.png'))[0]
    ms_image_path = glob(os.path.join(input_folder, 'ms_ranked_*.png'))[0]

    wt_energetics = float(read_file(os.path.join(input_folder, 'filtered_energetics_WT.txt')))
    v_energetics = float(read_file(os.path.join(input_folder, 'filtered_energetics_V.txt')))

    wt_hbonds = get_hbonds(input_folder, 'wt_ranked_*.txt', r'.*wt_ranked_[0-4]\.txt$')
    ms_hbonds = get_hbonds(input_folder, 'ms_ranked_*.txt', r'.*ms_ranked_[0-4]\.txt$')

    rmsd = float(read_file(rmsd_file).split(': ')[1].split(' ')[0])
    rmsd_residues = float(read_file(ranks_file).split('RMSD between residues: ')[1])

    energetics_diff = v_energetics - wt_energetics
    hbonds_diff = ms_hbonds - wt_hbonds
    
    current_working_dir = os.path.dirname(os.path.abspath(__file__))

    # Create HTML table
    html_content = f"""
<html>
<head>
    <title>{report_name}: Missense Mutation Analysis Report</title>
    <link rel="stylesheet" type="text/css" href="{current_working_dir}/styles.css">
</head>

<body>
    <h1>{report_name}: Missense Mutation Analysis Report</h1>
    <div class="wrapper">
    <table>
        <tr>
            <th></th>
            <th><div class="img-container"><img src="{wt_image_path}" alt="WT Image"></div></th>
            <th><div class="img-container"><img src="{ms_image_path}" alt="MS Image"></div></th>
        </tr>
        <tr>
            <th></th>
            <th>Wild Type</th>
            <th>Missense</th>
        </tr>
        <tr>
            <td class="space-grotesk">H-bonds</td>
            <td>{wt_hbonds}</td>
            <td>{ms_hbonds}</td>
        </tr>
        <tr>
            <td class="space-grotesk">Energetics (kcal/mol)</td>
            <td>{wt_energetics:.3f}</td>
            <td>{v_energetics:.3f}</td>
        </tr>
        <tr>
            <td class="space-grotesk">RMSD (Å)</td>
            <td colspan="2">{rmsd:.3f}</td>
        </tr>
        <tr>
            <td class="space-grotesk">RMSD between residue</td>
            <td colspan="2">{rmsd_residues:.3f}</td>
        </tr>
    </table>
</div>
<div class="card-container">
    <div class="card">
        <div class="card-title">ΔΔG</div>
        <div class="card-value">{energetics_diff:.2f}</div>
        <div class="card-tag">{"stability increases ⬆️" if energetics_diff < 0 else "stability decreases ⬇️"}</div>
    </div>

    <div class="card">
        <div class="card-title">ΔH-bonds</div>
        <div class="card-value">{hbonds_diff}</div>
        <div class="card-tag">{"stability increases ⬆️" if hbonds_diff > 0 else "stability decreases ⬇️"}</div>
    </div>
</div>
</body>
</html>
"""

    # Generate PDF
    HTML(string=html_content, base_url=current_working_dir).write_pdf(f"{input_folder}/{report_name}_report.pdf")

    # Write data to CSV
    csv_data = [
    ['Metric', 'Wild Type', 'Missense', 'Difference'],
    ['H-bonds', wt_hbonds, ms_hbonds, hbonds_diff],
    ['Energetics (kcal/mol)', f"{wt_energetics:.3f}", f"{v_energetics:.3f}", f"{energetics_diff:.3f}"],
    ['RMSD (Å)', '', '', f"{rmsd:.3f}"],
    ['RMSD between residues', '', '', f"{rmsd_residues:.3f}"]
    ]

    with open(f"{input_folder}/{report_name}_data.csv", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(csv_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate analysis report.')
    parser.add_argument('input_folder', type=str, help='Path to the folder containing the analysis files.')
    args = parser.parse_args()
    main(args.input_folder)
