# OOP

Class : Name group of Properties and Functions 

    class Name :
                age
                name
                getIncome();


 Abstraction : Encapsulation : Polymor : Inheritance 
 
 Absraction providing Functions() , its hide the things
 
 *_*_ Abstraction is design level and perform by functions 
 
 
 *Encapsulation : Bundile of data in a single of file /data 
 
 all data is bundle means 
 *_implementation level 
 ->  <- 

 pythone no overloading here overiding is code 

 


```python
# class
class Person:
    age = 0
    name = 'zummun'
```


```python
kunal = Person()
# whenever you create an object , a constructor is called 
#
#
# here kunal is in the Stack and where Heap is object or reference variable 
```


```python
kunal.age

```




    0




```python
kunal.name
```




    'zummun'




```python
class A:
    pass
```


```python
 
```


```python
kunal.salary = 300
```


```python
kunal.salary
```




    300




```python
sasa = Person()
```


```python
sasa.salary
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_8136\2310140751.py in <module>
    ----> 1 sasa.salary
    

    AttributeError: 'Person' object has no attribute 'salary'



```python
class Test:
    def fun():
        print('I am a method')
```


```python
demoTest = Test()
```


```python
demoTest.fun()
```


```python
class Test:
    def fun(something):
        print('I am a method')
```


```python
demoTest1 = Test()
demoTest1.fun()
```

Lests watch the difference between abobe the methods 


```python

```


```python

```


```python
class Human:
    age=45
    def fun(self):
        #print(self)
        print(self.age)
```


```python
sajjad = Human()
```


```python
sajjad.age = 99
```


```python
sajjad.fun()
```


```python
Human.fun(sajjad)
```


```python
 class Human:
        def __init__(self,name,age):
            self.age = age
            self.name = name
```


```python
 sakib = Human("sakib hasan",67)
```


```python
sakib.age
```


```python
class Car:
    #overriding
    def __init__(self,price,model,year):
        self.price = price 
        self.model = model
        self.year = year
```


```python
Toyota = Car(45000,'At78',2023)
```


```python
Toyota.price,Toyota.model , Toyota.year
```

# that is not a good prectices to 


```python
Car.country = "BD"
```


```python
Toyota.country
```


```python
Car
```

# poly morphisom


```python
 def fun():
    print("null")
def fun(a):
    print(" i am ",a)

```


```python
fun('a')
```

### if i call fun() it gives error why error find the answer by self 

# more about ooop 

# more info 
class variable is known as 
      class variable / static variable 
      static variable is common for all objects of that class 
      
object variable is known as 
                    instance variable 
 


```python
class Human:
    #static variable : that not depend on objects 
    
    population = 0
    
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        Human.population += 1
```


```python
Human.population
```


```python
A_man = Human("sa75",34)
```


```python
Human.population
```


```python
B_man = Human("sa7576",34)
```


```python
Human.population
```

## let see the below example of the static variables 


```python
A_man.population
```


```python
B_man.population
```

# importance matter look 


```python
#incerese the A_man.population +=1 let see the effect of the other class 
```


```python
A_man.population+=1
```


```python
A_man.population
```


```python
#after increaseing the value of A_man then see the outputs 
A_man.population , B_man.population , Human.population
```

# no value cahnge above in the cell  by objcet level 


```python
# if I assing new object will it affect on the or increase the
# value of A_man.population already it is bigger than others 
# what do you think mr / mrs 
```


```python
C_man =    Human("sajjad",34)
```


```python
C_man.population
```


```python
A_man.population , B_man.population , C_man.population,  Human.population
```


```python
#it does not effect as A_man itself hase A_man.population variable has but not others 
```


```python
#what if i changed increment one 
```


```python
Human.population +=1
```


```python
A_man.population , B_man.population , C_man.population,  Human.population
```


```python

```

# static methods 


```python
class Human1:
    #static variable : that not depend on objects 
    
    population = 0
    
    
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        Human.population += 1
    @staticmethod  
    def met():
        print(Human.population)
        
```


```python
D_man =    Human("sajjad",34)
```


```python
D_man.met()
```


```python
E_man = Human("sajjad",34)
```


```python
E_man.met()
```

# make a method static WE used   @staticmethod   as a result no need to pass an self arguments   

# class methods 


```python
class Human:  
    population = 0
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        Human.population += 1
    @staticmethod  
    def met():
        print(Human.population)
    def getName(self):
        print(self.name)
    
    @classmethod
    def atomBomb(cls):
        cls.population=0
```


```python
sajjad = Human("sajjad",45)
sakib = Human("Sakib",56)
```


```python
Human.fun()
```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```

# For Loop


```python

```


```python

```


```python
pets = ['cats', 'dogs', 'rabbits', 'hamsters']

for myPets in pets:
    print (myPets)
```

    cats
    dogs
    rabbits
    hamsters
    


```python

```


```python
for index, myPets in enumerate(pets):
    print (index, myPets)
```

    0 cats
    1 dogs
    2 rabbits
    3 hamsters
    


```python
for i in range(9):
    print(' ',i,' ',i+2)
```

      0   2
      1   3
      2   4
      3   5
      4   6
      5   7
      6   8
      7   9
      8   10
    


```python
range?
```


```python
 j = 0
for i in range(5):
    j = j + 2
    print ('i = ', i, ' j = ', j)
    if j == 6:
        continue
    print('i am over by 6')
```

    i =  0  j =  2
    i am over by 6
    i =  1  j =  4
    i am over by 6
    i =  2  j =  6
    i =  3  j =  8
    i am over by 6
    i =  4  j =  10
    i am over by 6
    


```python

```
