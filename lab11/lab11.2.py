class Liquid:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"Это {self.name}"

class Water(Liquid):
    def __init__(self, temperature):
        super().__init__("вода")
        self.temperature = temperature

    def describe(self):
        return f"{super().describe()}, температура: {self.temperature}°"

class Oil(Liquid):
    def __init__(self, viscosity):
        super().__init__("нефть")
        self.viscosity = viscosity

    def describe(self):
        return f"{super().describe()}, вязкость: {self.viscosity}"

water = Water(25)
oil = Oil("высокая")

print(water.describe())
print(oil.describe())

