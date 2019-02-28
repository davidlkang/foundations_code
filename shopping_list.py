def show_help():
    print("""
Type 'HELP' for this help.
Type 'CLEAR' to clear your list.
Type 'DEL X' where 'X' is the number of the element you want to remove.
Type 'SHOW' to display your list.
Type 'DONE' to stop adding items.
""")


def add_to_list(user_input):
    shopping_list.append(user_input.lower())
    print("Great! Your item was added. There are", len(shopping_list), "items in your list.")


def clear_list():
    shopping_list.clear()
    print("Success. Your list was cleared.")


def show_list():
    print("You have the following items in your shopping list: ")
    for element in shopping_list:
        print(element)


def delete_item_from_list(index):
    index = int(index) - 1
    print("You succesfully removed {}.".format(shopping_list.pop(index)))


shopping_list = []
show_help()

while True:

    user_input = input("> ")

    if user_input == "HELP":
        show_help()
    elif user_input == "CLEAR":
        clear_list()
    elif "DEL " in user_input:
        delete_item_from_list(user_input[4])
    elif user_input == "SHOW":
        show_list()
    elif user_input == "DONE":
        show_list()
        break
    elif user_input.lower() in shopping_list:
        print("You already have {} in your shopping list. Do you still want to add it? ".format(user_input))
        if input("(Y/N) ").lower() == "y":
            add_to_list(user_input)
    else:
        add_to_list(user_input)
