def criteria(number):
    if "5" in str(number):
        return False


def main(number, counter=1):
    l = 1
    for character in str(number):
        l *= int(character)
    if len(str(l)) == 1:
        return counter
    else:
        return 1 + main(l, counter)

if __name__ == "__main__":
    f = open("multiplicative_persistence.csv","w+")
    f.write("Number,MultiplicativePersistence\n")
    for i in range(277777788888000, 277777788888900):
        if main(i) > 9:
            f.write(str(i)+","+str(main(i))+"\n")
    f.close()

