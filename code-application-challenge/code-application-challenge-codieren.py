

def encrypt_file(file_content, password):
    pass


def main():
    output_content = encrypt_file(input_file, input_password)
    output_file = open(output_filename, "w+")
    output_file.write(output_content)
    output_file.close()


if __name__ == "__main__":
    input_file = open(input("Enter the name of the file you want to encrypt: "), "r+")
    input_password = input("Enter a password: ")
    output_filename = input("Enter the name the new file should have: ")
    main()
    input_file.close()
