#import dependency:
from matplotlib import pyplot as plt
import random
from Bio import SeqIO

nucleotides = ['A', 'C', 'G', 'T']


class Fasta():
    def __init__(self, fasta_path):
        self.fasta_path= fasta_path
    
    def parse(self):
        fasta_parsed = [record.seq.upper() for record in SeqIO.parse(self.fasta_path, "fasta")]
        return fasta_parsed
    def count(self ,symbol):
        total = 0
        with open (self.fasta_path, "r") as fasta:
            for line in fasta:
                if line.startswith(symbol):
                    total +=1
        return total
    
    def nucleotide_frequencies(self):
        nucleotide_counts = {nucleotide: 0 for nucleotide in nucleotides}
        sequences = self.parse()  # Reuse the parse method
        for seq in sequences:
            for nucleotide in seq:
                if nucleotide in nucleotide_counts:
                    nucleotide_counts[nucleotide] += 1
        total_nucleotides = sum(nucleotide_counts.values())
        nucleotide_freqs = {nucleotide: count / total_nucleotides for nucleotide, count in nucleotide_counts.items()}
        return nucleotide_freqs


        
    def __str__(self):
        return f"Fasta file at {self.fasta_path}"