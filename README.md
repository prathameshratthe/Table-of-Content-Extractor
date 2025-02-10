Topics Extraction & TOC Generator

Overview

This Python script extracts topics and subtopics from structured text files, combines similar topics from multiple documents, organizes them into a logical sequence, and generates a structured Table of Contents (TOC).

Features

Extracts main topics and subtopics using NLP (SpaCy)

Merges and removes duplicate topics from multiple documents

Sequences topics based on logical learning progression

Generates a structured TOC with chapters and subtopics

Requirements

Python 3.8+

Required Python Libraries:

spacy

argparse

collections

Installation

Clone the repository or download the script.

Install dependencies:

pip install spacy
python -m spacy download en_core_web_sm

Usage

Running the Script

To extract topics from one or multiple text files, run:

python topic_extraction.py --documents topics1.txt topics2.txt

Input Format (Example: topics1.txt)

Machine Learning
- Supervised Learning
- Unsupervised Learning

Deep Learning
- Neural Networks
- CNNs
- RNNs

Expected Output

Combined Topics:
- Machine Learning
  - Supervised Learning
  - Unsupervised Learning
- Deep Learning
  - Neural Networks
  - CNNs
  - RNNs

Sequenced Topics:
['Deep Learning', 'Machine Learning']

Generated TOC:
Chapter 1: Deep Learning
Chapter 2: Machine Learning

Debugging

If the script runs but produces no output:

Ensure the input .txt files contain valid structured text.

Run with a single document to test:

python topic_extraction.py --documents topics1.txt

Add debug prints in topic_extraction.py:

print(extract_topics(docs_content[0]))

File Structure

/Proj2/
  ├── topic_extraction.py  # Main script
  ├── topics1.txt          # Sample input file
  ├── topics2.txt          # Another input file
  ├── README.md            # Documentation

Notes

The script currently supports .txt files only.

Make sure to use structured text with clear headings and subtopics for best results.

License

This project is open-source and available for use under the MIT License.
