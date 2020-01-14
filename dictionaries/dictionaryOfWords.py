"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = {}

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

word_definitions["cattywampus"] = "askew, awry, kitty-corner"
word_definitions["bumfuzzle"] = "confuse; perplex; fluster"
word_definitions["Gardyloo"] = "used in Edinburgh as a warning cry when it was customary to throw slops from the windows into the streets"
word_definitions["Taradiddle"] = "1: a fib 2 : pretentious nonsense"
word_definitions["Snickersnee"] = "to engage in cut-and-thrust fighting with knives"

# print single definition
# print(word_definitions["Snickersnee"])
# print(word_definitions["Gardyloo"])

# print all definitions in word_definitions
for (key, value) in word_definitions.items():
    print(f'The definition of {key} is {value}')
