"""
=========================================================
Module: Data Extraction Pipeline (NCBI SRA Toolkit)
Developed by: Ibrahim Mustafa (ID: 4231439)
Role: Automation Engineer
Research Criteria & Sample IDs Provided by: Ahmed Refaat
=========================================================
"""

import os
import subprocess
import csv

OUTPUT_DIR = "data"
METADATA_FILE = "metadata.csv"

HEALTHY_SAMPLES = ["SRR12096039", "SRR12096038", "SRR12096037", "SRR12096036", "SRR12096035"]
DIABETIC_SAMPLES = ["SRR12096024", "SRR12096020", "SRR12096019", "SRR12096018", "SRR12096016"]

NUM_READS = 5000

os.makedirs(OUTPUT_DIR, exist_ok=True)

def download_sra_sample(srr_id):
    """
    Downloads exactly 5000 reads from an SRA sample using fastq-dump.
    Requires SRA Toolkit to be installed on the system.
    """
    print(f"Downloading {NUM_READS} reads for {srr_id}...")
    
    command = f"fastq-dump -X {NUM_READS} --outdir {OUTPUT_DIR} {srr_id}"
    
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Success: {srr_id}.fastq saved in {OUTPUT_DIR}/")
    except subprocess.CalledProcessError:
        print(f"Error downloading {srr_id}. Make sure SRA Toolkit is installed and in your system PATH.")

def main():
    metadata_records = []
    
    print("Starting SRA real data extraction...")

    for srr in HEALTHY_SAMPLES:
        download_sra_sample(srr)
        metadata_records.append([srr, "0", "Healthy"])

    for srr in DIABETIC_SAMPLES:
        download_sra_sample(srr)
        metadata_records.append([srr, "1", "Type 2 Diabetes"])

    print("\nGenerating metadata.csv...")
    with open(METADATA_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["sample_id", "class_label", "disease_type"])
        writer.writerows(metadata_records)
        
    print(f"\nAll done! Check the '{OUTPUT_DIR}/' folder and '{METADATA_FILE}'.")

if __name__ == "__main__":
    main()