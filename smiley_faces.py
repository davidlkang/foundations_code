VALID_SMILEY_NOSE = ['-', '~']
VALID_SMILEY_EYES = [':', ';']
VALID_SMILEY_MOUTH = [')', 'D']


def valid_eyes(smiley):
    if smiley[0] in VALID_SMILEY_EYES:
        valid = True
    else:
        valid = False
    return valid


def valid_nose(smiley):
    if smiley[1] in VALID_SMILEY_NOSE or smiley[1] in VALID_SMILEY_MOUTH:
        valid = True
    else:
        valid = False
    return valid


def valid_mouth(smiley):
    if len(smiley) == 2:
        valid = True
    elif smiley[2] in VALID_SMILEY_MOUTH:
        valid = True
    else:
        valid = False
    return valid


def main(input_list):
    smiley_count = 0
    for string in input_list:
        if valid_eyes(string) and valid_nose(string) and valid_mouth(string):
            smiley_count += 1
        else:
            pass
    return smiley_count


if __name__ == "__main__":
    print(main([':)', ';(', ';}', ':-D']))
