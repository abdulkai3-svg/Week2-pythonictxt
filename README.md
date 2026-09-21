# Pythonic Text Analyzer

## What this is
This is my refactor of the messy starter file (unpythonic_analyzer.py) for the Pythonic Text Analyzer assignment. The program reads a text file and gives you the total word count, unique word count, top 5 most common words, and how many words are longer than 3 characters. Same output as the original, just way cleaner code.

## How to run it
Keep text_analyzer.py and sample.txt in the same folder, then run:

python3 text_analyzer.py

That's it, it'll print the stats to the terminal.

## What I actually fixed

Original code had everything crammed into one function with names like the_file and word_item, no docstrings, and it opened/closed the file manually which isn't safe. Here's what I did instead:

- Used a with statement to open the file so it closes automatically no matter what happens
- Swapped the manual counting loop for collections.Counter, way less code and it does the counting for me
- Used .most_common(5) instead of sorting the dictionary by hand
- Built the long words list with a list comprehension instead of a for loop with .append()
- Split the one giant function into separate ones: read_words, count_words, get_long_words, print_results, and analyze_text
- Fixed all the variable/function names to snake_case and added docstrings
- Switched every print to an f-string
- Added the if __name__ == "__main__": block at the bottom

## Files
- unpythonic_analyzer.py — the original starter code
- text_analyzer.py — my refactored version
- sample.txt — text file I used to test it
