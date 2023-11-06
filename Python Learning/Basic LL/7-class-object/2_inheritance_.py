class Person:
  def __init__(self, fname, lname,age):
    self.firstname = fname
    self.lastname = lname
    self.age = age

  def printname(self):
    print(self.firstname, self.lastname,self.age)

class Student(Person):
  def __init__(self, fname, lname, age ,year):
    super().__init__(fname, lname,age)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    print(f" also the age of {self.firstname} and age is = {self.age}")

x = Student("Mike", "Olsen", 23, 2019)
x.welcome()