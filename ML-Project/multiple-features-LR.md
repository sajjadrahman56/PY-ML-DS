```python
import pandas as pd
import numpy as np
#import matplot

from sklearn import linear_model
```


```python
df = pd.read_csv('car_data.txt')
```


```python
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>speed</th>
      <th>car_age</th>
      <th>experience</th>
      <th>risk</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>200</td>
      <td>15</td>
      <td>5.0</td>
      <td>85</td>
    </tr>
    <tr>
      <th>1</th>
      <td>90</td>
      <td>17</td>
      <td>13.0</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>165</td>
      <td>12</td>
      <td>4.0</td>
      <td>93</td>
    </tr>
    <tr>
      <th>3</th>
      <td>110</td>
      <td>20</td>
      <td>NaN</td>
      <td>60</td>
    </tr>
    <tr>
      <th>4</th>
      <td>140</td>
      <td>5</td>
      <td>3.0</td>
      <td>82</td>
    </tr>
    <tr>
      <th>5</th>
      <td>115</td>
      <td>2</td>
      <td>8.0</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>



check particular column 


```python
df.experience
```




    0     5.0
    1    13.0
    2     4.0
    3     NaN
    4     3.0
    5     8.0
    Name: experience, dtype: float64



I wanna replace null value with some data so I apply another rules that is I can perform mean or median here 


```python
df.experience.mean()
```

    6.6


# store in variable the median value 


```python
exp_fit = df.experience.median()
```


```python
exp_fit
```




    5.0



### I want to fill the with help of df.experience.fillna('pass value')


```python
df.experience = df.experience.fillna(exp_fit)
```

#### see the output 


```python
df.experience
```




    0     5.0
    1    13.0
    2     4.0
    3     5.0
    4     3.0
    5     8.0
    Name: experience, dtype: float64




```python
df

```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>speed</th>
      <th>car_age</th>
      <th>experience</th>
      <th>risk</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>200</td>
      <td>15</td>
      <td>5.0</td>
      <td>85</td>
    </tr>
    <tr>
      <th>1</th>
      <td>90</td>
      <td>17</td>
      <td>13.0</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>165</td>
      <td>12</td>
      <td>4.0</td>
      <td>93</td>
    </tr>
    <tr>
      <th>3</th>
      <td>110</td>
      <td>20</td>
      <td>5.0</td>
      <td>60</td>
    </tr>
    <tr>
      <th>4</th>
      <td>140</td>
      <td>5</td>
      <td>3.0</td>
      <td>82</td>
    </tr>
    <tr>
      <th>5</th>
      <td>115</td>
      <td>2</td>
      <td>8.0</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
reg = linear_model.LinearRegression()
```

### dimentations matter


```python
reg.fit(df[['speed','car_age','experience']],df.risk)
```




    LinearRegression()




```python
reg.predict([[160,10,5]])
```

    array([71.37146872])

## coeficient  find 


```python
reg.coef_
```




    array([ 0.33059217,  1.61053246, -6.20772074])



## Intercept find 


```python
reg.intercept_
```


    33.410000910435905
## Manuale check the output 


```python
(0.33059217*160) + (1.61053246 * 10  ) - ( 5 * 6.20772074 ) + 33.410000910435905
```




    71.3714690104359




``` Thank you This all about multiple features of Linear Regressions 

```
