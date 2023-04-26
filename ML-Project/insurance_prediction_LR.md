---
jupyter:
  colab:
    collapsed_sections:
    - LebjXyxL6VHM
  kernelspec:
    display_name: Python 3
    name: python3
  language_info:
    name: python
  nbformat: 4
  nbformat_minor: 0
---

::: {.cell .code execution_count="112" id="Y4_3liys6Rl9"}
``` python
```
:::

::: {.cell .markdown id="LebjXyxL6VHM"}
# Import Library for this projects
:::

::: {.cell .code execution_count="113" id="UrEo_2jR4lvQ"}
``` python
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split as tts 
from sklearn.linear_model import LinearRegression 
from sklearn import metrics 
```
:::

::: {.cell .code execution_count="113" id="yVKC-Kel5Qoa"}
``` python
```
:::

::: {.cell .code execution_count="114" id="Vj0eA9Hm6oci"}
``` python
# DATA LOAD 
insurance_dataset = pd.read_csv('/content/drive/MyDrive/insurance.csv')
```
:::

::: {.cell .code execution_count="115" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":206}" id="RUeHy3zP6v6a" outputId="e0875f12-0620-4c4e-8bf3-0d311459a020"}
``` python
# read 5 data from dataset 
insurance_dataset.head(5)
 
```

::: {.output .execute_result execution_count="115"}
```{=html}

  <div id="df-4c48409d-fc0a-4538-831c-d7d23ffcf736">
    <div class="colab-df-container">
      <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>sex</th>
      <th>bmi</th>
      <th>children</th>
      <th>smoker</th>
      <th>region</th>
      <th>charges</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>19</td>
      <td>female</td>
      <td>27.900</td>
      <td>0</td>
      <td>yes</td>
      <td>southwest</td>
      <td>16884.92400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>18</td>
      <td>male</td>
      <td>33.770</td>
      <td>1</td>
      <td>no</td>
      <td>southeast</td>
      <td>1725.55230</td>
    </tr>
    <tr>
      <th>2</th>
      <td>28</td>
      <td>male</td>
      <td>33.000</td>
      <td>3</td>
      <td>no</td>
      <td>southeast</td>
      <td>4449.46200</td>
    </tr>
    <tr>
      <th>3</th>
      <td>33</td>
      <td>male</td>
      <td>22.705</td>
      <td>0</td>
      <td>no</td>
      <td>northwest</td>
      <td>21984.47061</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32</td>
      <td>male</td>
      <td>28.880</td>
      <td>0</td>
      <td>no</td>
      <td>northwest</td>
      <td>3866.85520</td>
    </tr>
  </tbody>
</table>
</div>
      <button class="colab-df-convert" onclick="convertToInteractive('df-4c48409d-fc0a-4538-831c-d7d23ffcf736')"
              title="Convert this dataframe to an interactive table."
              style="display:none;">
        
  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M0 0h24v24H0V0z" fill="none"/>
    <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
  </svg>
      </button>
      
  <style>
    .colab-df-container {
      display:flex;
      flex-wrap:wrap;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

      <script>
        const buttonEl =
          document.querySelector('#df-4c48409d-fc0a-4538-831c-d7d23ffcf736 button.colab-df-convert');
        buttonEl.style.display =
          google.colab.kernel.accessAllowed ? 'block' : 'none';

        async function convertToInteractive(key) {
          const element = document.querySelector('#df-4c48409d-fc0a-4538-831c-d7d23ffcf736');
          const dataTable =
            await google.colab.kernel.invokeFunction('convertToInteractive',
                                                     [key], {});
          if (!dataTable) return;

          const docLinkHtml = 'Like what you see? Visit the ' +
            '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
            + ' to learn more about interactive tables.';
          element.innerHTML = '';
          dataTable['output_type'] = 'display_data';
          await google.colab.output.renderOutput(dataTable, element);
          const docLink = document.createElement('div');
          docLink.innerHTML = docLinkHtml;
          element.appendChild(docLink);
        }
      </script>
    </div>
  </div>
  
```
:::
:::

::: {.cell .code execution_count="116" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="b_l2BVBa6x8x" outputId="cae24cd5-2aae-499e-c965-f6b99ded2654"}
``` python
#  i want to know the number rows of columns and 
insurance_dataset.shape
```

::: {.output .execute_result execution_count="116"}
    (1338, 7)
:::
:::

::: {.cell .code execution_count="117" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="xe25i2oy8GX5" outputId="721e154b-b985-4d5d-86de-977f823afa68"}
``` python
# SOME info about data set 
insurance_dataset.info
```

