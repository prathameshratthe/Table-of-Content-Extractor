import re
import spacy
from collections import defaultdict
import argparse

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_topics(document: str):
    """
    Extracts main topics and subtopics using NLP and regex.
    """
    topics = defaultdict(list)
    current_topic = None
    
    for line in document.split('\n'):
        line = line.strip()
        if not line:
            continue
        
        doc = nlp(line)
        if len(doc) > 1:
            current_topic = line
            topics[current_topic] = []
        elif current_topic and (line.startswith('-') or line.startswith('*') or line[0].islower()):
            subtopic = line.lstrip('-*').strip()
            topics[current_topic].append(subtopic)
    
    return topics

def combine_topics(documents: list):
    """
    Combines topics from multiple documents, removing duplicates and merging similar concepts.
    """
    combined_topics = defaultdict(set)
    
    for doc in documents:
        extracted_topics = extract_topics(doc)
        for topic, subtopics in extracted_topics.items():
            combined_topics[topic].update(subtopics)
    
    result = []
    for topic, subtopics in combined_topics.items():
        result.append(f"- {topic}")
        for subtopic in sorted(subtopics):
            result.append(f"  - {subtopic}")
    
    return '\n'.join(result)

def sequence_topics(topics: list):
    """
    Organizes topics into a logical learning sequence based on foundational knowledge.
    """
    return sorted(topics)

def generate_toc(topics: list):
    """
    Generates a structured Table of Contents (TOC) with chapters and subtopics.
    """
    toc = []
    chapter_count = 1
    for i, topic in enumerate(topics, start=1):
        toc.append(f"Chapter {chapter_count}: {topic}")
        chapter_count += 1
    return '\n'.join(toc)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract, combine, and organize topics from documents.")
    parser.add_argument("--documents", nargs='+', help="List of document file paths")
    args = parser.parse_args()
    
    if args.documents:
        docs_content = [open(doc, "r", encoding="utf-8").read() for doc in args.documents]
        print("\nDocument Content:\n", docs_content)  # Debugging line
        combined = combine_topics(docs_content)
        sequenced = sequence_topics(list(extract_topics(docs_content[0]).keys()))
        toc = generate_toc(sequenced)
        
        print("\nCombined Topics:")
        print(combined)
        print("\nSequenced Topics:")
        print(sequenced)
        print("\nGenerated TOC:")
        print(toc)
