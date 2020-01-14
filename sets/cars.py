showroom = set()
showroom = {"prius", "f-150", "Jeep", "Ol Blue", "f-150"}

#print length of a set with len()
print(len(showroom))

#print set to show no duplicates present
print(showroom)

#add items with update (square brackets are needed regardless of one or many being added)
showroom.update(["Silverado", "Element"])
print(showroom)

#remove item with discard
showroom.discard("Element")
print(showroom)

#junkyard
junkyard = set()
junkyard = {"Chevelle", "f-150", "Gremlin", "E-Class", "f-150", "Omega", "Silverado"}

# intersection() method to show duplicates in 2 sets
duplicates = showroom.intersection(junkyard)
print(f"these are duplicates: {duplicates}")

new_showroom = showroom.union(junkyard)
new_showroom.discard("E-Class")
print(f"this is my new showroom: {new_showroom}")






