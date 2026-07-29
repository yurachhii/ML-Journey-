# as we know to inherit a class -> there should be 2 classes (parent , child)
# Python fully supports multiple inheritance unlike Java


#To create a class that inherits the functionality from another class ->  send the parent class as a **parameter** when creating the child class

class People:
    def __init__(this,first_name,last_name):
        this.first_name = first_name
        this.last_name = last_name
    def get_info(this):
        return f"the current person is {this.first_name} {this.last_name}"

class Person(People):  # -> here u have inherited all the proprtiesfrom the parent class
    def __init__(this , fname, lname , gyear):
        # here we did override on the __init__() parent class 
        #if u wanna keep inheritance then u call it by **Parent** class or using super keyword 
        super.__init__(this,fname,lname)
        this.gyear = gyear


# Challenge 

# Inside the editor, complete the following steps:
# Create a parent class Animal with an __init__ that takes name
# Add a method speak that prints the name
# Create a child class Dog that inherits from Animal
# Create an object d1 = Dog("Rex")
# Call d1.speak()

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name)

class Dog(Animal):
    pass

d1 = Dog("Rex")

d1.speak()