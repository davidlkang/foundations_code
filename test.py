

def disemvowel(word):
    for element in word:
        if element == "a":
            a = word.replace(element, "")
    return a


def first_4(iterable):
    return iterable[:4:]


def first_and_last_4(iterable):
    return iterable[:4:] + iterable[-5::]


def word_count(string):
    string = string.lower()
    list = string.split(" ")
    dictionary = {}

    for element in list:

        if element in dictionary:
            dictionary[element] = dictionary[element] + 1
        else:
            dictionary.update({element: 1})

    return dictionary


def num_teachers(teachers_courses):
    counter = 0
    for element in teachers_courses:
        counter += 1
    return counter


def num_courses(teachers_courses):
    counter = 0
    for key, value in teachers_courses.items():
        counter += len(value)
    return counter


def courses(teachers_courses):
    courses = []
    for key, value in teachers_courses.items():
        courses.extend(value)
    return courses


def most_courses(teachers_courses):
    num_of_most_courses = 0
    for key, value in teachers_courses.items():
        if len(value) > num_of_most_courses:
            num_of_most_courses = len(value)
            teacher_with_most_courses = key
    return teacher_with_most_courses


def stats(teachers_courses):
    list_of_teacher_stats = []
    for key, value in teachers_courses.items():
        new_list = [key, len(value)]
        list_of_teacher_stats.append(new_list)
    return list_of_teacher_stats


def combo(first_iterable, second_iterable):
    touple_list = []
    for element in first_iterable:
        touple_list.append((element, second_iterable[first_iterable[element]], ))
    return touple_list


#print(combo([1, 2, 3], "abc"))
#print(stats({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']}))
#print(num_courses({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']}))
#print(disemvowel("sxectaagzbhuns"))
#print(word_count("I do not like it Sam I Am"))
#print(first_and_last_4([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))



