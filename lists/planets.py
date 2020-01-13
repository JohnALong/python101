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