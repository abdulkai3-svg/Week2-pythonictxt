# Pythonic Text Analyzer

Refactored version of the messy unpythonic_analyzer.py file for my Python class assignment. It reads a text file and prints out the total word count, unique word count, top 5 most used words, and how many words are longer than 3 characters.

## Running it

Need text_analyzer.py and sample.txt in the same folder, then just run:

python3 text_analyzer.py

## What I changed

The original file had everything in one function, bad variable names like the_file and word_item, no docstrings, and it opened/closed the file manually instead of using a with statement. I fixed all of that:

- with statement for opening the file so it always closes properly
- collections.Counter instead of manually looping and building a dictionary to count words
- .most_common(5) to grab the top 5 words instead of sorting it myself
- list comprehension for the long words list instead of a loop with .append()
- broke the one big function into smaller ones (read_words, count_words, get_long_words, print_results, analyze_text)
- renamed everything to snake_case and added docstrings
- f-strings instead of string concatenation
- added if __name__ == "__main__" at the bottom

## Files

- unpythonic_analyzer.py - original starter code
- text_analyzer.py - my refactored version
- sample.txt - test file
