# Multi-level Inheritance in Python


# Lecture 80

class A():
    pass

class B(A):
    pass

class C(B):
    pass



            #  A ---> B ----> C



# Hybrid and Hierarchical Inheritance in Python



# Lecture 81


class A():                                              #     A                   
    pass                                                #    / \
                                                        #   D1  D2   
class B():                                              #  / \ / \
    pass

class D1(A):
    pass

class D1(B):

class D2(A):
    pass

class D3(B):

