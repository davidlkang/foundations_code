def main(list_of_stock, list_of_wanted_categories):
    library_of_books = {}
    for string in list_of_stock:
        new_list = string.split(" ")
        category = new_list[0][0]
        library_of_books.update({string: {"id": new_list[0], "category": category, "stock": int(new_list[1])}})
    counter = 0
    new_inventory = []
    while counter <= (len(list_of_wanted_categories)-1):
        stock_counter = 0
        for key, value in library_of_books.items():
            if value["category"] == list_of_wanted_categories[counter]:
                stock_counter += value["stock"]
        new_inventory.append((list_of_wanted_categories[counter], str(stock_counter),))
        counter += 1
    return new_inventory


if __name__ == "__main__":
    l = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}
    m = ["A", "B", "C", "W"]
    print(main(l, m))
