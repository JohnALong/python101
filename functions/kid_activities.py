# stuff = ["name", "age", "parking", "job"]

# cap_stuff = []

# #loop example
# for foo in stuff:
#     cap_stuff.append(foo.capitalize())

# # map example
# cap_stuff = list(map(lambda foo: foo.capitalize(), stuff))

# #comprehension example
# cap_stuff = [ foo.capitalize() for foo in stuff ]
# print(cap_stuff)

# Function and variable names are snake case instead of camel case
# def create_person(first_name, last_name, age, occupation):
#     return {
#         "first_name": first_name,
#         "last_name": last_name,
#         "age": age,
#         "occupation": occupation,
#     }

# melissa = create_person("Melissa", "Bell", 25, "Software Developer")
# print(melissa)
# function for run
# running_kids = ["Pam", "Sam", "Andrea", "Will"]
# def run(name):
#     print(f"{child} ran desperately towards NSS")

# for child in running_kids:
#     run(child)

# # function for swinging
# swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
# def swing(name):
#     print(f"{child} swung over the canyon as if they had no fear!")

# for child in running_kids:
#     swing(child)

# #function for sliding
# sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
# def slide(name):
#     print(f"{name} slid into capstone by the skin of their teeth")

# for name in sliding_kids:
#     slide(name)

# #function for hiding
# hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]
# def hide(name):
#     print(f"{name} hid their deficiencies by studying longer than everyone else")

# for name in hiding_kids:
#     hide(name)

#Chicken Monkey
# generate a list of numbers 1..100
numbers_1_to_100 = range(1, 101)
def num_list(num):
    print(num)

for num in numbers_1_to_100:
    if num % 5 == 0 and num % 7 == 0:
        print("ChickenMonkey")
    elif num % 5 == 0:
        print("Chicken")
    elif num % 7 == 0:
        print("Monkey")
    else:
        print(num)