::: {.output .execute_result execution_count="117"}
    <bound method DataFrame.info of       age     sex     bmi  children smoker     region      charges
    0      19  female  27.900         0    yes  southwest  16884.92400
    1      18    male  33.770         1     no  southeast   1725.55230
    2      28    male  33.000         3     no  southeast   4449.46200
    3      33    male  22.705         0     no  northwest  21984.47061
    4      32    male  28.880         0     no  northwest   3866.85520
    ...   ...     ...     ...       ...    ...        ...          ...
    1333   50    male  30.970         3     no  northwest  10600.54830
    1334   18  female  31.920         0     no  northeast   2205.98080
    1335   18  female  36.850         0     no  southeast   1629.83350
    1336   21  female  25.800         0     no  southwest   2007.94500
    1337   61  female  29.070         0    yes  northwest  29141.36030

    [1338 rows x 7 columns]>
:::
:::

::: {.cell .code execution_count="118" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="KwKKnvJc-sWj" outputId="5096490f-362f-4161-dbae-03c68132c4bb"}
``` python
insurance_dataset.info()
```

::: {.output .stream .stdout}
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1338 entries, 0 to 1337
    Data columns (total 7 columns):
     #   Column    Non-Null Count  Dtype  
    ---  ------    --------------  -----  
     0   age       1338 non-null   int64  
     1   sex       1338 non-null   object 
     2   bmi       1338 non-null   float64
     3   children  1338 non-null   int64  
     4   smoker    1338 non-null   object 
     5   region    1338 non-null   object 
     6   charges   1338 non-null   float64
    dtypes: float64(2), int64(2), object(3)
    memory usage: 73.3+ KB
:::
:::

::: {.cell .markdown id="32NFO3dD_x90"}
## above the code we can that non-null means numerical value where in the objcet ✈ {#above-the-code-we-can-that-non-null-means-numerical-value-where-in-the-objcet-}

object means class type , fixed no of of output no particluar values ok.
categories ❤

-   sex ⛔
-   smoker ⛔
-   region ⛔
:::

::: {.cell .code execution_count="119" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":424}" id="_SACORBP_TdR" outputId="58ba7219-267f-4a23-9eb3-7d503f790773"}
``` python
# here i am select is null value or not 

insurance_dataset.isnull()
```

::: {.output .execute_result execution_count="119"}
```{=html}

  <div id="df-6a1df143-8d56-4003-9492-80d513fcd1d1">
    <div class="colab-df-container">
      <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>sex</th>
      <th>bmi</th>
      <th>children</th>
      <th>smoker</th>
      <th>region</th>
      <th>charges</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1333</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1334</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1335</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1336</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1337</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>1338 rows × 7 columns</p>
</div>
      <button class="colab-df-convert" onclick="convertToInteractive('df-6a1df143-8d56-4003-9492-80d513fcd1d1')"
              title="Convert this dataframe to an interactive table."
              style="display:none;">
        
  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M0 0h24v24H0V0z" fill="none"/>
    <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
  </svg>
      </button>
      
  <style>
    .colab-df-container {
      display:flex;
      flex-wrap:wrap;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

      <script>
        const buttonEl =
          document.querySelector('#df-6a1df143-8d56-4003-9492-80d513fcd1d1 button.colab-df-convert');
        buttonEl.style.display =
          google.colab.kernel.accessAllowed ? 'block' : 'none';

        async function convertToInteractive(key) {
          const element = document.querySelector('#df-6a1df143-8d56-4003-9492-80d513fcd1d1');
          const dataTable =
            await google.colab.kernel.invokeFunction('convertToInteractive',
                                                     [key], {});
          if (!dataTable) return;

          const docLinkHtml = 'Like what you see? Visit the ' +
            '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
            + ' to learn more about interactive tables.';
          element.innerHTML = '';
          dataTable['output_type'] = 'display_data';
          await google.colab.output.renderOutput(dataTable, element);
          const docLink = document.createElement('div');
          docLink.innerHTML = docLinkHtml;
          element.appendChild(docLink);
        }
      </script>
    </div>
  </div>
  
```
:::
:::

::: {.cell .code execution_count="120" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="5J94arwRGHk4" outputId="2e7021fd-46e0-47c9-9af8-43f71eae22f6"}
``` python
insurance_dataset.isnull().sum()
```

::: {.output .execute_result execution_count="120"}
    age         0
    sex         0
    bmi         0
    children    0
    smoker      0
    region      0
    charges     0
    dtype: int64
:::
:::

::: {.cell .markdown id="5eyF28a_GnKm"}
STATISTICAL MEASUSRE
:::

::: {.cell .code execution_count="121" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":300}" id="3zf-p-uiGRme" outputId="59054235-d98d-41cf-9f68-475354a7aad2"}
``` python
insurance_dataset.describe()
```

