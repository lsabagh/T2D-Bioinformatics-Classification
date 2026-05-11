from Bio import SeqIO

def parse_fastq(file_path):
    """
    Reads a FASTQ file and extracts ID, Sequence, and Quality Scores
    using the Biopython library.
    """
    parsed_data = []
    
    for record in SeqIO.parse(file_path, "fastq"):
        read_info = {
            "ID": record.id,
            "Sequence": str(record.seq),
            "Quality": record.letter_annotations["phred_quality"]
        }
        parsed_data.append(read_info)
        
    return parsed_data

if __name__ == "__main__":
    sample_file = "../data/cancer_01.fastq" 
    try:
        data = parse_fastq(sample_file)
        print(f"Successfully parsed {len(data)} reads.")
        print(f"Sample Read 1 ID: {data[0]['ID']}")
    except FileNotFoundError:
        print(f"Error: File '{sample_file}' not found. Please check the path.")