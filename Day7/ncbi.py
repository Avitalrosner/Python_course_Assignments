import sys
import os
import csv
import datetime
from Bio import Entrez, SeqIO
Entrez.email = "avitalrosner@gmail.com" 

def download_data(search_term, num_items):
    handle = Entrez.esearch(db="nucleotide", term=search_term, retmax=num_items)
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"], record["Count"]

def fetch_and_save_data(id_list, search_term):
    filenames = []
    for uid in id_list:
        handle = Entrez.efetch(db="nucleotide", id=uid, rettype="fasta", retmode="text")
        filename = f"{search_term}_{uid}.fasta"
        with open(filename, "w") as f:
            f.write(handle.read())
        handle.close()
        filenames.append(filename)
    return filenames


def save_metadata(date, search_term, num_requested, total_found):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    metadata_file = os.path.join(script_dir, "metadata.csv")
    with open(metadata_file, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if os.stat(metadata_file).st_size == 0:
            writer.writerow(["date", "term", "max", "total"])
        writer.writerow([date, search_term, num_requested, total_found])

        

def main():
    if len(sys.argv) != 3:
        print("Usage: python ncbi.py TERM NUMBER")
        sys.exit(1)

    search_term = sys.argv[1]
    num_items = int(sys.argv[2])

    if num_items <= 0:
        print("Please enter a valid number of items.")
        sys.exit(1)

    try:
        id_list, total_found = download_data(search_term, num_items)

        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("date,term,max,total")
        print(f"{current_date},{search_term},{num_items},{total_found}")
        save_metadata(current_date, search_term, num_items, total_found)

        filenames = fetch_and_save_data(id_list, search_term)

        print("Files saved:")
        for filename in filenames:
            print(filename)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

