#  list or input convert into the int list 



```python
li = '1','4','7'

```


```python
li
```




    ('1', '4', '7')




```python
li = list(map(int,li))
```


```python
li
```




    [1, 4, 7]




```python
sum(li)
```




    12




```python
max(li)
```




    7




```python
min(li)
```




    1




```python
min(li)+max(li)
```




    8



# Now I want to make it Set as it is the Map 


```python
setA = set(map(int,li))
```


```python
setA
```




    {1, 4, 7}




```python
setA.add(9)
```


```python
setA
```




    {1, 4, 7, 9}




```python
setA.add(9)
```


```python
setA
```




    {1, 4, 7, 9}




```python

```

# I want to take multiple variable together how let see 


```python
num1,num2 = [2,3]
```


```python
num1
```




    2




```python
num2
```




    3




```python
nums = input()
```

    5 6
    


```python
a,b = map(int,nums.split(' '))
```


```python
a
```




    5




```python
b
```




    6




```python

```

# Print Method K moja dekne ho 


```python
print(32,56)
```

    32 56
    


```python
print(32,56,sep='^')
```

    32^56
    

# string formating


```python
a = 3 
b = 7
```


```python
print("the two nums are ",a,"and",b)
```

    the two nums are  3 and 7
    

### another way 


```python
print("the two nums are {} and {}".format(a,b))
```

    the two nums are 3 and 7
    

        ### the best way   ' f  strings '


```python
print(f"the two nums are {a} and {b} and last call 100 is = {100}")
```

    the two nums are 3 and 7 and last call 100 is = 100
    


```python

```
