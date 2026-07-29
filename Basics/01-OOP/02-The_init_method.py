# we consider __init__ methood is a constructor and have the same proprites 
# it will be called once you create an object so basiclly you have 2 types of init methods 
# 1- default which you didn't create as followed -> with pass keyword as we illustrated earlier 
class Example1:
    def __init__(self):
        pass

# 2- you already define it 
class Example2:
    def __init__(self,par1,par2):
        self.par1 = par1
        self.par2 = par2
# **self** keyword = **this** in java

## so baicly using __init__ method makes declaring objects with inital value 

# instead of 

class Example3:
    pass
e1 = Example3()
e1.name = "Laufey"

# we use 

class Example4:
    def __init__(self,name):
        self.name = name
e2 = Example4("Lauefey")


# challenge
# Create a class called Dog
# Add an __init__ method with parameters name and age, and store them as properties using self
# Add a method called bark that prints the dog's name followed by " says Woof!"
# Create an object d1 of the Dog class with name "Buddy" and age 3
# Call the bark method on d1

class Dog:
    def __init__(self,name,age):
        self.name = name;
        self.age = age

    def bark(self):
        return f"{self.name} is laughing wewe"

dog = Dog("buddy",3)
print(dog.bark)