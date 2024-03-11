#generate random sequence function
import random
def random_sequence_generator(parsed_dna):
        if not parsed_dna:  # Check if the list is empty
                return None, None  # Or raise an error
        index= random.randint(0, len(parsed_dna)-1)
        random_sequence=parsed_dna[index]
        return index , random_sequence



#generate k-mer function
def generate_k_random( parsed_dna, k_mer, motif_per_sequence):
    if not parsed_dna:
            print("Input list is empty. No motifs generated.")
            return []
    motifs = []            
    for sequence in parsed_dna:
            length = len(sequence)
            if k_mer <= length:
                for _ in range(motif_per_sequence):
                    start_index = random.randint(0, length - k_mer)
                    motif = sequence[start_index:start_index + k_mer]
                    motifs.append(motif)
            else:
                print(f"Sequence length ({length}) is shorter than k-mer length ({k_mer}). Skipping.")
    return motifs

#Update the k-mers with the new one

def update_k_mers(k_mers, index_random_seq, new_k_mer):
    k_mers[index_random_seq] = new_k_mer