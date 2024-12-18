# Classes and Objects in Python

# Lecture 57

class New:
    name="Ismail"
    occupation = "Data Scientist"
    networth = 100000

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = New()
a.name = "Najeeb"
a.occupation= "Scientist"
a.info()