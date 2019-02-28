import generate_mixed_number_string


TEXT = generate_mixed_number_string.EXAMPLE_TEXT
mixed_text = generate_mixed_number_string.generate_string(TEXT)


def sort_by_int(word, y = 0):
    while y != len(word):
        character = word[y]
        if character.isnumeric():
            new_index_number = character
            try:
                new_index_number += sort_by_int(word, y + 1)
            except NameError:
                pass
            break
        else:
            y += 1
    return new_index_number


def order(sentence):
    counter = 0
    sorted_sentence_list = []
    sentence = sentence.split(" ")
    length_of_sentence = len(sentence)
    while counter < length_of_sentence:
        sorted_sentence_list.append(0)
        counter += 1
    for word in sentence:
        sorted_sentence_list[int(sort_by_int(word)) - 1] = word
    for element in sorted_sentence_list.copy():
        if element == 0:
            sorted_sentence_list.remove(0)
    sorted_sentence = " ".join(sorted_sentence_list)
    return sorted_sentence


if __name__ == "__main__":
    pass
    #print(order(mixed_text))
