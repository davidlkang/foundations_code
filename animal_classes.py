'''Create a file called animals.py, and add to this file two classes, of two of your favorite types of animals (cats and dogs, fish and zebras).
Each class should have some variables which are always defined same (e.g. name or color),
and some which are unique to that animal (length of whiskers or distance between stripes).
The same for methods: 2 for each animal, at least one unique and one the same. Create a few instance of each class.
How much are you repeating yourself? What can you do to repeat yourself less?'''

class Carp:

    SPECIES = "Carp"
    FAMILY = "Cyprinidae"

    def __init__(self, name="no-name", age="not less then zero", color="ninja"):
        self.age = age
        self.name = name
        self.color = color


    def introduction(self):
        print("Hi! My name is {}. I am {} years old and a {} {}.".format(self.name, self.age, self.color, self.SPECIES))


    def eating(self):
        print("When a {} is hungry, it eats stuff.".format(self.FAMILY))


Bob = Carp("Bob", 5, "green")
Bob.introduction()

Chris = Carp("Chris")
Chris.introduction()
