import random
import the_metamorphosis_chapter_1_german

EXAMPLE_TEXT = the_metamorphosis_chapter_1_german.TEXT


def generate_string(text):
    word_list = text.split(" ")
    number_of_words = len(word_list)
    mixed_list = []
    word_counter = 1
    for word in word_list:
        list_of_characters = list(word)
        length_of_word = len(list_of_characters)
        list_of_characters.insert(random.randint(0, length_of_word-1), str(word_counter))
        numbered_word = list_of_characters
        numbered_word = "".join(numbered_word)
        mixed_list.insert(random.randint(0, number_of_words-1), numbered_word)
        word_counter += 1
    for word in mixed_list.copy():
        mixed_list.insert(random.randint(0, len(mixed_list)-1), mixed_list.pop(mixed_list.index(word)))
    mixed_sentence = " ".join(mixed_list)

    return mixed_sentence


if __name__ == "__main__":
    print(generate_string(EXAMPLE_TEXT))

