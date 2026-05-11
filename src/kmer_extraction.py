import pandas as pd
from collections import Counter
from fastq_parser import parse_fastq

def extract_kmers(parsed_data, k=3):
    """
    Extracts K-mer frequencies from FASTQ sequences.
    """
    kmer_counts = Counter()
    
    for read in parsed_data:
        seq = read["Sequence"]
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i+k]
            kmer_counts[kmer] += 1
            
    return kmer_counts

if __name__ == "__main__":
    sample_file = "../data/cancer_01.fastq"
    output_file = "../features.csv"
    
    try:
        print(f"Reading data from {sample_file}...")
        data = parse_fastq(sample_file)
        
        print("Extracting 3-mers (This might take a few seconds)...")
        kmers = extract_kmers(data, k=3)
        
        df = pd.DataFrame(list(kmers.items()), columns=['Feature_Kmer', 'Frequency'])
        df['Class_Label'] = 'Disease' 
        
        df.to_csv(output_file, index=False)
        print(f"Success! Features saved to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: File '{sample_file}' not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")