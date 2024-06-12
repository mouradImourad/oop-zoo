class Animal:

    def __init__(self, name, species):
        self._name = name
        self._species = species

    def speak(self):

        return "animal sound"
    

class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    def give_birth(self):
        print(f"{self.name} has given birth!")


class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan


class Reptile(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def bask_in_sun(self):
        print(f"{self.reptile} is basking in the sun")


class Primate(Mammal):

    def climb_tree():
        print(f"{primate} climbing trees")


class Murspial(Mammal):

    def carry_baby(self):
        print(f"{marsupial} is carrying its baby")
