def criteria(number):
    if "5" in str(number) or "0" in str(number):
        return False
    else:
        return True


def main(input_number, step_counter=1):
    storage = 1
    if criteria(input_number):
        for character in str(input_number):
            storage *= int(character)
            if int(character) == 0:
                break
    if len(str(storage)) == 1:
        return step_counter
    else:
        return 1 + main(storage, step_counter)

if __name__ == "__main__":
    #f = open("multiplicative_persistence.csv","w+")
    #f.close()
    f = open("multiplicative_persistence.csv","a+")
    f.write("Number,MultiplicativePersistence\n")
    for i in range(277777788888899+1):
        if main(i) > 9:
            f.write(str(i)+","+str(main(i))+"\n")
    f.close()