::: {.output .execute_result execution_count="121"}
```{=html}

  <div id="df-912887d9-c899-42d9-bc6d-a6dedc0e6227">
    <div class="colab-df-container">
      <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>bmi</th>
      <th>children</th>
      <th>charges</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1338.000000</td>
      <td>1338.000000</td>
      <td>1338.000000</td>
      <td>1338.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>39.207025</td>
      <td>30.663397</td>
      <td>1.094918</td>
      <td>13270.422265</td>
    </tr>
    <tr>
      <th>std</th>
      <td>14.049960</td>
      <td>6.098187</td>
      <td>1.205493</td>
      <td>12110.011237</td>
    </tr>
    <tr>
      <th>min</th>
      <td>18.000000</td>
      <td>15.960000</td>
      <td>0.000000</td>
      <td>1121.873900</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>27.000000</td>
      <td>26.296250</td>
      <td>0.000000</td>
      <td>4740.287150</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>39.000000</td>
      <td>30.400000</td>
      <td>1.000000</td>
      <td>9382.033000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>51.000000</td>
      <td>34.693750</td>
      <td>2.000000</td>
      <td>16639.912515</td>
    </tr>
    <tr>
      <th>max</th>
      <td>64.000000</td>
      <td>53.130000</td>
      <td>5.000000</td>
      <td>63770.428010</td>
    </tr>
  </tbody>
</table>
</div>
      <button class="colab-df-convert" onclick="convertToInteractive('df-912887d9-c899-42d9-bc6d-a6dedc0e6227')"
              title="Convert this dataframe to an interactive table."
              style="display:none;">
        
  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M0 0h24v24H0V0z" fill="none"/>
    <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
  </svg>
      </button>
      
  <style>
    .colab-df-container {
      display:flex;
      flex-wrap:wrap;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

      <script>
        const buttonEl =
          document.querySelector('#df-912887d9-c899-42d9-bc6d-a6dedc0e6227 button.colab-df-convert');
        buttonEl.style.display =
          google.colab.kernel.accessAllowed ? 'block' : 'none';

        async function convertToInteractive(key) {
          const element = document.querySelector('#df-912887d9-c899-42d9-bc6d-a6dedc0e6227');
          const dataTable =
            await google.colab.kernel.invokeFunction('convertToInteractive',
                                                     [key], {});
          if (!dataTable) return;

          const docLinkHtml = 'Like what you see? Visit the ' +
            '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
            + ' to learn more about interactive tables.';
          element.innerHTML = '';
          dataTable['output_type'] = 'display_data';
          await google.colab.output.renderOutput(dataTable, element);
          const docLink = document.createElement('div');
          docLink.innerHTML = docLinkHtml;
          element.appendChild(docLink);
        }
      </script>
    </div>
  </div>
  
```
:::
:::

::: {.cell .code execution_count="122" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":769}" id="PwOmUgGNGy44" outputId="99489216-029e-4294-eafc-9b0a0fac02ae"}
``` python
#distribution of age value 
sns.set()
plt.figure(figsize=(6,6))
sns.distplot(insurance_dataset['age']) # oh no distplot is depricated we cab use 
# if i used displot it return count in the y axixs `displot` (a figure-level function with
#similar flexibility) or `histplot` (an axes-level function for histograms).
plt.title('age distibution')
plt.show()
```

::: {.output .stream .stderr}
    <ipython-input-122-0894c64b84bf>:4: UserWarning: 

    `distplot` is a deprecated function and will be removed in seaborn v0.14.0.

    Please adapt your code to use either `displot` (a figure-level function with
    similar flexibility) or `histplot` (an axes-level function for histograms).

    For a guide to updating your code to use the new functions, please see
    https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

      sns.distplot(insurance_dataset['age']) # oh no distplot is depricated we cab use
:::

::: {.output .display_data}
![](vertopal_7b9778ee567d43478f5ed343847fbfab/08e1cf26c2f8c24269970a22a633f51ec1efe95c.png)
:::
:::

::: {.cell .code execution_count="123" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":480}" id="bILOBIi1H6to" outputId="39f61f63-8f86-412a-9c04-1e2971ab4542"}
``` python
# Gender Column 


sns.countplot(x='sex',data= insurance_dataset)
plt.title('sex distibution')
plt.show()
```

::: {.output .display_data}
![](vertopal_7b9778ee567d43478f5ed343847fbfab/b398901fa86993248e359cacc95f1064d88cc564.png)
:::
:::

::: {.cell .code execution_count="123" id="gVt-2q3pPuZ4"}
``` python
```
:::

::: {.cell .code execution_count="124" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":480}" id="RkfLBYRjPyC5" outputId="008a39ae-239a-4a01-ff85-f390a083f85b"}
``` python
# Gender Column 

sns.countplot(x='smoker',data= insurance_dataset)
plt.title('smoker distibution')
plt.show()
```

::: {.output .display_data}
![](vertopal_7b9778ee567d43478f5ed343847fbfab/4857c44ae78f0cc7e8df8654e1acdd99a80a5d8d.png)
:::
:::

::: {.cell .code execution_count="125" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":480}" id="0nRKzsyUt8ee" outputId="2ae91f62-a157-4c4c-f53c-a1658d0b1c46"}
``` python
# region Column 

sns.countplot(x='region',data= insurance_dataset)
plt.title('region distibution')
plt.show()
```

