# a class defines what an object is as we know ya3ny 
# to create a class use the key word **class**

class newClass:
    x = "What a class?"

#create an object of a class -> c = newClass()
def Creating_an_object():
    p = newClass()
    print(p.x) # output: What a class? 

def deleting_an_object():
    p = newClass()
    print(p.x) # output: What a class? 
    del p
    # print(p.x) # this will raise an error because the object has been deleted

def pass_statement():
    pass # this is a null statement, it does nothing but can be used as a placeholder

## challenge 1
# Create a class called Person
# Add an __init__ method that takes name and age as parameters
# Add a method called greet that prints "Hello, my name is " followed by the name
# Create an object p1 of the class with name "John" and age 36
# Call the greet method on p1

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"hey , i called {self.name}") 
    
p1 = Person("john",15)
p1.greet()
