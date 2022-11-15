class Animal:

    Name = "-"
    Color = "-"
    Breed = "-"
    Classification = "-"

    def __init__(self):
        self.Name = input("Введите название животного:")
        self.Color = input("Введите цвет животного:")
        self.Breed = input("Введите породу животного:")
        self.Classification = input("Введите класификацию животного:")

    def PrintInfo(self):
        print("название:", self.Name,
              "цвет:", self.Color,
              "порода:", self.Breed,
              "класификация:", self.Classification)

    def ReturnDictInfo(self):
        return {"название": self.Name,
              "цвет": self.Color,
              "порода": self.Breed,
              "класификация": self.Classification}

    def ReturnStrInfo(self):
        return f"название: {self.Name}, " \
               f"цвет: {self.Color}, " \
               f"порода:{self.Breed}, " \
               f"класификация: {self.Classification}."