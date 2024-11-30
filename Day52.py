# Exercise 6 Solution - Library Management Software in Python

# Lecture 67


class library:
    def __init__(self):
        self.numbooks = 0
        self.books = []

    def addbook(self,Book):
        self.books.append(Book)
        self.numbooks = self.books.length
    
    def showinfo(self):
        print(f"The Library has {self.numbooks} Books")

l1 = library()
l1.addbook("Sumaira Hameed")
l1.showinfo()        

