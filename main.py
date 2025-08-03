from stats import get_num_words
from stats import count_characters
from stats import sorted_list
import sys

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
	return file_contents

def main():
	if len(sys.argv) == 1:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	Path = sys.argv[1]
	print(f"Usage: python3 main.py {Path}")
	text = get_book_text(Path)
	num_word = get_num_words(text)
	count = count_characters(text)
	list = sorted_list(count)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {Path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_word} total words")
	print("--------- Character Count -------")
	for i in list:
		print (i["char"] +": " + str(i["num"]))
	print(sys.argv)
main()
