import re
import argparse
import random
from Bio import SeqIO

def find_longest_repeated_subsequence(sequence):
    length = 1
    result = ''
    while True:
        regex = r'([GATC]{' + str(length) + r'}).*\1'
        match = re.search(regex, sequence)
        if match:
            result = match.group(1)
            length += 1
        else:
            break
    return result

def calculate_gc_content(sequence):
    gc_count = sum(1 for base in sequence if base in 'GC')
    return (gc_count / len(sequence)) * 100

def main(file_path, find_duplicate, calculate_gc):
    for record in SeqIO.parse(file_path, "fasta"):
        sequence = str(record.seq)
        
        if find_duplicate:
            longest_dup = find_longest_repeated_subsequence(sequence)
            print(f"Longest repeated subsequence: {longest_dup} (Length: {len(longest_dup)})")
        
        if calculate_gc:
            gc_content = calculate_gc_content(sequence)
            print(f"GC content: {gc_content:.2f}%")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze sequences from a Fasta or GeneBank file.")
    parser.add_argument("file", help="Path to the input file in Fasta or GeneBank format")
    parser.add_argument("--duplicate", action="store_true", help="Find the longest repeated sub-sequence")
    parser.add_argument("--gc_content", action="store_true", help="Calculate the GC content")

    args = parser.parse_args()
    main(args.file, args.duplicate, args.gc_content)
