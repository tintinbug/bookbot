def get_num_words(text):
	return len(text.split())

def count_characters(text):
	count = {}
	text = text.lower()
	text = text.split()
	for i in text:
		for char in i:
			if char in count:
				count[str(char)] += 1
			else:
				count[str(char)] = 1
	return count
def sort_on(characters):
	return characters["num"]

def sorted_list(dict):
	sorted_list = []
	for i in dict:
		temp_dict = {}
		temp_dict["char"] = i
		temp_dict["num"] = dict[i]
		sorted_list.append(temp_dict)
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list
