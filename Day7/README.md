In this assignment the code "ncbi.py" searches for a spesific TERM in the nucleotide database of NCBI.
It gives back a spesific NUMBER of nucleotide sequences in the FASTA format. The the sequences are saved individualy.
The information about the search is also saved - date, the TERM, the NUMBER of searches requested, total number of searches found.
All the above metadata is saved in a csv file.

The user must give both the TERM and the NUMBER.
For example - if you wish to look for cmk and you want 5 results, write the following:
python ncbi.py cmk 5