::: {.output .display_data}
![](vertopal_7b9778ee567d43478f5ed343847fbfab/0eee1a678bebad48521ddf51a5c04a69b846ae16.png)
:::
:::

::: {.cell .code execution_count="126" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="uJBnFSSMuEMb" outputId="77d47ad3-a74a-4cc9-ce24-d4ba2768f43d"}
``` python
insurance_dataset['region'].value_counts()
```

::: {.output .execute_result execution_count="126"}
    southeast    364
    southwest    325
    northwest    325
    northeast    324
    Name: region, dtype: int64
:::
:::

::: {.cell .code execution_count="127" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="G9hYlCfcP5ev" outputId="3b3b95ce-7eae-4057-f465-27f8b94771f3"}
``` python
# how many   male and female to show 
insurance_dataset['sex'].value_counts()
```

::: {.output .execute_result execution_count="127"}
    male      676
    female    662
    Name: sex, dtype: int64
:::
:::

::: {.cell .code execution_count="128" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="qZevh5QgQnd3" outputId="ea367c89-0e71-405e-a826-73bd15a2d76b"}
``` python
# how many smoker yes or not show 
insurance_dataset['smoker'].value_counts()
```

::: {.output .execute_result execution_count="128"}
    no     1064
    yes     274
    Name: smoker, dtype: int64
:::
:::

::: {.cell .code execution_count="128" id="GvR_DeG0QxOu"}
``` python
```
:::

::: {.cell .code execution_count="129" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":541}" id="jMEerJrQSuKo" outputId="ffb1287b-e3d6-4988-b855-2b557e76cf7f"}
``` python
#distribution of age value 
sns.set()
plt.figure(figsize=(6,6))
sns.displot(insurance_dataset['bmi']) # oh no distplot is depricated we cab use 
# if i used displot it return count in the y axixs `displot` (a figure-level function with
#similar flexibility) or `histplot` (an axes-level function for histograms).
plt.title('bmi distibution')
plt.show()
```

::: {.output .display_data}
    <Figure size 600x600 with 0 Axes>
:::

::: {.output .display_data}
![](vertopal_7b9778ee567d43478f5ed343847fbfab/8662dce41477cb83ccfa1eb35cf30488323023fe.png)
:::
:::

::: {.cell .markdown id="4L879KqDr2OH"}
Normal BMI range \--\> 18.5 to 24.9
:::

::: {.cell .code execution_count="130" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":480}" id="Deh5lPkgSzhV" outputId="39ea8752-d5a1-4c92-95c3-cd2be72e4e73"}
``` python
# children column 
sns.countplot(x='children',data=insurance_dataset)
plt.title('Children')
plt.show()
```

::: {.output .display_data}
![](vertopal_7b9778ee567d43478f5ed343847fbfab/3842eb73ff825d4cb31a02016945ec840287ff68.png)
:::
:::

::: {.cell .code execution_count="131" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="aUVmPOIksZGQ" outputId="a98e67cf-1b69-4f5f-eeab-d8fee8a421a3"}
``` python
insurance_dataset['children'].value_counts()
```

::: {.output .execute_result execution_count="131"}
    0    574
    1    324
    2    240
    3    157
    4     25
    5     18
    Name: children, dtype: int64
:::
:::

::: {.cell .code execution_count="132" id="oc767uywspVA"}
``` python
 # Charege distribution

```
:::

::: {.cell .code execution_count="133" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":523}" id="Z2hJI_WFuzjg" outputId="c0933659-6296-4ebb-ea38-8a3e930c4ec3"}
``` python
 sns.displot(insurance_dataset['charges'])
 plt.title('Charege Distributions')
 plt.show()
```

::: {.output .display_data}
![](vertopal_7b9778ee567d43478f5ed343847fbfab/3d33334d02e293fdba5ad0f5d049e53320b624b3.png)
:::
:::

::: {.cell .markdown id="ySojkqUVvgTj"}
# Data Prepocessing

Machine do not read text so we give 0 or 1
:::

::: {.cell .code execution_count="134" id="OWgW2Q-Ju1UZ"}
``` python
# encoding sex 
insurance_dataset.replace({'sex':{'male':0,'female':1}},inplace=True)
# encoding smoker 
insurance_dataset.replace({'smoker':{'yes':0,'no':1}},inplace = True)

# encoding region class 
insurance_dataset.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}},inplace = True)
```
:::

::: {.cell .code execution_count="135" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="EF3feekAvL2Z" outputId="a4dfba65-989e-4e81-c967-8c4b9493aed3"}
``` python
 insurance_dataset.describe
```

