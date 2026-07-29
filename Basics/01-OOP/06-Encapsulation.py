# Encapsulation is protecting the data to be accessed outside the class

# **Private** properties using __ prefix

class Person:
    def __init__(this, name, age):
        this.name = name
        this.__age = age # Private property

# but how do reach  it? -> getter and setters  method is the solution 
    def get_age(this):
        return this.__age

    def set_age(this,new_age):
        this.__age = new_age

# **Protected** properties using _ prefix

# a single underscore _ is just a convention
# it tells others  that the property is intended for internal use, but Python doesn't enforce this restriction

class Account:
    def __init__(this,owner,balance):
        this.owner = owner
        this._balance = balance

    def display(this):
        return f"Owner : {this.owner} with balance : {this._balance}" # -> this is an internal use

class SavingAccount(Account):

    def ChangingBalance(this):
        this._balance += this._balance*0.5 # -> one the internal uses   

# Name mangling is how Python implements private properties and methods

# when u use __ -> pythong added in prefix _ClassName__attribute but no recommended to use it

class Person:
    def __init__(self, age):  
        self.__age = age

p = Person(20)

print(p._Person__age)