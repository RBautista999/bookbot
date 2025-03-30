def get_word_count(book: str) -> int:
    word_split = book.split()
    num_words = word_split.__len__()
    return num_words


def get_character_occurance(book: str) -> dict:
    char_split: list[str] = list(book.lower())
    occurances: dict = {}
    for i in char_split:
        if i not in occurances.keys():
            occurances.update({f"{i}": 1})
        elif i in occurances.keys():
            occurances[i] += 1
    return occurances


def sort_on(dict_to_sort: dict):
    return dict_to_sort["count"]

def sort_dictionary(dict_of_char: dict) -> list[dict]:
    char_list = []
    for k,v in dict_of_char.items():
        if k.isalpha():
            char_list.append(dict(char = k, count = v))
    # print(f"Unsorted: {char_list}")
    sorted_list = sorted(char_list, reverse=True, key=sort_on)
    # print(f"Sorted: {sorted_list}")
    return sorted_list
    # sorted_list: list[dict] = sorted(unsorted_list, reverse=True, key=sort_on)
    # return sorted_list

