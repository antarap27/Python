import time


class EmployeeA:

    def __init__(self):
        self.name = input("Enter the Name\n")
        self.age = input("Enter the Age\n")

    def calling_A(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")


E1 = EmployeeA()
E1.calling_A()

time.sleep(1)


class EmployeeB:

    def __init__(self):
        self.walk = input("Enter if B can walk\n")

    def calling_B(self):

        if self.walk.lower() == "yes":
            print("Cool")
        else:
            print("Sad")


E2 = EmployeeB()
E2.calling_B()
