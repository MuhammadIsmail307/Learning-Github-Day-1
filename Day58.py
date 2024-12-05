# Magic/Dunder Methods in Python


# Lecture 73


class employee():
    def __init__(self, name ):
        self.name = name
    
    def __len__(self):
        i=0
        for c in self.name:
            i = i + 1
        
        return i
    

e = employee("Muhammad Ismail")
print(e.name)
print(len(e))


# Learn to use these methods 


# __str__
# __repr__
# __len__
# __call__
