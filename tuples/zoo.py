# tuple ***can't be changed***
zoo = ("cat", "dog", "hamster", "deer", "cow", "horse", "bird", "kangaroo", "lemur", "lion")
# find index of item in tuple
print(zoo.index("lemur"))

# find if item is in tuple with value in
animal_to_find = "dog"
if animal_to_find in zoo:
    # Print that the animal was found
    print("was found")

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo
print(first_animal)
print(second_animal)
print(third_animal) 
print(fourth_animal)
print(fifth_animal)
print(sixth_animal)
print(seventh_animal)
print(eighth_animal)
print(ninth_animal)
print(tenth_animal)

#convert tuple to list
zoo_list = list(zoo)
#add items to list
zoo_list.extend(["goldfish", "swamp rat", "alligator"])
print(zoo_list)

#convert back to tuple
new_zoo = tuple(zoo_list)
print(new_zoo)





