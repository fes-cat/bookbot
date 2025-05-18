def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] +=1
        else: 
            chars[lowered] = 1
    return chars
    
def sort_on(dict):
    return dict["num"]

def chars_dictionary_to_sorted_list(num_chars_dict):
    sorted_list = []
    for d in num_chars_dict:
        sorted_list.append({"char": d, "num": num_chars_dict[d]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list