::: {.output .execute_result execution_count="135"}
    <bound method NDFrame.describe of       age  sex     bmi  children  smoker  region      charges
    0      19    1  27.900         0       0       1  16884.92400
    1      18    0  33.770         1       1       0   1725.55230
    2      28    0  33.000         3       1       0   4449.46200
    3      33    0  22.705         0       1       3  21984.47061
    4      32    0  28.880         0       1       3   3866.85520
    ...   ...  ...     ...       ...     ...     ...          ...
    1333   50    0  30.970         3       1       3  10600.54830
    1334   18    1  31.920         0       1       2   2205.98080
    1335   18    1  36.850         0       1       0   1629.83350
    1336   21    1  25.800         0       1       1   2007.94500
    1337   61    1  29.070         0       0       3  29141.36030

    [1338 rows x 7 columns]>
:::
:::

::: {.cell .code execution_count="136" id="yPu5x1miwyJQ"}
``` python
# Split the feature and Target
# AXIS = 1 cause we remove a column if we remove row we give AXIS = 0
X = insurance_dataset.drop(columns='charges',axis=1)
Y = insurance_dataset['charges']
```
:::

::: {.cell .code execution_count="137" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":424}" id="1ieipW_Py7IK" outputId="7e3e9bd2-02fe-4b54-b645-e5d996a57450"}
``` python
X
```

::: {.output .execute_result execution_count="137"}
```{=html}

  <div id="df-48cae20d-bc8d-4c17-bee6-3faf5b86ec77">
    <div class="colab-df-container">
      <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>sex</th>
      <th>bmi</th>
      <th>children</th>
      <th>smoker</th>
      <th>region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>19</td>
      <td>1</td>
      <td>27.900</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>18</td>
      <td>0</td>
      <td>33.770</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>28</td>
      <td>0</td>
      <td>33.000</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>33</td>
      <td>0</td>
      <td>22.705</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32</td>
      <td>0</td>
      <td>28.880</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1333</th>
      <td>50</td>
      <td>0</td>
      <td>30.970</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1334</th>
      <td>18</td>
      <td>1</td>
      <td>31.920</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1335</th>
      <td>18</td>
      <td>1</td>
      <td>36.850</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1336</th>
      <td>21</td>
      <td>1</td>
      <td>25.800</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1337</th>
      <td>61</td>
      <td>1</td>
      <td>29.070</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
<p>1338 rows × 6 columns</p>
</div>
      <button class="colab-df-convert" onclick="convertToInteractive('df-48cae20d-bc8d-4c17-bee6-3faf5b86ec77')"
              title="Convert this dataframe to an interactive table."
              style="display:none;">
        
  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M0 0h24v24H0V0z" fill="none"/>
    <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
  </svg>
      </button>
      
  <style>
    .colab-df-container {
      display:flex;
      flex-wrap:wrap;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

      <script>
        const buttonEl =
          document.querySelector('#df-48cae20d-bc8d-4c17-bee6-3faf5b86ec77 button.colab-df-convert');
        buttonEl.style.display =
          google.colab.kernel.accessAllowed ? 'block' : 'none';

        async function convertToInteractive(key) {
          const element = document.querySelector('#df-48cae20d-bc8d-4c17-bee6-3faf5b86ec77');
          const dataTable =
            await google.colab.kernel.invokeFunction('convertToInteractive',
                                                     [key], {});
          if (!dataTable) return;

          const docLinkHtml = 'Like what you see? Visit the ' +
            '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
            + ' to learn more about interactive tables.';
          element.innerHTML = '';
          dataTable['output_type'] = 'display_data';
          await google.colab.output.renderOutput(dataTable, element);
          const docLink = document.createElement('div');
          docLink.innerHTML = docLinkHtml;
          element.appendChild(docLink);
        }
      </script>
    </div>
  </div>
  
```
:::
:::

::: {.cell .code execution_count="138" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="QOBiIx1Ay9TA" outputId="9dd3a2d4-626f-4f7b-81b5-0043dd9d3403"}
``` python
Y
```

::: {.output .execute_result execution_count="138"}
    0       16884.92400
    1        1725.55230
    2        4449.46200
    3       21984.47061
    4        3866.85520
               ...     
    1333    10600.54830
    1334     2205.98080
    1335     1629.83350
    1336     2007.94500
    1337    29141.36030
    Name: charges, Length: 1338, dtype: float64
:::
:::

::: {.cell .code execution_count="139" id="S-8xoTNmzE45"}
``` python
# Split Data into training and testing 
```
:::

::: {.cell .code execution_count="140" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="mJEpMBjQI3bz" outputId="b750984b-e267-43a4-907c-89b19024129d"}
``` python
X_train,X_test,Y_train,Y_test = tts(X,Y,test_size=0.2,random_state=1)
print(X.shape,X_train.shape,X_test.shape)
```

::: {.output .stream .stdout}
    (1338, 6) (1070, 6) (268, 6)
:::
:::

::: {.cell .code execution_count="141" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="4xra9b-VJHAE" outputId="854aff88-0a73-4b74-db27-a12d1d83f50f"}
``` python
X_train,X_test,Y_train,Y_test = tts(X,Y,test_size=0.2,random_state=42)
print(X.shape,X_train.shape,X_test.shape)
```

::: {.output .stream .stdout}
    (1338, 6) (1070, 6) (268, 6)
