def main(string):
    number_list = string.split(" ")
    is_even_counter = 0
    for number in number_list:
        if int(number) % 2 == 0:
            is_even_counter += 1
        else:
            is_even_counter -= 1
    #Since the is_even_counter is incremented with an even element and decremented with an odd, it shows the overwhelming tendency.
    #The counter is positve for an even tendency and negative for an odd tendency.
    for number in number_list:
        number_is_odd = int(number) % 2
        if ((is_even_counter > 0) and number_is_odd) or ((is_even_counter < 0) and not number_is_odd):
            return number_list.index(number) + 1


if __name__ == "__main__":
    print(main(input(">")))
