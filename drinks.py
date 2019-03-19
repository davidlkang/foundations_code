favorite_drinks = {'Katja':'Whiskey Sour', 'Behnaz':'Gin Tonic', 'Leon':'Moscow Mule', 'Viktoria':'Gin Basil', 'Winston':'Ginger', 'Tilli':'Whiskey Coke', 'David':'Beer', 'Elias':'Water'}

drinks = {"Cocktails": ['Gin Tonic', 'Gin Basil', 'Moscow Mule', 'Whiskey Sour', 'Whiskey Coke'], "Wines": ['Red Wine', 'White Wine'], "Liquors": ['Whiskey', 'Gin', 'Vokda'], "Nonalcoholic": ['tea', 'Water', 'orange juice', 'Ginger'], "Beers":['Beer']}

number_of_drinks_per_hour_per_type = {'Cocktails':1, 'Beers':3,'Wines':2,'Liquors':2,'Nonalcoholic':3}


def drinks_needed(drink_category, drink_preferences, drinks_per_hour, number_of_hours):
    total_drinks = {}
    for key, value in drink_preferences.items():
        for x, y in drink_category.items():
            if value in y:
                if x in total_drinks.keys():
                    total_drinks[x] += drinks_per_hour[x]*number_of_hours
                else:
                    total_drinks.update({x: drinks_per_hour[x]*number_of_hours})
    return total_drinks


print(drinks_needed(drinks, favorite_drinks, number_of_drinks_per_hour_per_type, 6))
