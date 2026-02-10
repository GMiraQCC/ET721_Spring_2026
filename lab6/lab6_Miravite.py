"""
Gabriel Miravite
Lab 6: Classes, Objects & Methods
"""

# import matplotlib.pyplot as plt

print("============= Example 1: Classes =============")
# Classes are like blueprints we can use to create different instances/objects
# Data attributes (or properties) are values that represent ___
# Methods are functions of an object

class Circle(object):
    # Constructor that auto-runs at instantiation
    def __init__(self, radius, color):
        self.r = radius
        self.c = color

    def add_radius(self, plusradius):
        self.r += plusradius
        return self.r

class Rectangle(object):
    def __init__(self, height, width, color):
        self.h = height
        self.w = width
        self.c = color
    
    def area(self):
        return self.h * self.w
    
    def perimeter(self):
        return (2*self.w) + (2*self.h)
    
    # See lines 64-66
    """
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0), self.w, self.h, fc=self.c))
        plt.axis("scaled")
        plt.show()
    """

# Create instances/objects
circ1 = Circle(5,"yellow")
circ2 = Circle(2,"red")
rect1 = Rectangle(2,3,"green")
rect2 = Rectangle(5,4,"blue")

# Access data in instances/objects
print(f"Color of circle 2 = {circ2.c}")
print(f"Area of rectangle 1 = {rect1.w * rect1.h}")
print(f"Area of rectangle 2 = {rect2.w * rect2.h}")

# Modify data in instances/objects
circ2.c = "orange"
print(f"Color of circle 2 after modification = {circ2.c}")

# Call a method in class Circle to modify a property
print(f"radius of circle 2 = {circ2.r}")
circ2.add_radius(6)
print(f"radius of circle 2 after method add_radius = {circ2.r}")

# Call methods in class Rectangle to calculate, return & display values
print(f"The area of rectangle 1 = {rect1.area()}")
print(f"The perimeter of rectangle 2 = {rect2.perimeter()}")

# Call a method to draw the rectangle
# rect2.drawRectangle()
# We're commenting this out for now just cuz we couldn't properly import the library that we needed around line 6 within the codespace, so this wasn't working at all



print("\nEnd of Examples, Start of EXERCISES")



print("\n============= Exercise: Bank Accounts =============")

class BankAccount(object):
    # Constructor that auto-runs at instantiation
    def __init__(self, account_number, account_holder, balance=250.50):
        self.n = account_number
        self.h = account_holder
        self.b = balance
    
    def deposit(self, amount):
        self.b += amount
    
    def withdraw(self, amount):
        if(self.b > amount):
            self.b -= amount
        else:
            print("Insufficient balance. Withdrawal transaction cannot be completed.")
    
    def balance(self):
        print(f"Final Balance ${self.b}")

# Create an instance of the BankAccount class
useraccount = BankAccount(123456789,"Gabriel")

# Demonstrate deposits & withdrawals
useraccount.withdraw(700)
useraccount.deposit(1000)
useraccount.withdraw(500)
useraccount.balance()