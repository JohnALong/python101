planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
# print(planet_list)

planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")
planet_list.append("Pluto")
print(planet_list)
# Mercury, Venus, Earth and Mars
rocky_planets = planet_list[0:4]
print(rocky_planets)
del planet_list[-1]
print(planet_list)

# spacecraft list
spacecraft = [
    ("Rover", "Mercury"),
    ("Explorer", "Neptune"),
    ("Lost", "Venus"),
    ("Found", "Mars"),
    ("Why", "Uranus"),
    ("Because", "Jupiter"),
    ("The Rings of", "Saturn"),
]
for planet in planet_list:
    for craft in spacecraft:
        if planet == craft[1]:
            print(f"{craft[0]} has visited {planet}")
        