from building import Building

eight_hundred_eighth = Building("800 8th St", 12)
print(eight_hundred_eighth.address)

building_one = Building("351 S Silver Springs Rd", 4)
building_two = Building("301 Plus Park Blvd", 5)
building_three = Building("1638 County Rd 642", 2)
building_four = Building("9731 Turner Rd", 3)
building_five = Building("222 HereThere", 947)

building_one.purchase("Bruce Lee")
building_two.purchase("Joe Shepard")
building_three.purchase("John Long")
building_four.purchase("Brenda Long")
building_five.purchase("Mr. Wong")

building_one.construct()
building_two.construct()
building_three.construct()
building_four.construct()
building_five.construct()

print(building_one.owner)
building_one.info()
building_two.info()
building_three.info()
building_four.info()
building_five.info() 