:::
:::

::: {.cell .code execution_count="141" id="bk1oP3S4JK3j"}
``` python
```
:::

::: {.cell .code execution_count="142" id="1zvT0p5bHY5M"}
``` python
X_train,X_test,Y_train,Y_test = tts(X,Y,test_size=0.2,random_state=2)
```
:::

::: {.cell .code execution_count="143" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="upBGpPcoIm3_" outputId="a31c6ca4-302a-4a90-d18e-c3f101a9c44e"}
``` python
#now check how many data train and test 
print(X.shape,X_train.shape,X_test.shape)
```

::: {.output .stream .stdout}
    (1338, 6) (1070, 6) (268, 6)
:::
:::

::: {.cell .code execution_count="144" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="6YmcIOu9VT-A" outputId="f8b673af-ea73-47b0-c846-af9549f3fdd7"}
``` python
print(Y.shape,Y_train.shape,Y_test.shape)
```

::: {.output .stream .stdout}
    (1338,) (1070,) (268,)
:::
:::

::: {.cell .code execution_count="145" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":75}" id="wEi2MMiDLexj" outputId="55182f8d-9269-4298-c1df-7890bdd95630"}
``` python
Lr = LinearRegression()
Lr
```

::: {.output .execute_result execution_count="145"}
```{=html}
<style>#sk-container-id-4 {color: black;background-color: white;}#sk-container-id-4 pre{padding: 0;}#sk-container-id-4 div.sk-toggleable {background-color: white;}#sk-container-id-4 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-4 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-4 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-4 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-4 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-4 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-4 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-4 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-4 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-4 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-4 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-4 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-4 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-4 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-4 div.sk-item {position: relative;z-index: 1;}#sk-container-id-4 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-4 div.sk-item::before, #sk-container-id-4 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-4 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-4 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-4 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-4 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-4 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-4 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-4 div.sk-label-container {text-align: center;}#sk-container-id-4 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-4 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-4" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-4" type="checkbox" checked><label for="sk-estimator-id-4" class="sk-toggleable__label sk-toggleable__label-arrow">LinearRegression</label><div class="sk-toggleable__content"><pre>LinearRegression()</pre></div></div></div></div></div>
```
:::
:::

::: {.cell .code execution_count="146" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":75}" id="on6e9QOyJQbL" outputId="97a5e387-6d3e-49a8-c1f3-9ed6ce450019"}
``` python
# Model Training

Lr.fit(X_train,Y_train)
```

::: {.output .execute_result execution_count="146"}
```{=html}
<style>#sk-container-id-5 {color: black;background-color: white;}#sk-container-id-5 pre{padding: 0;}#sk-container-id-5 div.sk-toggleable {background-color: white;}#sk-container-id-5 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-5 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-5 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-5 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-5 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-5 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-5 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-5 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-5 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-5 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-5 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-5 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-5 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-5 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-5 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-5 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-5 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-5 div.sk-item {position: relative;z-index: 1;}#sk-container-id-5 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-5 div.sk-item::before, #sk-container-id-5 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-5 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-5 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-5 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-5 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-5 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-5 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-5 div.sk-label-container {text-align: center;}#sk-container-id-5 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-5 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-5" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-5" type="checkbox" checked><label for="sk-estimator-id-5" class="sk-toggleable__label sk-toggleable__label-arrow">LinearRegression</label><div class="sk-toggleable__content"><pre>LinearRegression()</pre></div></div></div></div></div>
```
:::
:::

::: {.cell .code execution_count="147" id="JMGhe5nFKvbl"}
``` python
# model evalutaion 
```
:::

::: {.cell .code execution_count="148" id="revH74TRK2_E"}
``` python
# prediction any data on training data 

training_data_prediction = Lr.predict(X_train)
```
:::

::: {.cell .code execution_count="149" id="aOC5Rb2LK8Fk"}
``` python
# R squre values 
r2_train = metrics.r2_score(Y_train,training_data_prediction)
```
:::

::: {.cell .code execution_count="150" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="oKzOHkdZMi6E" outputId="319f2acf-25e3-4c9f-af43-805085f76443"}
``` python
print('R squrevale : ',r2_train)
```

::: {.output .stream .stdout}
    R squrevale :  0.751505643411174
:::
:::

::: {.cell .code execution_count="151" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":75}" id="kyanUYQEMnWM" outputId="a9bc93fe-840a-4786-d84c-ab6193df87d3"}
``` python
Lr
```

