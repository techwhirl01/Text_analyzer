import re 
from collections import Counter

def analyze_text(text):
    lines = text.strip().splitlines()
    words = re.findall(r'\b\w+\b', text.lower())
    sentences = re.split(r'[.!?]+', text.strip())
    characters = len(text)
    vowels = sum(1 for char in text.lower() if char in 'aeiou')
    consonants = sum(1 for char in text.lower() if char.isalpha() and char not in 'aeiou')
    most_common = Counter(words).most_common(1)[0][0] if words else ''
    longest_word = max(words, key=len) if words else ''
    shortest_word = min(words, key=len) if words else ''

    print("\nText Analysis Report")
    print("-"* 30)
    print(f"Total Lines: {len(lines)}")
    print(f"Total Words: {len(words)}")
    print(f"Total Sentences: {len([s for s in sentences if s.strip()])}")
    print(f"Total Characters: {characters}")
    print(f"Total Vowels: {vowels}")
    print(f"Total Consonants: {consonants}")
    print(f"Most Common Word: {most_common}")
    print(f"Longest Word: {longest_word}")
    print(f"Shortest Word: {shortest_word}")    
    print("-"* 30)

if __name__ == "__main__":
    print("Enter text for analysis (press enter twice to finish):\n")
    line=[]
    while True:
        try:
            input_line = input()
            if input_line == "":
                break
            line.append(input_line)
        except EOFError:
            break
    text = "\n".join(line)
    analyze_text(text)
