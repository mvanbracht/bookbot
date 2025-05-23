from stats import get_num_words
from stats import character_count
from stats import list_of_dictionaries
import sys


if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
else:
	path_to_book = sys.argv[1]


def get_book_text(path_to_book):
	with open(path_to_book) as f:
		file_contents = f.read()
	return file_contents


def main():
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path_to_book}...")
	
	print("----------- Word Count ----------")
	text = get_book_text(path_to_book)
	word_count = get_num_words(text)
	print(f"Found {word_count} total words")
	
	print("--------- Character Count -------")
	count = character_count(text)
	sorted_list = list_of_dictionaries(count)
	
	for dictionary in sorted_list:
		print(f"{dictionary['character']}: {dictionary['count']}")

	print("============= END ===============")









main()
