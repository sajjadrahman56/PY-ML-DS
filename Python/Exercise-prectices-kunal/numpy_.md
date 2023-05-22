```python
# the difference between List and numpy

from time import process_time
```


```python
process_time?
```


```python
py_list = [i for i in range(1000000)]


```


```python
start_time = process_time()
```


```python
py_list = [i+5 for i in py_list]
```


```python
end_time = process_time()
```


```python
print(end_time - start_time)
```

    0.125
    


```python

```


```python
# in the numpy the differences
```


```python
import numpy as np

```


```python
np_array = np.array([i for i in range(1000000)])

```


```python
start_time =   process_time()
```


```python
np_array += 5
```


```python
end_time = process_time()
```


```python
print(end_time - start_time)
```

    0.0
    


```python

```


```python
# now see the difference 
```


```python
list1 = [1,3,4,5,6,7]
print(list1)
type(list1)
```

    [1, 3, 4, 5, 6, 7]
    




    list




```python

```


```python
np_array= np.array([1,3,4,5,6,7])
print(np_array)
type(np_array)
```

    [1 3 4 5 6 7]
    




    numpy.ndarray




```python
 
```

# Creatig 1 dim array


```python
a= np.array([1,3,4,5,6,7])
```


```python
a.shape
```




    (6,)




```python
b = np.array([(1,3,4,7),(33,44,55,66)])
```


```python
b.shape
```




    (2, 4)




```python
print(b)
```

    [[ 1  3  4  7]
     [33 44 55 66]]
    


```python

```


```python
addition_operation = lambda a, b: a + b
```


```python


```


```python
np.full()

```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_4704\2372936444.py in <module>
    ----> 1 np.full()
    

    TypeError: full() missing 2 required positional arguments: 'shape' and 'fill_value'



```python
np.full((3,4),22)
```




    array([[22, 22, 22, 22],
           [22, 22, 22, 22],
           [22, 22, 22, 22]])




```python
np.arange(10, 30, 0.5)
```




    array([10. , 10.5, 11. , 11.5, 12. , 12.5, 13. , 13.5, 14. , 14.5, 15. ,
           15.5, 16. , 16.5, 17. , 17.5, 18. , 18.5, 19. , 19.5, 20. , 20.5,
           21. , 21.5, 22. , 22.5, 23. , 23.5, 24. , 24.5, 25. , 25.5, 26. ,
           26.5, 27. , 27.5, 28. , 28.5, 29. , 29.5])




```python
np.linspace(11,20,40)
```




    array([11.        , 11.23076923, 11.46153846, 11.69230769, 11.92307692,
           12.15384615, 12.38461538, 12.61538462, 12.84615385, 13.07692308,
           13.30769231, 13.53846154, 13.76923077, 14.        , 14.23076923,
           14.46153846, 14.69230769, 14.92307692, 15.15384615, 15.38461538,
           15.61538462, 15.84615385, 16.07692308, 16.30769231, 16.53846154,
           16.76923077, 17.        , 17.23076923, 17.46153846, 17.69230769,
           17.92307692, 18.15384615, 18.38461538, 18.61538462, 18.84615385,
           19.07692308, 19.30769231, 19.53846154, 19.76923077, 20.        ])




```python

```


```python
a = np.array( [20, 30, 40, 50] )
a

```




    array([20, 30, 40, 50])




```python
b = np.arange(4)
b
```




    array([0, 1, 2, 3])




```python
a+b
```




    array([20, 31, 42, 53])




```python
a-b
```




    array([20, 29, 38, 47])




```python
a*b

```




    array([  0,  30,  80, 150])




```python
a/b
```

    C:\Users\user\AppData\Local\Temp\ipykernel_4704\1348051284.py:1: RuntimeWarning: divide by zero encountered in true_divide
      a/b
    




    array([        inf, 30.        , 20.        , 16.66666667])




```python
np.dot(a,b)
```




    260




