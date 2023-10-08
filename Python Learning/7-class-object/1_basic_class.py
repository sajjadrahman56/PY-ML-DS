class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(f'Name is {p1.name} and Age is {p1.age}')