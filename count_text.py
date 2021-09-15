def input_sentence(text):
    return input(text).strip()

def clean_data(string):
    char = list(string)
    for i in range(len(char)):
        if char[i].isalnum() == False and char[i] != " ":
            char[i] = " "
    new_string = "".join(char)
    return new_string

def remove_duplicate(array):
    new_array =  list(set(array))
    new_array.sort()
    return new_array

def count_words(word, array):
    return array.count(word)

if __name__ == '__main__':
    sentence = input_sentence("Input sentence or paragraph here: \n")
    list_word = clean_data(sentence).lower().split()
    new_list_word = remove_duplicate(list_word)
    result = {}
    for i in new_list_word:
        dict = {i:count_words(i, list_word)}
        result.update(dict)
    for key, val in result.items():
        print(f"{key:7}: {val:4}")