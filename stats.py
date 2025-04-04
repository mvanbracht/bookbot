def get_num_words(text):   	
	words = text.split()
	num_words = len(words)
	return num_words

def character_count(text):
	character_dict = {}
	for c in text:
		lower_letter = c.lower()
		if lower_letter in character_dict:
			character_dict[lower_letter] += 1
		else:
			character_dict[lower_letter] = 1
	return character_dict


def list_of_dictionaries(dictionary):
	list_of_dicts = []
	for character in dictionary:
		count = dictionary[character]
		if character.isalpha() == True:
			list_of_dicts.append({"character" : character, "count" : count})
	
	def sort_on(dict_item):
		return dict_item["count"]
		
	list_of_dicts.sort(reverse=True, key=sort_on)
	return list_of_dicts

