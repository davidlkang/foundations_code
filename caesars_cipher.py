def main(message, key):
    list_of_all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_message = []
    for letter in message:
        letter = letter.lower()
        if letter in list_of_all_letters:
            index_of_letter = list_of_all_letters.index(letter)
            index_of_letter += key
            index_of_letters = index_of_letter % 26
            new_message.append(list_of_all_letters[index_of_letter])
        elif letter == ' ':
            new_message.append(' ')
    return ''.join(new_message)
if __name__ == "__main__":
    main('hello david', 5)
