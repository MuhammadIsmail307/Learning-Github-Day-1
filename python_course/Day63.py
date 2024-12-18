# Single Inheritance in Python

# Lecture 78

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Sound made by animal")


class dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species="dog")
        self.breed = breed

    def make_sound(self):
        print("Bark !")


c = dog("Tommy", "German")
c.make_sound()

a = Animal("Tommy", "German")
a.make_sound()



# ===========================================================


