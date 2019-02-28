import string_sorting

text = string_sorting.order(string_sorting.mixed_text)


def main(text):
    word_list = text.split(" ")
    denumerised_list = []
    for word in word_list:
        denumerised_word = ""
        for character in word:
            if not character.isnumeric():
                denumerised_word += character
        denumerised_list.append(denumerised_word)
    denumerised_text = " ".join(denumerised_list)
    return denumerised_text


if __name__ == "__main__":
    print(main(text))
