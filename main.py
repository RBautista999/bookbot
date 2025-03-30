import sys
from stats import get_word_count, get_character_occurance, sort_dictionary


def get_book_text(book: str) -> str:
    with open(book) as f:
        book_contents = f.read()
        return book_contents


def main(filepath: str):
    text = get_book_text(book=filepath)
    word_count = get_word_count(book=text)
    character_count = get_character_occurance(book=text)
    sorted_count = sort_dictionary(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in sorted_count:
        print(f"{character['char']}: {character['count']}")
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    main(filepath)