```python
b**2
```




    array([0, 1, 4, 9], dtype=int32)




```python
np.minimum(a,b)
```




    array([0, 1, 2, 3])




```python
np.sum(a)
```




    140




```python

```

# changing the shape


```python
import numpy as np
```


```python
a = np.floor(10*np.random.random((3,4)))
```


```python
a
```




    array([[1., 1., 7., 1.],
           [3., 5., 1., 5.],
           [1., 8., 8., 8.]])




```python
a.ravel() # return 1 dimensional array
```




    array([1., 1., 7., 1., 3., 5., 1., 5., 1., 8., 8., 8.])




```python
a.shape
```




    (3, 4)




```python
a.reshape(2,6)
```




    array([[1., 1., 7., 1., 3., 5.],
           [1., 5., 1., 8., 8., 8.]])




```python
a.reshape(3,4)
```




    array([[1., 1., 7., 1.],
           [3., 5., 1., 5.],
           [1., 8., 8., 8.]])




```python

```

# Stacking and Spliting of Arrays
stack several arrays together or split an array to several arrays 


```python
arr = np.array([[33,44],[45,55]])
```


```python
arr.shape,type(arr)
```




    ((2, 2), numpy.ndarray)




```python
arr2 = np.array([(1,2),(9,56)])
```


```python
arr2
```




    array([[ 1,  2],
           [ 9, 56]])




```python
arr2.shape,type(arr2)
```




    ((2, 2), numpy.ndarray)




```python
v_stack_array = np.vstack((arr,arr2))
```


```python
v_stack_array,type(v_stack_array)
```




    (array([[33, 44],
            [45, 55],
            [ 1,  2],
            [ 9, 56]]),
     numpy.ndarray)




```python
h_stack_array = np.hstack((arr,arr2))
```


```python
h_stack_array,type(h_stack_array)
```




    (array([[33, 44,  1,  2],
            [45, 55,  9, 56]]),
     numpy.ndarray)




```python

```

# Notice the difference
there are two major difference , now I follow the one more example


```python
ar1 = np.array([[100,200],[400,600]])
```


```python
ar2 = np.array([[1000,2000,5000],[4000,6000,7000],[1000,2000,8000]])
```


```python
 
```


```python
h_stack_array = np.hstack((ar1,ar2))
# we got an error , yes the size is matter 
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_4704\1106314638.py in <module>
    ----> 1 h_stack_array = np.hstack((ar1,ar2))
          2 # we got an error , yes the size is matter
    

    <__array_function__ internals> in hstack(*args, **kwargs)
    

    E:\anaconda\lib\site-packages\numpy\core\shape_base.py in hstack(tup)
        343         return _nx.concatenate(arrs, 0)
        344     else:
    --> 345         return _nx.concatenate(arrs, 1)
        346 
        347 
    

    <__array_function__ internals> in concatenate(*args, **kwargs)
    

    ValueError: all the input array dimensions for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 2 and the array at index 1 has size 3



```python
h_stack_array,type(h_stack_array)
```




    (array([[33, 44,  1,  2],
            [45, 55,  9, 56]]),
     numpy.ndarray)




```python

```


```python
v_stack_array = np.vstack((ar1,ar2))
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_4704\3312247306.py in <module>
    ----> 1 v_stack_array = np.vstack((ar1,ar2))
    

    <__array_function__ internals> in vstack(*args, **kwargs)
    

    E:\anaconda\lib\site-packages\numpy\core\shape_base.py in vstack(tup)
        280     if not isinstance(arrs, list):
        281         arrs = [arrs]
    --> 282     return _nx.concatenate(arrs, 0)
        283 
        284 
    

    <__array_function__ internals> in concatenate(*args, **kwargs)
    

    ValueError: all the input array dimensions for the concatenation axis must match exactly, but along dimension 1, the array at index 0 has size 2 and the array at index 1 has size 3



```python

```
