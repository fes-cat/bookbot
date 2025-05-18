from stats import (
    get_num_words, 
    count_characters, 
    chars_dictionary_to_sorted_list,
)
import sys


def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
        return file_contents

def print_report(book_path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        if not i["char"].isalpha():
            continue
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = count_characters(text)
    sorted_list = chars_dictionary_to_sorted_list(chars_dict)
    print_report(book_path, num_words, sorted_list)

# "sys.argv" takes in arguments when you execute the script.
# you can use it instead of hard coding paths, for example
# sys.argv[1] is the initial argument, which is the script
if len(sys.argv) > 1:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# sadly I had to look up the solution for a few things in stats.py
# even though I had some of it correct, it was very dirty. so i cleaned up.
# i know understood what the mistakes were. it was a good experience.
# but I will improve in the future. i just need to keep going!