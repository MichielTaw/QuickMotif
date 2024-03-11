import numpy as np
class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence
        
    def update_sequence(self, new_sequence):
        self.sequence = new_sequence
        
    def ScoreSequence(self, pwm):
        sequence = self.sequence
        kmer_length = pwm.shape[1] 
        L = len(sequence)
        probabilities = []
        nucleotide_to_row = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        for i in range(L - kmer_length + 1):
            substring = sequence[i:i + kmer_length]
            prob_log = 0  # Log-probability score
            for j, nucleotide in enumerate(substring):
                if nucleotide in nucleotide_to_row:  
                    row_index = nucleotide_to_row[nucleotide]
                    prob_log += pwm[row_index, j]
            probabilities.append(prob_log)
        return probabilities
    
    def generate_kmer(self, pwm):
        sequence = self.sequence
        kmer_length = pwm.shape[1]  # Assuming pwm is a NumPy array
        L = len(sequence)
        
        # Calculate log probabilities for each k-mer
        log_probabilities = []
        nucleotide_to_row = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        for i in range(L - kmer_length + 1):
            substring = sequence[i:i + kmer_length]
            prob_log = 0
            for j, nucleotide in enumerate(substring):
                if nucleotide in nucleotide_to_row:
                    row_index = nucleotide_to_row[nucleotide]
                    prob_log += pwm[row_index, j]
            log_probabilities.append(prob_log)

        # Convert log probabilities to probabilities
        # To avoid underflow, subtract the max log probability and then exponentiate
        max_log_prob = max(log_probabilities)
        probabilities = [np.exp(log_prob - max_log_prob) for log_prob in log_probabilities]
        
        # Normalize the probabilities so they sum to 1
        total_prob = sum(probabilities)
        probabilities = [prob / total_prob for prob in probabilities]
        
        # Sample a k-mer index from this distribution
        kmer_index = np.random.choice(range(L - kmer_length + 1), p=probabilities)
        
        # Return the sampled k-mer
        return sequence[kmer_index:kmer_index + kmer_length]