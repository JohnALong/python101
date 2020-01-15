class Pizza:
    def __init__(self):
        self.size = ""
        self.crust = ""
        self.toppings = list()

    def set_size(self, size):
        self.size = size

    def set_crust(self, style):
        self.crust = style

    def descrbe_pizza(self):
        toppings = " and "
        print(f"I would like a {self.size}, {self.crust} pizza with {toppings.join(self.toppings)}")

    def add_topping(self, topping):
        self.toppings.append(topping)