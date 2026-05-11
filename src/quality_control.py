import os
from fastq_parser import parse_fastq

def calculate_qc_metrics(parsed_data, output_report="qc_report.txt"):
    """
    Computes GC content, Q20, Q30, and saves a text report.
    """
    total_reads = len(parsed_data)
    if total_reads == 0:
        return "No data to analyze."

    total_length = 0
    gc_count = 0
    total_bases = 0
    q20_count = 0
    q30_count = 0

    for read in parsed_data:
        seq = read["Sequence"]
        qual = read["Quality"]

        length = len(seq)
        total_length += length
        total_bases += length

        gc_count += seq.count('G') + seq.count('C')

        for q in qual:
            if q >= 20:
                q20_count += 1
            if q >= 30:
                q30_count += 1

    avg_read_length = total_length / total_reads if total_reads > 0 else 0
    gc_content = (gc_count / total_bases) * 100 if total_bases > 0 else 0
    q20_percentage = (q20_count / total_bases) * 100 if total_bases > 0 else 0
    q30_percentage = (q30_count / total_bases) * 100 if total_bases > 0 else 0

    report = (
        f"--- Premium Quality Control Report ---\n"
        f"Total Reads: {total_reads}\n"
        f"Average Read Length: {avg_read_length:.2f} bp\n"
        f"GC Content: {gc_content:.2f}%\n"
        f"Q20 Percentage: {q20_percentage:.2f}%\n"
        f"Q30 Percentage: {q30_percentage:.2f}%\n"
        f"--------------------------------------\n"
    )

    with open(output_report, "w") as f:
        f.write(report)

    print(f"Report generated successfully: {output_report}")
    print(report)

if __name__ == "__main__":
    sample_file = "../data/cancer_01.fastq"
    output_file = "../qc_report.txt"
    
    try:
        print(f"Parsing data from {sample_file}...")
        data = parse_fastq(sample_file)
        print("Calculating Quality Metrics...")
        calculate_qc_metrics(data, output_report=output_file)
    except FileNotFoundError:
        print(f"Error: File '{sample_file}' not found. Please check the path.")