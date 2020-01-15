my_family = {
    "sister": {
        "name": "Brenda",
        "age": 52
    },
    "mother": {
        "name": "Deanna",
        "age": 75
    },
    "father": {
        "name": "Jim",
        "age": 75
    },
    "spouse": {
        "name": "Jeanne",
        "age": 44
    }
}
for member, info in my_family.items():
    print(f"{info['name']} is my {member} and is {info['age']} years old")


print(my_family["sister"].get("name"))


family_strings = []
family_strings = [ f"My {key}'s name is {value['name']}" for key, value in my_family.items() ]
print(family_strings)

 