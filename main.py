def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()
    
from stats import num_words, character_count, char_sort




def main():
    text = get_book_text("./books/frankenstein.txt")
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

