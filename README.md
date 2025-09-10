Text Similarity with MinHash and LSH

This project detects similar paragraphs in a text file using shingling, MinHash, and Locality Sensitive Hashing (LSH). It is useful for identifying duplicate content, plagiarism, or near-duplicate documents.

Features

Splits text into paragraphs

Creates k-word shingles for each paragraph

Converts shingles to numeric representation and bit vectors

Generates MinHash signatures

Applies LSH to efficiently find candidate similar paragraphs

Computes Jaccard similarity between candidate pairs



Requirements

Python 3.8+

Packages: numpy, pandas, hashlib, re

Install packages using pip:

pip install numpy pandas



Usage

Place your text file in the project folder.

Update the file_path variable in the script to point to your file.

Run the script:

python text_similarity.py


The script outputs the top similar paragraph pairs along with their similarity scores.


Notes

Shingle size (k) and number of hash permutations can be adjusted for precision vs. performance trade-offs.

The output lists paragraph indices and Jaccard similarity in descending order.
