
def main(mat_size_y, mat_size_x):
    counter = 1
    while counter < mat_size_y:
        middle_chars = ".|."*counter
        print(middle_chars.center(mat_size_x, "-"))
        counter += 2
    print("WELCOME".center(mat_size_x, "-"))
    counter -= 2
    while counter > 0:
        middle_chars = ".|."*counter
        print(middle_chars.center(mat_size_x, "-"))
        counter -= 2


if __name__ == "__main__":
    #x = input().split(" ")
    #y = int(x[0])
    #z = y * 3
    y = 51
    z = 153
    main(y, z)