::: {.output .execute_result execution_count="151"}
```{=html}
<style>#sk-container-id-6 {color: black;background-color: white;}#sk-container-id-6 pre{padding: 0;}#sk-container-id-6 div.sk-toggleable {background-color: white;}#sk-container-id-6 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-6 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-6 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-6 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-6 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-6 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-6 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-6 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-6 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-6 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-6 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-6 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-6 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-6 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-6 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-6 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-6 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-6 div.sk-item {position: relative;z-index: 1;}#sk-container-id-6 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-6 div.sk-item::before, #sk-container-id-6 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-6 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-6 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-6 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-6 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-6 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-6 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-6 div.sk-label-container {text-align: center;}#sk-container-id-6 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-6 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-6" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-6" type="checkbox" checked><label for="sk-estimator-id-6" class="sk-toggleable__label sk-toggleable__label-arrow">LinearRegression</label><div class="sk-toggleable__content"><pre>LinearRegression()</pre></div></div></div></div></div>
```
:::
:::

::: {.cell .markdown id="hvXUFFzwQLvo"}
# prediction any data on test data

test_data_prediction = Lr.predict(X_test)
:::

::: {.cell .code execution_count="152" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="UdBd_RpsQXFy" outputId="5aed4bd9-0dab-4ac0-fd64-04c5ce6269b8"}
``` python
# test ting data 
test_data_prediction = Lr.predict(X_test) 
r2_test = metrics.r2_score(Y_test,test_data_prediction)
print('R squrevale : ',r2_test)
```

::: {.output .stream .stdout}
    R squrevale :  0.7447273869684076
:::
:::

::: {.cell .code execution_count="152" id="4BJQaPGSQitk"}
``` python
```
:::

::: {.cell .markdown id="I2YoqGzXRo_8"}
# Predict Score with Lr.Score() {#predict-score-with-lrscore}
:::

::: {.cell .code execution_count="153" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="ibrhhfaiRxnk" outputId="b0d453e4-7f57-4faa-e2c7-ad53a1aa9b09"}
``` python
Lr.score(X_test,Y_test)
```

::: {.output .execute_result execution_count="153"}
    0.7447273869684076
:::
:::

::: {.cell .code execution_count="154" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="Sc4xeAo_R4et" outputId="74a2dc26-e12b-42df-f494-c7d1fd0cd2c2"}
``` python
 print('X_test.shape = ',X_test.shape,'Y_test.shape = ',Y_test.shape,'X_train.shape = ',X_train.shape,'Y_train.shape = ',Y_train.shape)
```

::: {.output .stream .stdout}
    X_test.shape =  (268, 6) Y_test.shape =  (268,) X_train.shape =  (1070, 6) Y_train.shape =  (1070,)
:::
:::

::: {.cell .code execution_count="154" id="eMP8UJcWSMGm"}
``` python
 
```
:::

::: {.cell .markdown id="8yJiMlb1aZCI"}
# Data Distribute another ways
:::

::: {.cell .code execution_count="156" id="s_oXxvsBTIqE"}
``` python
x1 = insurance_dataset[['age','sex','bmi','children','smoker','region']]
y1 = insurance_dataset['charges']

```
:::

::: {.cell .code execution_count="157" id="dxqz1p3MT979"}
``` python
#plt.scatter(x1,y1)
#plt.plot(df.populations ,reg.predict(df[['populations']]),color="red")
```
:::

::: {.cell .code execution_count="158" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":519}" id="fcZi45szUmLE" outputId="2bb8dc95-4a44-445a-b989-2c40a983e76a"}
``` python
sns.displot(X_test)
```

::: {.output .execute_result execution_count="158"}
    <seaborn.axisgrid.FacetGrid at 0x7fa809cf3880>
:::

::: {.output .display_data}
![](vertopal_7b9778ee567d43478f5ed343847fbfab/6a1410853a4fcf1830092af5083ca7f03bfee316.png)
:::
:::

::: {.cell .code execution_count="159" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":519}" id="sUfPfennXRX2" outputId="76a02dd2-24d6-47e4-f119-5b3d40e976d2"}
``` python
sns.displot(Y_test)
```

::: {.output .execute_result execution_count="159"}
    <seaborn.axisgrid.FacetGrid at 0x7fa84423dc10>
:::

::: {.output .display_data}
![](vertopal_7b9778ee567d43478f5ed343847fbfab/85cd52aff7fd826411021212dd59ebf5e3baac7f.png)
:::
:::

::: {.cell .code execution_count="160" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":519}" id="OXG6HhBYXbZG" outputId="21eff1e6-9ca1-4710-f8e7-798816a0f89f"}
``` python
sns.displot(X_train)
```

::: {.output .execute_result execution_count="160"}
    <seaborn.axisgrid.FacetGrid at 0x7fa8441f63d0>
:::

::: {.output .display_data}
![](vertopal_7b9778ee567d43478f5ed343847fbfab/7aa13ad565facc0eb52ff0604f0f3813929be201.png)
:::
:::

::: {.cell .markdown id="fWzAmcn9Zt6A"}
# DATA SHOW BASED ON THE FEATURES
:::

