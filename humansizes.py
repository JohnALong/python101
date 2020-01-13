SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# Instead of the word `function`, in Python, you use `def`
def approximate_size(size, a_kilobyte_is_1024_bytes=True):

    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            # return '{0:.1f} {1}'.format(size, suffix)
            return f'{size:.1f} {suffix}',

    raise ValueError('number too large')

# if __name__ == '__main__':
#     print(approximate_size(16384, False))
#     print(approximate_size(size=16384, a_kilobyte_is_1024_bytes=True))
#     print(approximate_size(-16384))

# name = "Fred"
# def say_name():
#     global name
#     name = "Bubba"
#     print("internal", name)
#     return name

# say_name()
# print("external", name)

# if/else

# name = "Joe"
# if name == "Steve":
#     print("I feel great")
# elif name == "Joe":
#     print("You got the better instructor")    
# else:
#     print("I have a cold")

# string concatenation
# 
# Still have dynamic typing (but no implicit coercion!)

# print(f"My name is {name}")

# collections/lists

junk = ["Fred", True, [1,2,3], 234]
# print(junk)

junk.append("uh-oh")
junk.insert(3, "oh, I get it")
junk.extend(["Mary", "Joseph", "Bob"])
# print(junk)

# JS
# junk.join(",")
names = ["Mary", "Joseph", "Bob"]
# print(", ".join(names))

# Dictionaries

my_pairs = {
    123: "number",
    "name": "Broomhilda"
}

# print(my_pairs[123])
# print(my_pairs["name"])
my_pairs["last"] = "Jones"
# print(my_pairs)
my_pairs["address"] = {"number": 123,
"street": "Sesame St" }
# print(my_pairs)
street_name = my_pairs["address"]["street"]
# print(street_name)
# print(my_pairs.items())
# print(my_pairs.values())
# print(my_pairs.keys())

# Sets

my_stuff = ["Fred", True, 123, "Jones", "Fred"]
# print(my_stuff)
# print(list(set(my_stuff)))

my_set = {1, 2, 3}
my_set.add("Feed me")
# print(my_set)

# tuple ***can't be changed***
my_tup = (1, 2, 3, 3, "hello")
# print(my_tup)
# print(my_tup[0])
my_tup = ("WTF", "I'm hungry")
# print(my_tup)

# loops
# my_tup = (1, 2, 3, 3, "hello")
# my_set = {1, 2, 3}
# junk = ["Fred", True, [1,2,3], 234]

# for foo in junk:
#     print(f"Why do I still have {foo} in this drawer")

# for foo in my_set:
#     print(f"Why do I still have {foo} in this drawer")  

# for foo in my_tup:
#     print(f"Why do I still have {foo} in this drawer") 

# for foo in my_pairs.values():
#     print(f"Why do I still have {foo} in this drawer")

my_list_tobe_sliced = [1, 2, 4, "hello", "monkey"]
my_subset = my_list_tobe_sliced[1:3]
print (my_subset)
















  