def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()
    
from stats import num_words

from stats import character_count



def main():
    text = get_book_text("./books/frankenstein.txt")
    print(f"{num_words(text)} words found in the document")
    print(character_count(text))
main()

