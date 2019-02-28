def main(string):
    s = string.split(" ")
    l = []
    for word in s:
        l.append(word.capitalize())
    return " ".join(l)

if __name__ == "__main__":
    print(main("david kang"))
