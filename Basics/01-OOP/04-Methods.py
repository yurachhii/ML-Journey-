# as we saw before methods in python in classes must contain **this** keyword a parameter 

# you can access the information in a certain instance using **this** keyword

class Calc:
    def __init__(this,a,b):
        this.a = a
        this.b = b
    def get_info(this):
        return f"the 1st number is {this.a} and the 2nd one {this.b}"

# the method __str()__ is equivalent to toString() in java

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

    def whatever_u_like(hobbies):
        pass


# you can also delete a method using **del** keyword 

person = People("loyza",40)
del person.whatever_u_like

# Challenge 
# Create a class called Rectangle
# Add an __init__ method with width and height, and store them as properties
# Add a method called area that returns the width multiplied by the height
# Create an object r1 with width 5 and height 3
# Print the area of r1



class Rectangle:
    def __init__(this,width,height):
        this.width = width
        this.height = height
    def area(this):
        return this.width * this.height

r1 = Rectangle(5,3)

print(r1.area())