::: {.cell .code execution_count="161" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":479}" id="66FVnOGlXmvl" outputId="74f0d168-41c6-4e4f-bdf1-f8f5d9a0c0fc"}
``` python
# Set the style of the plot
sns.set_style("ticks")

# Create a figure with 6 subplots (one for each feature in x1)
fig, axes = plt.subplots(nrows=1, ncols=6, figsize=(15, 5), sharey=True)

# Loop over the features in x1 and plot y1 vs. each feature
for i, feature in enumerate(x1.columns):
    sns.scatterplot(ax=axes[i], x=x1[feature], y=y1)
    axes[i].set_xlabel(feature)
    axes[i].set_ylabel('Insurance Charges')

# Set the title of the plot
fig.suptitle('Relationship between Features and Insurance Charges')

# Show the plot
plt.show()

#This code creates a figure with six subplots, one for each feature in x1.
# It then loops over each feature, creates a scatter plot of y1 vs. that feature, 
#and sets the x-label of the subplot to the name of the feature. Finally, 
#it sets the title of the entire plot and shows the figure.
```

::: {.output .display_data}
![](vertopal_7b9778ee567d43478f5ed343847fbfab/c76d418bf15425df8401037a90ee072e30b46819.png)
:::
:::

::: {.cell .code execution_count="161" id="-app5ii5ZPce"}
``` python

```
:::

::: {.cell .markdown id="raeUV89canwu"}
# Building and predict system single data
:::

::: {.cell .code execution_count="167" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="Kgy6YuILZVp-" outputId="6dba5b45-62ce-416e-cb29-831ee7fb53bb"}
``` python
input_data = (31,1,25.74,0,1,0)

# predicts changing tuple to numpy array
input_data_as_np_array = np.asarray(input_data)

# re shape the array 
input_data_reshaped = input_data_as_np_array.reshape(1,-1)

pre = Lr.predict(input_data_reshaped)

print('prediction now the value = ',pre)

print('the insurance cost is usd = ',pre[0])
```

::: {.output .stream .stdout}
    prediction now the value =  [3760.0805765]
    the insurance cost is usd =  3760.080576496057
:::

::: {.output .stream .stderr}
    /usr/local/lib/python3.9/dist-packages/sklearn/base.py:439: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names
      warnings.warn(
:::
:::

::: {.cell .markdown id="MA57nQdcdqaq"}
# User input test case test
:::

::: {.cell .code execution_count="169" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="ModSyZmAbrN9" outputId="9e0c5738-4fff-41c9-a168-82a1077cb30a"}
``` python
# taking input from the user
input_data_str = input("Enter input data separated by commas (age, sex, bmi, children, smoker, region): ")

# converting input data string to a list of values
input_data_list = input_data_str.split(',')

# converting list of strings to list of floats
input_data_list = [float(val) for val in input_data_list]

# predicts changing list to numpy array
input_data_as_np_array = np.asarray(input_data_list)

# reshape the array 
input_data_reshaped = input_data_as_np_array.reshape(1,-1)

pre = Lr.predict(input_data_reshaped)

print('prediction now the value = ',pre)
print('the insurance cost is usd = ',pre[0])
```

::: {.output .stream .stdout}
    Enter input data separated by commas (age, sex, bmi, children, smoker, region): 45,1,30.45,2,0,3
    prediction now the value =  [34562.41445239]
    the insurance cost is usd =  34562.41445239418
:::

::: {.output .stream .stderr}
    /usr/local/lib/python3.9/dist-packages/sklearn/base.py:439: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names
      warnings.warn(
:::
:::

::: {.cell .markdown id="6gbl7TsPd32G"}
:::

::: {.cell .code execution_count="170" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="dZ3MgyOrd4Jp" outputId="b77a383f-3057-4f06-b542-4b6853116400"}
``` python
input_data_list = [(31,1,25.74,0,1,0), (28,0,23.87,1,0,1), (45,1,30.45,2,0,3)]

for input_data in input_data_list:
    # predicts changing tuple to numpy array
    input_data_as_np_array = np.asarray(input_data)

    # re shape the array 
    input_data_reshaped = input_data_as_np_array.reshape(1,-1)

    pre = Lr.predict(input_data_reshaped)

    print('prediction for input_data =', input_data, 'is', pre[0])
    print('the insurance cost is usd = ', pre[0], '\n')
```

::: {.output .stream .stdout}
    prediction for input_data = (31, 1, 25.74, 0, 1, 0) is 3760.080576496057
    the insurance cost is usd =  3760.080576496057 

    prediction for input_data = (28, 0, 23.87, 1, 0, 1) is 27082.03785698135
    the insurance cost is usd =  27082.03785698135 

    prediction for input_data = (45, 1, 30.45, 2, 0, 3) is 34562.41445239418
    the insurance cost is usd =  34562.41445239418 
:::

::: {.output .stream .stderr}
    /usr/local/lib/python3.9/dist-packages/sklearn/base.py:439: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names
      warnings.warn(
    /usr/local/lib/python3.9/dist-packages/sklearn/base.py:439: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names
      warnings.warn(
    /usr/local/lib/python3.9/dist-packages/sklearn/base.py:439: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names
      warnings.warn(
:::
:::
