class Kitchen_appliances:
    Model = ""
    Name = ""
    Country = ""

    def __init__(self, model, name, country):
        self.Model = model
        self.Name = name
        self.Country = country

    def print(self):
        print(f"{self.Name} , {self.Model}, {self.Country}")


class Plate(Kitchen_appliances):

    method_work = "Heating"

    def print(self):
        print(f"{self.method_work}")


class Fridg(Kitchen_appliances):

    method_work = "cool"

    def print(self):
        print(f"{self.method_work}")

class Freezer(Kitchen_appliances):

    method_work = "freeze"

    def print(self):
        print(f"{self.method_work}")

class Electric_Plate(Plate):

    heating_method = "Electric"

    def print(self):
        print(f"{self.Name}, {self.Model}, {self.method_work} = {self.heating_method}")

class Gas_Plate(Plate):

    heating_method = "Gas"

    def print(self):
        print(f"{self.Name}, {self.Model}, {self.method_work} = {self.heating_method}")