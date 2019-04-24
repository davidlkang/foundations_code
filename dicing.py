import random


def die_throw(number_of_dice, is_attacker=False):
    dice_results = []
    if is_attacker:
        for i in range(3):
            dice_results.append(random.randint(1, 6))
    else:
        for i in range(2):
            dice_results.append(random.randint(1, 6))
    return dice_results


def main(units_player_one, units_player_two):
    while (units_player_one > 0) and (units_player_two > 0):
        result_player_one = die_throw(units_player_one, True).sort()
        result_player_two = die_throw(units_player_two, False).sort()
        if result_player_one[0] > result_player_two[0]:
            units_player_two -= 1
        else:
            units_player_one -= 1
        if result_player_one[1] > result_player_two[1]:
            units_player_two -= 1
        else:
            units_player_one -= 1
    return units_player_one, units_player_two,


if __name__ == "__main__":
    main(12, 23)
