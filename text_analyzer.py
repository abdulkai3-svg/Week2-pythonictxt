from collections import Counter

LONG_WORD_LENGTH = 3
TOP_N_WORDS = 5


def read_words(file_name):
    """Open the file, grab the text, and split it into a list of lowercase words."""
    with open(file_name, "r") as file:
        text = file.read()
    return text.lower().split()


def count_words(words):
    """Use Counter to count how many times each word shows up."""
    return Counter(words)


def get_long_words(words):
    """Return only the words that are longer than 3 characters."""
    return [word for word in words if len(word) > LONG_WORD_LENGTH]


def print_results(words, word_counts, long_words):
    """Print out all the stats."""
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(word_counts)}")
    print("Top 5 most common words:")

    for word, count in word_counts.most_common(TOP_N_WORDS):
        print(f"'{word}': {count}")

    print(f"Words longer than {LONG_WORD_LENGTH} characters: {len(long_words)}")


def analyze_text(file_name):
    """Run the whole analysis on a text file."""
    words = read_words(file_name)
    word_counts = count_words(words)
    long_words = get_long_words(words)
    print_results(words, word_counts, long_words)


if __name__ == "__main__":
    analyze_text("sample.txt")