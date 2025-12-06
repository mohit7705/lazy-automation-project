"""
Summarize all text (.txt) files inside a folder INCLUDING subfolders.
Usage:
python summarize_texts.py "C:/path/to/folder"
"""

import sys
from pathlib import Path
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

def summarize_text(text, num_sentences=3):
    sentences = sent_tokenize(text)
    if len(sentences) <= num_sentences:
        return text
    
    words = [w.lower() for w in word_tokenize(text) if w.isalpha()]
    freq = Counter(words)

    scored_sentences = []
    for idx, sentence in enumerate(sentences):
        score = sum(freq[w.lower()] for w in word_tokenize(sentence) if w.lower() in freq)
        scored_sentences.append((score, idx, sentence))

    # Pick top 3 sentences
    top = sorted(scored_sentences, reverse=True)[:num_sentences]
    top_sorted = sorted(top, key=lambda x: x[1])

    return " ".join(s[2] for s in top_sorted)

def summarize_folder(folder):
    p = Path(folder)

    # Scan for .txt files inside all subfolders
    text_files = [f for f in p.rglob("*.txt") if f.is_file()]
    
    if not text_files:
        print("No text files found.")
        return

    print(f"Summarizing {len(text_files)} text files...\n")

    for t in text_files:
        content = t.read_text(encoding="utf-8", errors="ignore")
        summary = summarize_text(content)

        print(f"\n--- Summary of {t.name} ---")
        print(summary[:500], "...\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python summarize_texts.py /path/to/folder")
    else:
        summarize_folder(sys.argv[1])
