import sys
from stats import num_words, character_count, char_sort

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]    
    text = get_book_text(filepath)
    word_count = num_words(text)
    char_counts = character_count(text)
    sorted_chars = char_sort(char_counts)



    print("========== BOOKBOT ==========")
    print("Analyzing book found at books/frankenstein.txt...")
    print("---------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("---------- Character Count ----------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("========== END ==========")

main()




