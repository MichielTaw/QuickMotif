import sys
#sys.path.append('src')  
#sys.path.append('data')  

import random

from helper import random_sequence_generator , generate_k_random, update_k_mers
from fasta import Fasta
from matrix import Matrix
from sequence import Sequence


##NEED FOR THE 
def loop(fasta_path , k_mer , sample_per_sequence, num_iterations):
    dna = Fasta(fasta_path)
    parsed_dna = dna.parse()
    k_mers_motif = generate_k_random(parsed_dna, k_mer, sample_per_sequence) 
    matrice = Matrix(k_mers_motif)
    indice, random_seq = random_sequence_generator(parsed_dna)
    seq = Sequence(random_seq)
    pwm = matrice.PWM(indice)
    scores= seq.ScoreSequence(pwm)
    new_motif = seq.generate_kmer(pwm)
    update_k_mers(k_mers_motif, indice, new_motif)
    for i in range(num_iterations):
        matrice = Matrix(k_mers_motif)
        indice, random_seq = random_sequence_generator(parsed_dna)
        seq = Sequence(random_seq)
        pwm = matrice.PWM(indice)
        scores= seq.ScoreSequence(pwm)
        new_motif = seq.generate_kmer(pwm)
        update_k_mers(k_mers_motif, indice, new_motif)
    return matrice.PlotMatrix(pwm)
