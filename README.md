
# QuickMotif

The aim of this software is to make motif analysis easier and faster. The software takes as input fasta files and can help you to:

Perform Gibbs sampling for a specific k-mer length
Analyze the frequency of nucleotides
Parse DNA
Generate random sequences of length k

## Example of Gibbs sampling matrix

![alt text](https://github.com/MichielTaw/QuickMotif/blob/main/images/Screenshot%202024-03-11%20at%2003.49.14.png?raw=true)

## Installation

To start with you can clone the repository  :
```bash
  git clone https://github.com/MichielTaw/QuickMotif.git

```


    
## Import function

```Python
import QuickMotif
from QuickMotif.src.fasta import Fasta
from QuickMotif.src.helper import generate_k_random, random_sequence_generator, update_k_mers
from QuickMotif.src.matrix import Matrix
from QuickMotif.src.sequence import Sequence
}
```


## Tutorial

**For more check the Tutorial.ipynb


## Authors

- [@MichielTawdarous](https://github.com/MichielTaw)


# Hi, I'm Michiel! 👋

I'm a PharmaD student at university of Paris, don't hesitate to contact me for any question about the software at this mail :
michiel.tawdarous@etu.u-paris.fr