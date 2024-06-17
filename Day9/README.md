# Analysis goal:
Analyze sequences from a Fasta or GeneBank file.
The code can find the longest repeated sub-sequence, and also calculate the GC content within it.


## GC content - bio info:
GC content means calculating the guanine-cytosine content in a sequence.
In biology, high gc content usually indicates a higher level of stability for the DNA molecule.

[More info can be found here](https://en.wikipedia.org/wiki/GC-content)

## Running the code:
To run the code, for a file named actin.fasta:
```
python analyze.py actin.fasta --duplicate --gc_content
```
The output will be:
Longest repeated subsequence: TGTTGTTG (Length: 8)
GC content: 52.92%

## Requirements
- Python 3.x
- Biopython

## Installation:
Install the required packages using pip:

```
pip install -r requirements.txt
```
