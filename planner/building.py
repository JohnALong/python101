import datetime

class Building:
    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def purchase(self, owner):
        self.owner = owner

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def info(self):
        # date = self.date_constructed
        print(f"{self.address} was purchased by {self.owner} on {self.date_constructed.strftime('%x')} and has {self.stories} stories.")

    