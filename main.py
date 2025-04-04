from stats import get_num_words
from stats import character_count
from stats import list_of_dictionaries

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents


def main():
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	
	print("----------- Word Count ----------")
	text = get_book_text("./books/frankenstein.txt")
	word_count = get_num_words(text)
	print(f"Found {word_count} total words")
	
	print("--------- Character Count -------")
	count = character_count(text)
	sorted_list = list_of_dictionaries(count)
	
	for dictionary in sorted_list:
		print(f"{dictionary['character']}: {dictionary['count']}")

	print("============= END ===============")









main()
