# instance vs Class varaibles

# python lecture 66


class employee:
    def __init__(self, name):
        self.name = name
    
    def showdetails(self):
        print(f"The Name of the employee is {self.name}")


emp1 = employee('Ismail')
employee.showdetails(emp1)


# =================================================


class employee:
    CompanyName = "Microsoft"
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.05
    def showdetails(self):
        print(f"The Name of the employee is {self.name} and the raise amount is {self.raise_amount} and he works in {self.CompanyName}")

employee.CompanyName = "Googli"
emp1 = employee('Ismail')
employee.showdetails(emp1)

