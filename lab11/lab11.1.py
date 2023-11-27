class Archer:
    total_archers = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.__arrows = 15
        Archer.total_archers += 1

    def shoot_arrow(self):
        if self.__arrows > 0:
            self.__arrows -= 1
            print(f"{self.name} выпускает стрелу. Осталось {self.__arrows} стрел.")
        else:
            print("Стрелы закончились.")

    def __str__(self):
        return f"{self.name} lvl {self.level}"

    def __add__(self, other):
        if isinstance(other, Archer):
            return Archer(f"{self.name} + {other.name}", self.level + other.level)

    def get_total_archers():
        return Archer.total_archers


archer1 = Archer("Леголас", 7)
archer2 = Archer("Риверс", 3)

print("Всего лучников:", Archer.get_total_archers())

archer1.shoot_arrow()
archer2.shoot_arrow()

print(str(archer1))
print(str(archer2))

print("МЕГАЛУЧНИК:", archer1 + archer2)
