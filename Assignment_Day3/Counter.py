import argparse

def read_fasta(file_path):
    """Read sequences from a FASTA file."""
    sequences = []
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                    sequence = ''
            else:
                sequence += line.strip().upper()
        if sequence:
            sequences.append(sequence)
    return sequences

def find_most_common_kmer(sequences, k=7):
    """Find the most common k-mer across all sequences."""
    kmer_counts = {}
    for seq in sequences:
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i+k]
            if kmer in kmer_counts:
                kmer_counts[kmer] += 1
            else:
                kmer_counts[kmer] = 1
    most_common_kmer = max(kmer_counts, key=kmer_counts.get)
    count = kmer_counts[most_common_kmer]
    return most_common_kmer, count

def calculate_gc_percentage(seq):
    """Calculate the GC percentage of a sequence."""
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count / len(seq)) * 100 if seq else 0

def analyze_fasta(file_path):
    sequences = read_fasta(file_path)
    most_common_kmer, count = find_most_common_kmer(sequences)
    gc_percentage = calculate_gc_percentage(most_common_kmer)
    return most_common_kmer, count, gc_percentage

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Find the most common 7-mer and its GC percentage in a FASTA file.")
    parser.add_argument("file_path", help="The path to the FASTA file.")
    args = parser.parse_args()

    result = analyze_fasta(args.file_path)
    print(f"Most Common 7-mer: {result[0]}")
    print(f"Occurrences: {result[1]}")
    print(f"GC Percentage: {result[2]:.2f}%")
