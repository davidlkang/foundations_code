player_names = []
would_like_to_continue = True

while would_like_to_continue == True:
    if input("Would you like to add a player to the list?\n(y/n) ").lower() == "y":
        player_names.append(input("Please enter the name. "))
    else:
        print(player_names)
        would_like_to_continue = False

print("There are {} players on the team.".format(len(player_names)))

for element in player_names:
    print("Player {}: {}".format((int(player_names.index(element)) + 1), element))

print("Your goalkeeper is", player_names[(int(input("Select a goalkeeper.\n(1-{}) ".format(len(player_names)))) - 1)])
