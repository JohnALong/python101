class City: 
    def __init__(self, name, established):
        self.name = name
        self.mayor = ""
        self.established = established
        self.buildings = list()

    def add_building(self, new_building):
        self.buildings.append(new_building)

    def elect_mayor(self, mayor):
        self.mayor = mayor

    def about(self):
        # date = self.date_constructed
        print(f"{self.name}'s mayor is {self.mayor}, and was established in {self.established}.")

    def city_buildings(self):
        print(f"{self.name} is in Southeast Missouri, and has the following buildings:")
        for building in self.buildings:
            building.info()