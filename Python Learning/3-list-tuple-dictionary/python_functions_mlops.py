# -*- coding: utf-8 -*-
"""python-functions-mlops.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E6CqWTVbQcxAw_e_HH2ldaTl7EJtRIEq
"""

def say_hello():
  print("sajjad")

say_hello()

# difference btween ()
say_hello

def say_hello(name):
  print(f'Hello {name}')

say_hello('jhon')

# defulat name passed
def say_hello(name = "sajjad Defult name"):
  print(f'Hello {name}')

say_hello()

say_hello('akib')

# tuple with functions
stock_prices = [('apple',450),('banana',120),('mango',456)]

for item in stock_prices:
  print(item) # both i can see
  print(item[0]) # only see the ticker
  print(item[1]) # only price is show

for ticker,item   in stock_prices:
  print(ticker)

works_hours = [('aba',400),('sam',780),('rakib',450)]

# touple return => we can say unpack
works_hours = [('aba',400),('sam',780),('rakib',450)]
def employee_check(works_hours):
  current_max = 0
  employee_of_month = ' '

  for employee,hours in works_hours:
    if hours > current_max:
      current_max = hours
      employee_of_month = employee
    else:
      pass

  return (employee_of_month,current_max)

employee_check(works_hours)

name,hours = employee_check(works_hours)

### interection functions game
#
from random import shuffle

example = [1,2,3,4,5,6,7]

def shuffle_example(mylist):
  shuffle(mylist)
  return mylist

result = shuffle_example(example)

result

mylist = [' ','o',' ']

shuffle_example(mylist)

def player_guess():
  guess = ' '

  while guess not in ['0','1','2']:
    guess = input("Pick a number : 0 , 1 or 2")
  return int(guess)

def myfunc(a,b):
  return a+b

myfunc(30,20)

# myfunc(40,30,40) # takes 2 postitiona arguments but 3 were given

def myfunc1(*args):
  print(args)
  sum = 0
  for i in args:
    sum+= i
  return sum

myfunc1(30,405,50,60)

myfunc1(30)

def myfunc2(**kwargs):
  print(kwargs)
  if 'fruit' in kwargs:
      print(f"my favourite furite is {kwargs['fruit']}")
  else:
    print(" i did not find it")

myfunc2(fruit='apple')

def myfunc3(*args,**kwargs):
  print(args)
  print(kwargs)
  print(f"I would like to {args[0]} {kwargs['food']}")

myfunc3(10,20,30,40,fruit='orange',food='eggs')

