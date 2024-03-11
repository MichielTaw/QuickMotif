import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
nucleotides = ['A', 'C', 'G', 'T']

class Matrix():
    def __init__(self, k_mers  ):
        self.k_mers = k_mers
        
    def PFM(self, random_seq_index):
        self.random_seq_index= random_seq_index
        k_mers = self.k_mers.copy() # Create a copy to avoid modifying the original list
        total_motifs = len(k_mers)
        k_mer_length = len(k_mers[0])
        k_mers.pop(random_seq_index)  # Remove the k-mer at the given index
        nucleotides = ['A', 'C', 'G', 'T']
        nucleotide_frequencies = [{"A": 0, "C": 0, "G": 0, "T": 0} for _ in range(k_mer_length)]
    
        for motif in k_mers:
            for i, nucleotide in enumerate(motif):
                nucleotide_frequencies[i][nucleotide] += 1
        for pos_freq in nucleotide_frequencies:
            for nucleotide in pos_freq:
                pos_freq[nucleotide] /= total_motifs

        matrix = np.zeros((4, k_mer_length))
        for j, freq in enumerate(nucleotide_frequencies):
            for i, nucleotide in enumerate(nucleotides):
                matrix[i, j] = freq[nucleotide]

        return matrix

    
    def PWM(self, random_seq_index):
        pfm = self.PFM(random_seq_index) 
        background_freq = 0.25
        pwm = np.log2((pfm + 1e-6 ) / background_freq)  # Adding a small constant to avoid log(0)
        return pwm


    def PlotMatrix(self, matrice):
        random_seq_index = self.random_seq_index
        matrix = self.PFM(random_seq_index)
        plt.figure(figsize=(20, 4))
        sns.heatmap(matrice, annot=True, cmap="viridis", xticklabels=range(1, matrix.shape[1]+1), yticklabels=nucleotides, cbar_kws={"label": "Frequency"})
        plt.title("Nucleotide Frequency at Each Position")
        plt.xlabel("Position in Motif")
        plt.ylabel("Nucleotide")
        plt.show()
        