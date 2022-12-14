# TOPSIS-Python

Project By: **Bhavya Kakwani**

***

## What is TOPSIS

**T**echnique for **O**rder **P**reference by **S**imilarity to **I**deal
**S**olution (TOPSIS) originated in the 1980s as a multi-criteria decision
making method. TOPSIS chooses the alternative of shortest Euclidean distance
from the ideal solution, and greatest distance from the negative-ideal
solution. More details at [wikipedia](https://en.wikipedia.org/wiki/TOPSIS).

<br>

## How to use this package:

The Topsis-Bhavya-101903365 has a function topsis() that takes 4 parameters, i.e., inputFile, weights, impacts, and outputFile, and returns the resulting dataframe having **Topsis Score** and **Rank** as additional columns. 

Where,

* **inputFile:** Can be either csv file or pandas dataframe. Input file must contain three or more columns, where, First column is the object/variable name like M1, M2, M3, M4, etc. Also, from 2nd to last columns must contain numeric values only.
* **weights:** In the form of string having numerical values separated by commas.
* **impacts:** In the form of string having + or - values separated by commas. Here, + refers to positive impact, whereas, - refers to negative impact.
* **outputFile** (optional): csv file in which output of the function will be stored.


For Example,

### Method 1: By passing csv file as input
```python
>>> import Topsis_Bhavya_101903365 as t
>>> inputFile = "input.csv"
>>> weights = "1,1,1,2,1"
>>> impacts = "+,+,-,+,+"
>>> result_df = t.topsis(inputFile, weights, impacts)
```
<br>

### Method 2: By passing pandas dataframe as input
```python
>>> import Topsis_Bhavya_101903365 as t
>>> import pandas as pd
>>> dataFrame = pd.read_csv("input.csv)
>>> weights = "1,1,1,2,1"
>>> impacts = "+,+,-,+,+"
>>> result_df = t.topsis(dataFrame, weights, impacts)
```

<br>

## Sample Input 

### Dataset

Fund Name | P1 | P2 | P3 | P4 | P5
----------|----|----|----|----|----
M1 | 0.65 | 0.42 | 3.3 | 46.3 | 12.67
M2 | 0.81 | 0.66 | 4.9 | 51.4 | 14.44
M3 | 0.87 | 0.76 | 6 | 65.4 | 18.26
M4 | 0.87 | 0.76 | 4.2 | 40.7 | 11.63
M5 | 0.75 | 0.56 | 6.8 | 57.5 | 16.4
M6 | 0.64 | 0.41 | 5.3 | 44.7 | 12.76
M7 | 0.77 | 0.59 | 4.7 | 49.8 | 13.97
M8 | 0.7 | 0.49 | 3.1 | 43.9 | 12.05

### Weights

weights = "1,1,1,2,1"

### Impacts

impacts = "+,+,-,+,+"

<br>

## Sample Output

Fund Name | P1 | P2 | P3 | P4 | P5 | Topsis Score | Rank
----------|----|----|----|----|----|--------------|------
M1 | 0.65 | 0.42 | 3.3 | 46.3 | 12.67 | 0.41202513 | 7
M2 | 0.81 | 0.66 | 4.9 | 51.4 | 14.44 | 0.510060544 | 2
M3 | 0.87 | 0.76 | 6 | 65.4 | 18.26 | 0.685105262 | 1
M4 | 0.87 | 0.76 | 4.2 | 40.7 | 11.63 | 0.433129944 | 5
M5 | 0.75 | 0.56 | 6.8 | 57.5 | 16.4 | 0.469643489 | 3
M6 | 0.64 | 0.41 | 5.3 | 44.7 | 12.76 | 0.225789842 | 8
M7 | 0.77 | 0.59 | 4.7 | 49.8 | 13.97 | 0.451566364 | 4
M8 | 0.7 | 0.49 | 3.1 | 43.9 | 12.05 | 0.418005937 | 6 

<br>