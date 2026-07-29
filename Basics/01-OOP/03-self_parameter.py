# as we said before self parameter gives the same meaning of this keyword in java 
# the intersting thing here that the **self** parameter can called anything not only **self**
# so here in my own pactice as i used to learn OOP using java i will call it **this** 

class example1:
    def __init__(this , name , age):
        this.name = name
        this.age = age
    def prining(this):
        print(f"introduce {this.name} whose age is {this.age}")
e1= example1("Elio" , 20)
e1.prining()

