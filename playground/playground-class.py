#!/usr/bin/env python3
class Dog():
   def __init__(self,name,age):
      self.name = name
      self.age = age

   def greetings(self):
       print("My Dog's Name is {} and He is {} yrs old".format(self.name,self.age))


if __name__ == '__main__':
    my_dog = Dog("Chipy",2)
    my_dog.greetings()
    print("Dog Name is => ",my_dog.name)
