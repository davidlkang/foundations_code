def is_vowel(character):
    vowel_list = ["a", "e", "i", "o", "u"]
    if character.lower() in vowel_list:
        vowel = True
    else:
        vowel = False
    return vowel


def vowel_score(input_string):
    return # score: integer


def consonant_score(input_string):
    position_of_last_character = input_string.rindex(input_string[-1]) + 1
    for letter in input_string:
        if not is_vowel(letter):
            i = 0
            while i in range(position_of_last_character - input_string.index(letter)):
                #input_string = "".join(input_string.split(letter, 1))
                p = input_string[ input_string.index(letter, i) : input_string.index(letter, i) + i + 1 ]
                print(p)
                i += 1

    return #score : integer


def main(input_string):
    stuarts_points = consonant_score(input_string)
    kevins_points = vowel_score(input_string)
    if stuarts_points > kevins_points:
        return "Stuart" + str(stuarts_points)
    elif kevins_points > stuarts_points:
        return "Kevin" + str(kevins_points)
    else:
        return "Draw"


if __name__ == "__main__":
    print(consonant_score("APPLEPIE"))
