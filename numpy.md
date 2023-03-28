---
jupyter:
Numpy:
---

 
``` python
import numpy as np

a = np.array([1, 2, 3])

a
```

    array([1, 2, 3])
 
``` python
np.arange(4)
#array([0, 1, 2, 3])
```

 
# ami amn akta array create korte chai jeta automatic starting to ending o nibe step size er moton kore
: 
``` python
np.arange(2,20,2.5)
```

 
    array([ 2. ,  4.5,  7. ,  9.5, 12. , 14.5, 17. , 19.5])
 

 
``` python
## Linspace is also similar 
```
 

 
np.linspace(0, 20, 2)
 

 
``` python
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
```
 

 
\### Concat 2 or more add
 
 
 
``` python
np.concatenate((a,b))
```

 
    array([1, 2, 3, 4, 5, 6, 7, 8])
 

 
``` python
np.concatenate((b,a))
```

 
    array([5, 6, 7, 8, 1, 2, 3, 4])
 
 
``` python
```
 
