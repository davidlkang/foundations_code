

def string_contains(string, method_name):
    for letter in string:
        if getattr(letter, method_name)():
            return True
    return False


if __name__ == '__main__':
    string = "-.,a-.,"
    print(string_contains(string, "isalnum"))
    print(string_contains(string, "isalpha"))
    print(string_contains(string, "isdigit"))
    print(string_contains(string, "islower"))
    print(string_contains(string, "isupper"))
