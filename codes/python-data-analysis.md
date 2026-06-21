# Python Data Analysis: Notebook-by-Notebook Reference
**CFI Business Intelligence & Data Analytics (BIDA) Course · 2026**

---

## Part 1: Introduction to Python

### Notebook 1: Variables & Data Types
**File Path**: `11. Intro Python/Getting Started with Python - Learner Files - Complete/1 - Variables & Data Types.ipynb`

This notebook introduces basic Python variables, valid naming syntax, core data types, string manipulation, and data type casting conversions.

#### 1. Variable Assignment
```python
x = 7
y = 11
z = 25
```

#### 2. Naming Conventions
Variable names must begin with a letter or an underscore, followed by letters, numbers, or underscores.
```python
# Starts with a letter
a5 = 20

# Starts with an underscore
_a8 = 45

# Descriptive name
Company01_EBIDA = 7500
```

#### 3. Printing Variables & Case Sensitivity
Python is case-sensitive. Evaluating uppercase `X` when lowercase `x` was defined yields a `NameError`.
```python
print(y)
print(z)
# print(X) # raises NameError: name 'X' is not defined
```
* **Output**:
```text
11
25
```

#### 4. Reassigning Variables
```python
x = 2
print(x)
```
* **Output**:
```text
2
```

#### 5. Numeric Data Types
```python
print(type(7))
print(type(-7))
print(type(1.25))
```
* **Output**:
```text
<class 'int'>
<class 'int'>
<class 'float'>
```

#### 6. Boolean Data Types
Booleans must be capitalised (`True` or `False`). Lowercase `true` results in a NameError.
```python
print(10 > 9)
print(type(True))
# boolean_b = true # raises NameError: name 'true' is not defined
```
* **Output**:
```text
True
<class 'bool'>
```

#### 7. Strings & Escape Characters
Strings are declared using matching single or double quotes. Escape characters (`\`) allow single quotes inside single-quoted strings.
```python
string_a = "Hello"
print(type(string_a))
print("I can't fly")
print('I can\'t fly')
```
* **Output**:
```text
<class 'str'>
I can't fly
I can't fly
```

#### 8. String Concatenation
Strings can be combined implicitly by placing them next to each other, using the `+` operator, or separating them as print function arguments (which adds an automatic space).
```text
# Implicit concatenation
'Net' 'Profit'  # Returns 'NetProfit'
```
```python
print('Net ' 'Profit')
print('Net ' + 'Profit')
print('Net', 'Profit')
```
* **Output**:
```text
Net Profit
Net Profit
Net Profit
```

#### 9. Data Type Conversion (Casting)
```python
# Float to Int (truncates decimals)
print(int(1.25))

# Int to Float
print(float(55616))

# Numbers to Strings
print(str(9))
print(str(10.72))

# Boolean to String
print(str(2 > 1))
```
* **Output**:
```text
1
55616.0
9
10.72
True
```

#### 10. Type Errors & Safe Concatenation
Adding strings to numerical types directly throws a `TypeError`. You must convert numbers to strings first.
```python
number = 5
# print(number + "Euros") # raises TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Correct method
print(str(number), "Euros")
```
* **Output**:
```text
5 Euros
```

---

### Notebook 2: Data Structures
**File Path**: `11. Intro Python/Getting Started with Python - Learner Files - Complete/2 - Data Structures.ipynb`

This notebook explores mutable lists, immutable tuples, and key-value dictionaries.

#### 1. Create List & Indexing
Lists are declared using brackets `[]` and allow positive (from 0) and negative (from -1) index slicing.
```python
list_a = ['Yuting', 'John', 'Karina', 'Rahul']
print(list_a[2])
print(list_a[-3])
```
* **Output**:
```text
Karina
John
```

#### 2. List Types (Numeric, Mixed, Nested, & Combined)
```python
list_b = [12, 11, 13]
list_c = [1, 'a', True, 2.56]

# Nested Lists
list_d = [list_a, 'Pavel']
print(list_d)

# Combined Lists
list_f = list_a + list_b
print(list_f)
```
* **Output**:
```text
[['Yuting', 'John', 'Karina', 'Rahul'], 'Pavel']
['Yuting', 'John', 'Karina', 'Rahul', 12, 11, 13]
```

#### 3. Sorting Lists
Lists containing uniform types can be sorted in-place. Sorting a mixed list yields a `TypeError`.
```python
list_a.sort()
print(list_a)

list_b.sort()
print(list_b)

# list_c.sort() # raises TypeError: '<' not supported between instances of 'str' and 'int'
```
* **Output**:
```text
['John', 'Karina', 'Rahul', 'Yuting']
[11, 12, 13]
```

#### 4. Sorting in Reverse Order
```python
list_a.sort(reverse=True)
print(list_a)

list_b.sort(reverse=True)
print(list_b)
```
* **Output**:
```text
['Yuting', 'Rahul', 'Karina', 'John']
[13, 12, 11]
```

#### 5. Modifying Lists (Append, Replace, Delete)
```python
# Append item to end
list_a.append('Rosie')
print("After Append:", list_a)

# Replace second item (index 1)
list_a[1] = 'Oscar'
print("After Replace:", list_a)

# Delete item at index 3
del list_a[3]
print("After Delete:", list_a)
```
* **Output**:
```text
After Append: ['Yuting', 'Rahul', 'Karina', 'John', 'Rosie']
After Replace: ['Yuting', 'Oscar', 'Karina', 'John', 'Rosie']
After Delete: ['Yuting', 'Oscar', 'Karina', 'Rosie']
```

#### 6. Tuple Creation & Operations
Tuples are declared using parentheses `()` and are immutable.
```python
tuple_a = ('a', 'b', 'c')
tuple_b = (1, 2, 3)
tuple_c = (1, 'a', True, 2.56)

# Tuple concatenation
tuple_e = tuple_a + tuple_b
print(tuple_e)
```
* **Output**:
```text
('a', 'b', 'c', 1, 2, 3)
```

#### 7. Tuple Immutability Verification
Attempting to append to or reassign items in a tuple yields errors.
```python
# tuple_a.append('a') # raises AttributeError: 'tuple' object has no attribute 'append'
# tuple_a[1] = 'e'    # raises TypeError: 'tuple' object does not support item assignment
# del tuple_a[3]      # raises TypeError: 'tuple' object doesn't support item deletion
```

#### 8. Dictionary Creation & Access
Dictionaries store key-value pairs declared inside braces `{}`. Values are retrieved via key strings.
```python
dict_a = {'first_name': 'Frank', 'last_name': 'Park', 'age': 20}
print(dict_a['first_name'])
```
* **Output**:
```text
Frank
```

#### 9. Duplicate Keys in Dictionaries
Lists support duplicate items, but dictionary keys must be unique. Declaring duplicate keys overwrites prior pairs, keeping only the final declared value.
```python
# Duplicate list values
list_g = ['Frank', 'Frank']
print(list_g)

# Duplicate dictionary keys
dict_c = {'first_name': 'Frank', 'first_name': 'Frank1', 'last_name': 'Park', 'age': 20}
print(dict_c)
```
* **Output**:
```text
['Frank', 'Frank']
{'first_name': 'Frank1', 'last_name': 'Park', 'age': 20}
```

#### 10. Dictionary View Items
```python
dict_sales = {'Sales': [100, 200, 240, 400, 100, 500], 'Stores': ['Store A', 'Store B', 'Store A', 'Store C', 'Store D', 'Store B']}
print(dict_sales.items())
```
* **Output**:
```text
dict_items([('Sales', [100, 200, 240, 400, 100, 500]), ('Stores', ['Store A', 'Store B', 'Store A', 'Store C', 'Store D', 'Store B'])])
```

---

### Notebook 3: Operators & Functions
**File Path**: `11. Intro Python/Getting Started with Python - Learner Files - Complete/3 - Operators & Functions.ipynb`

This notebook covers standard mathematical calculations, comparison checks, logical masks, built-in functions, and module imports.

#### 1. Arithmetic Operators
```python
print("Addition 3 + 2 =", 3 + 2)
print("Subtraction 3 - 2 =", 3 - 2)
print("Multiplication 3 * 5 =", 3 * 5)
print("Division 10 / 2 =", 10 / 2)
print("Modulo 4 % 3 =", 4 % 3)
print("Exponentiation 2 ** 4 =", 2 ** 4)
```
* **Output**:
```text
Addition 3 + 2 = 5
Subtraction 3 - 2 = 1
Multiplication 3 * 5 = 15
Division 10 / 2 = 5.0
Modulo 4 % 3 = 1
Exponentiation 2 ** 4 = 16
```

#### 2. Order of Precedence (BODMAS)
```python
print(18 / (2 + 1) ** 2)
```
* **Output**:
```text
2.0
```

#### 3. Comparison Operators
```python
print("15 > 10 is", 15 > 10)
print("15 < 10 is", 15 < 10)
print("15 >= 10 is", 15 >= 10)
print("15 <= 10 is", 15 <= 10)
print("20 == 20 is", 20 == 20)
print("'John' == 'disagreeable' is", 'John' == 'disagreeable')
print("21 != 21 is", 21 != 21)
print("'John' != 'disagreeable' is", 'John' != 'disagreeable')
```
* **Output**:
```text
15 > 10 is True
15 < 10 is False
15 >= 10 is True
15 <= 10 is False
20 == 20 is True
'John' == 'disagreeable' is False
21 != 21 is False
'John' != 'disagreeable' is True
```

#### 4. Logical Operators (and / or)
```python
# and requires both conditions to be True
x = 0
print("x=0 (and) is", x < 1 and x < 3)
x = 2
print("x=2 (and) is", x < 1 and x < 3)

# or requires at least one condition to be True
x = 0
print("x=0 (or) is", x < 1 or x < 3)
x = 2
print("x=2 (or) is", x < 1 or x < 3)
x = 4
print("x=4 (or) is", x < 1 or x < 3)
```
* **Output**:
```text
x=0 (and) is True
x=2 (and) is False
x=0 (or) is True
x=2 (or) is True
x=4 (or) is False
```

#### 5. Complex Logical Expressions
```python
a = 10
b = 5
c = 20
print(a+b > b+c or b+c < a+c)
```
* **Output**:
```text
True
```

#### 6. Built-in Core Functions
```python
print("Max value:", max(4, 7, 23, 11))
print("Min value:", min(4, 7, 23, 11))
print("Absolute value of -9.4:", abs(-9.4))
print("Sum list [1, 2, 3] =", sum([1, 2, 3]))
print("Round 4.91278 to 2 decimals:", round(4.91278, 2))
print("2 to the power of 3:", pow(2, 3))
print("Length of list:", len([1, 3, 5, 7, 9]))
```
* **Output**:
```text
Max value: 23
Min value: 4
Absolute value of -9.4: 9.4
Sum list [1, 2, 3] = 6
Round 4.91278 to 2 decimals: 4.91
2 to the power of 3: 8
Length of list: 5
```

#### 7. Import Modules (math)
```python
# Standard Import
import math
print("Square root of 100:", math.sqrt(100))

# Import with Alias
import math as mth
print("Square root of 81:", mth.sqrt(81))

# Specific Function Import
from math import sqrt
print("Square root of 25:", sqrt(25))

# Help utility
# help(math.sqrt)
```
* **Output**:
```text
Square root of 100: 10.0
Square root of 81: 9.0
Square root of 25: 5.0
```

---

### Notebook 4: Conditional Statements & For Loops
**File Path**: `11. Intro Python/Getting Started with Python - Learner Files - Complete/4 - Conditional Statements & For Loops.ipynb`

This notebook explores control structures, conditional branching paths, and iterating over lists, tuples, and dictionaries.

#### 1. Basic If Statement
```python
a = 6
b = 5
if a > b:
    print('a is greater than b')
```
* **Output**:
```text
a is greater than b
```

#### 2. If-Else Statements
```python
customer_a = 20
if customer_a > 15:
    print("high")
else:
    print("low")
```
* **Output**:
```text
high
```

#### 3. If-Elif-Else Statement
```python
customer_list = [20, 5, 10]

# Individual evaluations
customer_a = 20
if customer_a > 15:
    print("high")
elif customer_a < 10:
    print("low")
else:
    print("med")
```
* **Output**:
```text
high
```

#### 4. Iterating List with For Loops
```python
for i_customer in customer_list:
    if i_customer > 15:
        print("high")
    elif i_customer < 10:
        print("low")
    else:
        print("med")
```
* **Output**:
```text
high
low
med
```

#### 5. Iterating over a Tuple
```python
tuple1 = ('John', 10, 25, 30, 50, 'Mary')
for i in tuple1:
    print(i)
```
* **Output**:
```text
John
10
25
30
50
Mary
```

#### 6. Iterating Dictionary Keys
Iterating over a dictionary defaults to reading its keys.
```python
electronics_dict = {
  "brand": ["Apple","Microsoft","Lenova"],
  "product": ["phone","laptop",'tablet'],
  "year": [2022, 2020, 2010]}

for i_key in electronics_dict:
    print(i_key)
```
* **Output**:
```text
brand
product
year
```

#### 7. Iterating Dictionary Values
```python
for i_key in electronics_dict:
    print(electronics_dict[i_key])
```
* **Output**:
```text
['Apple', 'Microsoft', 'Lenova']
['phone', 'laptop', 'tablet']
[2022, 2020, 2010]
```

#### 8. Iterating Dictionary Key-Value Pairs
```python
for i_key, j_value in electronics_dict.items():
    print('This is the '+ i_key + ', these are the values:', j_value)
```
* **Output**:
```text
This is the brand, these are the values: ['Apple', 'Microsoft', 'Lenova']
This is the product, these are the values: ['phone', 'laptop', 'tablet']
This is the year, these are the values: [2022, 2020, 2010]
```

#### 9. Nested For Loops
```python
for i_key in electronics_dict:
    for j_value in electronics_dict[i_key]:
        print(j_value)
```
* **Output**:
```text
Apple
Microsoft
Lenova
phone
laptop
tablet
2022
2020
2010
```

---

## Part 2: Loading & Cleaning Data

### Notebook 1: Introduction to NumPy & Pandas
**File Path**: `12. Python Data Analysis/Learner Files/C1 - Loading & Cleaning Data/2 - Complete/1 - Introduction to Numpy & Pandas - Complete.ipynb`

This notebook introduces the fundamentals of NumPy arrays (for vectorised calculations) and Pandas Series/DataFrames (which label indexes).

#### 1. Import NumPy
```python
import numpy as np
```

#### 2. Create 1D array
```python
np.array([0,1,2])
```
* **Output**:
```text
array([0, 1, 2])
```

#### 3. Create 2D array
```python
Array_1 = np.array([[1,2,3],[4,5,6]])
Array_1
```
* **Output**:
```text
array([[1, 2, 3],
       [4, 5, 6]])
```

#### 4. Mixed Types Array (Type Coercion)
When lists containing different types are passed to `np.array`, elements are coerced into a single compatible type (usually strings).
```python
Array_2 = np.array([[1,2,3],['a',5,6]])
Array_2
```
* **Output**:
```text
array([['1', '2', '3'],
       ['a', '5', '6']], dtype='<U11')
```

#### 5. Check Array Shape
```python
Array_1.shape
```
* **Output**:
```text
(2, 3)
```

#### 6. NumPy Min & Max
```python
print(Array_1.min())
print(Array_1.max())
```
* **Output**:
```text
1
6
```

#### 7. 2D Indexing & Slicing
Index using `[row_index, col_index]`.
```python
# Second row, first column
Array_1[1,0]
```
* **Output**:
```text
4
```

#### 8. Import Pandas
```python
import pandas as pd
```

#### 9. Pandas Series from List (Default Index)
```python
list_1 = [12,24,36]
pd.Series(data=list_1)
```
* **Output**:
```text
0    12
1    24
2    36
dtype: int64
```

#### 10. Pandas Series from List (Custom Index Labels)
```python
markers = ['a','b','c']
pd.Series(data=list_1, index = markers)
```
* **Output**:
```text
a    12
b    24
c    36
dtype: int64
```

#### 11. Mixed Data Types Series
```python
a = 'Mike'
b = True
c = sum
pd.Series([a,b,c])
```
* **Output**:
```text
0                       Mike
1                       True
2    <built-in function sum>
dtype: object
```

#### 12. Indexing Series by Name
```python
salesQ1 = pd.Series(
    data=[300,550,240,180],
    index = ['Magnets','Coasters','Handbags','Snacks']
)
salesQ1['Magnets']
```
* **Output**:
```text
300
```

#### 13. Adding two Pandas Series
Adding series automatically aligns indices.
```python
salesQ2 = pd.Series(
    data = [340,600,225,75],
    index = ['Magnets', 'Coasters','Handbags', 'Snacks']
)
salesQ1 + salesQ2
```
* **Output**:
```text
Magnets      640
Coasters    1150
Handbags     465
Snacks       255
dtype: int64
```

#### 14. Adding Series with Mismatched Indexes
Missing alignments result in `NaN` (Not a Number).
```python
salesQ3 = pd.Series(
    data = [480,520,360,40],
    index = ['Magnets', 'Coasters','Handbags', 'Postcards']
)
salesQ1 + salesQ2 + salesQ3
```
* **Output**:
```text
Coasters     1670.0
Handbags      825.0
Magnets      1120.0
Postcards       NaN
Snacks          NaN
dtype: float64
```

#### 15. Create DataFrame from NumPy Array
```python
Data = np.array([[2,2000,3],[4,5000,4],[3,8000,4],[3,11000,5],[1,14000,6]])
Rows= ['Max', 'Will', 'Jordan', 'Chris', 'Michelle']
Columns= ['GPA', 'Tuition', 'ClassesEnrolled']
df_1 = pd.DataFrame(Data,Rows,Columns)
df_1
```
* **Output**:
```text
          GPA  Tuition  ClassesEnrolled
Max         2     2000                3
Will        4     5000                4
Jordan      3     8000                4
Chris       3    11000                5
Michelle    1    14000                6
```

#### 16. Create DataFrame from Dictionary
```python
dictionary_2 = {'Grade':['A','A','B','B','C','C'],
                'Tuition':[12500,23600,30000,30000,47200,60000],
                'State':['NY','CA','IL','IL','WI','NV']}
df_2 = pd.DataFrame(data=dictionary_2)
df_2
```
* **Output**:
```text
  Grade  Tuition State
0     A    12500    NY
1     A    23600    CA
2     B    30000    IL
3     B    30000    IL
4     C    47200    WI
5     C    60000    NV
```

#### 17. Inspect DataFrame Information
```python
df_2.info()
```
* **Output**:
```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Grade    6 non-null      object
 1   Tuition  6 non-null      int64 
 2   State    6 non-null      object
dtypes: int64(1), object(2)
memory usage: 272.0+ bytes
```

---

### Notebook 2: Loading Data
**File Path**: `12. Python Data Analysis/Learner Files/C1 - Loading & Cleaning Data/2 - Complete/2 - Loading Data - Complete.ipynb`

This notebook explores techniques for generating arrays programmatically, connecting to online web APIs, and loading local flat files.

#### 1. Generate Array with Interval Range
```python
Array_3 = np.arange(30)
Array_3
```
* **Output**:
```text
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
```

#### 2. Slicing with `arange`
```python
np.arange(3,7)
```
* **Output**:
```text
array([3, 4, 5, 6])
```

#### 3. Slicing with `arange` and step
```python
# np.arange(start, stop, step)
np.arange(1,10,2)
```
* **Output**:
```text
array([1, 3, 5, 7, 9])
```

#### 4. Linear Spacing
```python
# 20 evenly spaced floats between 0 and 5
np.linspace(0,5,20)
```
* **Output**:
```text
array([0.        , 0.26315789, 0.52631579, 0.78947368, 1.05263158,
       1.31578947, 1.57894737, 1.84210526, 2.10526316, 2.36842105,
       2.63157895, 2.89473684, 3.15789474, 3.42105263, 3.68421053,
       3.94736842, 4.21052632, 4.47368421, 4.73684211, 5.        ])
```

#### 5. Generate Zero Matrices
```python
np.zeros((3, 4))
```
* **Output**:
```text
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
```

#### 6. Random Float Values
```python
# 10 random float values between 0 and 1
np.random.rand(10)
```
* **Output**:
```text
array([0.10948721, 0.42726152, 0.11934049, 0.3120513 , 0.92493051,
       0.87818833, 0.6053977 , 0.3952584 , 0.9709223 , 0.92499124])
```

#### 7. Random Integer within Range
```python
np.random.randint(10,20)
```
* **Output**:
```text
14
```

#### 8. Random Integer Matrix with Specific Shape
```python
# Random integers between 1 and 99 in a 2x4 matrix
np.random.randint(1,100,(2,4))
```
* **Output**:
```text
array([[38, 41, 57, 18],
       [67, 46, 58, 92]])
```

#### 9. Seed the Random Number Generator
Seeding guarantees that the code produces identical random arrays each run.
```python
np.random.seed(11)
np.random.randint(10,21,5)
```
* **Output**:
```text
array([19, 10, 11, 17, 11])
```

```python
# Running it a second time without setting seed gives different values
np.random.randint(10,21,5)
```
* **Output**:
```text
array([15, 17, 14, 11, 18])
```

```python
# Resetting the seed returns the exact original values
np.random.seed(11)
np.random.randint(10,21,5)
```
* **Output**:
```text
array([19, 10, 11, 17, 11])
```

#### 10. Fetch Live Stocks via Naver DataReader API
```python
import pandas_datareader.data as pdr

# '005930' corresponds to Samsung Electronics on KOSPI
naver_df = pdr.DataReader('005930', 'naver', '2022-01-01', '2022-01-31')
naver_df.head()
```
* **Output**:
```text
             Open   High    Low  Close    Volume
Date                                            
2022-01-03  79400  79800  78200  78600  13502112
2022-01-04  78800  79200  78300  78700  12427416
2022-01-05  78800  79000  76400  77400  25470640
2022-01-06  76700  77600  76600  76900  12931954
2022-01-07  78100  78400  77400  78300  15163757
```

#### 11. Fetch Live Stock Data via yfinance API
```python
import yfinance as yf

stocks_df = yf.download('SPY', start='2022-01-01', end='2022-01-31')
stocks_df.head()
```
* **Output**:
```text
                  Open        High         Low       Close   Adj Close    Volume
Date                                                                            
2022-01-03  476.299988  477.850006  473.850006  477.709991  466.563354  72668200
2022-01-04  479.220001  479.980011  475.579987  477.549988  466.407043  71178700
2022-01-05  477.160004  477.980011  468.279999  468.380005  457.451080 104538900
2022-01-06  467.890015  470.820007  465.429993  467.940002  457.021271  86858900
2022-01-07  467.950012  469.200012  464.649994  466.089996  455.214447  85111600
```

#### 12. Load Local CSV Data
```python
df_3 = pd.read_csv('Data Source.csv')
df_3.info()
```
* **Output**:
```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1887 entries, 0 to 1886
Data columns (total 8 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   Store       1887 non-null   int64  
 1   Date        1887 non-null   object 
 2   CategoryID  1887 non-null   int64  
 3   ProductID   1887 non-null   object 
 4   Q1          1887 non-null   float64
 5   Q2          1885 non-null   object 
 6   Q3          1886 non-null   float64
 7   Q4          1881 non-null   float64
dtypes: float64(3), int64(2), object(3)
memory usage: 118.1+ KB
```

---

### Notebook 3: Cleaning Data
**File Path**: `12. Python Data Analysis/Learner Files/C1 - Loading & Cleaning Data/2 - Complete/3 - Cleaning Data - Complete.ipynb`

This notebook covers standard data auditing and cleaning techniques on transaction logs containing missing values, duplicates, wrong data types, and unparsed fields.

#### 1. Load data-source.csv
```python
import pandas as pd
import numpy as np

df_3 = pd.read_csv('data-source.csv')
df_3.head()
```
* **Output**:
```text
  TransID  Store                Date  CategoryID ProductID        Q1        Q2        Q3  Q4
0   Txn-1      1   3/10/2019 0:00:00           2  11XXRP-P  24924.50  46039.49  41595.55 NaN
1   Txn-2      1    6/4/2019 0:00:00           2  12XXRP-Q  50605.27  44682.74  47928.89 NaN
2   Txn-3      1   1/16/2019 0:00:00           2    13XXRP  13740.12  10887.84  11523.47 NaN
3   Txn-4      1  10/18/2019 0:00:00           6    14XXRP  39954.04  35351.21  36826.95 NaN
4   Txn-5      1   4/11/2019 0:00:00           2  15XXRP-A  32229.38  29620.81  26468.27 NaN
```

#### 2. Check Column Names and Index
```python
print(df_3.columns)
print(df_3.index)
```
* **Output**:
```text
Index(['TransID', 'Store', 'Date', 'CategoryID', 'ProductID', 'Q1', 'Q2', 'Q3', 'Q4'], dtype='object')
RangeIndex(start=0, stop=25, step=1)
```

#### 3. Auditing Shapes & Data Types
```python
print("Shape:", df_3.shape)
print("\nData Types:")
print(df_3.dtypes)
```
* **Output**:
```text
Shape: (25, 9)

Data Types:
TransID        object
Store           int64
Date           object
CategoryID      int64
ProductID      object
Q1            float64
Q2            float64
Q3            float64
Q4            float64
dtype: object
```

#### 4. Audit Missing Values (NaNs)
```python
df_3.isna().sum()
```
* **Output**:
```text
TransID       0
Store         0
Date          0
CategoryID    0
ProductID     0
Q1            1
Q2            2
Q3            1
Q4            8
dtype: int64
```

#### 5. Summary Statistics Profiling
```python
df_3.describe(include='all')
```

#### 6. Rename Columns
```python
df_3 = df_3.rename(columns={'Store': 'StoreID'})
```

#### 7. Convert ID Columns to Objects (Categorical)
Columns containing IDs should not be treated as numbers.
```python
df_3 = df_3.astype({
    'CategoryID': 'object',
    'StoreID': 'object'
})
```

#### 8. Convert Date Column to Datetime
```python
df_3['Date'] = pd.to_datetime(df_3['Date'])
```

#### 9. Set Row Index to TransID
```python
df_3 = df_3.set_index('TransID')
```

#### 10. Drop Rows containing any NaNs
```python
df_3.dropna()
```
* **Output**: Returns only 16 rows out of 25.

#### 11. Drop Columns containing any NaNs
```python
df_3.dropna(axis=1)
```
* **Output**: Returns a DataFrame keeping only: `StoreID`, `Date`, `CategoryID`, `ProductID`.

#### 12. Fill NaNs with 0
```python
pd.set_option('future.no_silent_downcasting', True)
df_3.fillna(0).head(6)
```
* **Output**: (Missing values in Q4 and Q2 are populated with 0.00).

#### 13. Forward Fill Missing Values
Replaces NaNs with the previous non-NaN row values.
```python
df_3.ffill().head(6)
```
* **Output**: (Txn-6's Q2 is filled with `29620.81` which is from Txn-5).

#### 14. Backward Fill Missing Values
Replaces NaNs with the next non-NaN row values.
```python
df_3.bfill().head(6)
```
* **Output**: (Txn-6's Q2 is filled with `18310.31` which is from Txn-7).

#### 15. Audit Duplicates
```python
print("Full Row Duplicates:", df_3.duplicated().sum())
print("Product Code Duplicates:", df_3['ProductID'].duplicated().sum())
```
* **Output**:
```text
Full Row Duplicates: 4
Product Code Duplicates: 5
```

#### 16. Remove Duplicates
```python
# Keep only unique rows
df_cleaned = df_3.drop_duplicates()
print("Cleaned Shape:", df_cleaned.shape)
```
* **Output**:
```text
Cleaned Shape: (21, 8)
```

```python
# Remove duplicates based on a subset (e.g. keeping only the first occurrence of each StoreID)
df_3.drop_duplicates(subset=['StoreID'])
```
* **Output**:
```text
        StoreID       Date CategoryID  ProductID        Q1        Q2        Q3        Q4
TransID                                                                                 
Txn-1         1 2019-03-10          2   11XXRP-P  24924.50  46039.49  41595.55       NaN
Txn-10        2 2019-03-10          3    110XXRP -30721.50 -31494.77  29634.13  27921.96
Txn-21        3 2019-03-10          3    116XXRP  10217.55  11873.89  13855.54  12881.02
```

#### 17. String Splitting Product Codes
Split product code suffixes into a separate column.
```python
# Check split output
df_3['ProductID'].str.split('-', expand=True).head(5)
```
* **Output**:
```text
              0     1
TransID              
Txn-1    11XXRP     P
Txn-2    12XXRP     Q
Txn-3    13XXRP  None
Txn-4    14XXRP  None
Txn-5    15XXRP     A
```

```python
# Apply split to columns
df_3[['ProductID','SpecialID']] = df_3['ProductID'].str.split('-', expand=True)
df_3.head(5)
```
* **Output**:
```text
        StoreID       Date CategoryID ProductID        Q1        Q2        Q3  Q4 SpecialID
TransID                                                                                    
Txn-1         1 2019-03-10          2    11XXRP  24924.50  46039.49  41595.55 NaN         P
Txn-2         1 2019-06-04          2    12XXRP  50605.27  44682.74  47928.89 NaN         Q
```

#### 18. Export Clean Dataset
```python
df_3.to_csv('export.csv')
```

### Chapter 1 Exercise: Loading & Cleaning at Scale (1,000 Rows)
**File Path**: `12. Python Data Analysis/Learner Files/C1 - Loading & Cleaning Data/3 - Chapter Exercise/2 - C1 - Chapter Exercise - Complete.ipynb`

This notebook applies the loaded dataset tools and cleaning functions onto a larger 1,000-row order database containing order prices, quantities, and shipping details.

#### 1. Load Chapter Exercise Data
```python
df = pd.read_csv('Chapter Exercise Data.csv')
df
```
* **Output**:
```text
     OrderID  PricePerItem  Quantity  ShippingDistance  CustomerID
0          1            10         5               3.0        6671
1          2            10        10              84.0        8647
2          3            10         1               NaN        4075
3          4            10        10              92.0        8452
4          5            10         3               2.0        2621
..       ...           ...       ...               ...         ...
995      996            10         8               2.0        6691
996      997            10         9              43.0        9782
997      998            10         2              10.0        1096
998      999            10         9              49.0        5319
999     1000            10         4              46.0        8187

[1000 rows x 5 columns]
```

#### 2. Calculate Order Values (Quantity * Price)
```python
df['PricePerItem']*df['Quantity']
```
* **Output**:
```text
0       50
1      100
2       10
3      100
4       30
      ... 
995     80
996     90
997     20
998     90
999     40
Length: 1000, dtype: int64
```

#### 3. Inspect Dataframe Info
```python
df.info()
```
* **Output**:
```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 5 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   OrderID           1000 non-null   int64  
 1   PricePerItem      1000 non-null   int64  
 2   Quantity          1000 non-null   int64  
 3   ShippingDistance  994 non-null    float64
 4   CustomerID        1000 non-null   int64  
dtypes: float64(1), int64(4)
memory usage: 39.2 KB
```

#### 4. Drop Rows with Missing Values (Checking Result)
```python
df2 = df.dropna()
df2.info()
```
* **Output**:
```text
     OrderID  PricePerItem  Quantity  ShippingDistance  CustomerID
0          1            10         5               3.0        6671
1          2            10        10              84.0        8647
3          4            10        10              92.0        8452
4          5            10         3               2.0        2621
6          7            10         2              63.0        3799
..       ...           ...       ...               ...         ...
995      996            10         8               2.0        6691
996      997            10         9              43.0        9782
997      998            10         2              10.0        1096
998      999            10         9              49.0        5319
999     1000            10         4              46.0        8187

[994 rows x 5 columns]
```

#### 5. Fill Missing Values with Zero
```python
df = df.fillna(0)
df
```
* **Output**:
```text
     OrderID  PricePerItem  Quantity  ShippingDistance  CustomerID
0          1            10         5               3.0        6671
1          2            10        10              84.0        8647
2          3            10         1               0.0        4075
3          4            10        10              92.0        8452
4          5            10         3               2.0        2621
..       ...           ...       ...               ...         ...
995      996            10         8               2.0        6691
996      997            10         9              43.0        9782
997      998            10         2              10.0        1096
998      999            10         9              49.0        5319
999     1000            10         4              46.0        8187

[1000 rows x 5 columns]
```

---

## Part 3: Data Analysis & Transformations

### Notebook 1: Transforming Data
**File Path**: `12. Python Data Analysis/Learner Files/C2 - Analyzing Data/2 - Complete/1 - Transforming Data - Complete.ipynb`

This notebook explores advanced slice manipulation, filtering datasets by conditions, writing calculated formulas, grouping rows by keys, and running relational joins.

#### 1. Load Student Grades Data
```python
import pandas as pd
import numpy as np

df_grades = pd.read_csv('student-grades.csv')
df_grades.head()
```
* **Output**:
```text
   StudentID FirstName LastName          FullName GradeAverage      Faculty  Tuition  OfficeHoursParticipated  ClassesSkipped
0   20123456      John     Park         John Park            B         Arts    44191                        0               5
1   20123457      Alex    Great        Alex Great            B      Science    32245                        4              10
2   20123458  Sebastian   Taylor  Sebastian Taylor            B     Business    42679                        6               7
3   20123459    Michael      Bay       Michael Bay            A         Math    46478                       15               2
4   20123460      Scott   Foster      Scott Foster            A  Engineering    36784                        5               8
```

#### 2. Select Columns
```python
# Single column
df_grades['StudentID'].head()

# Multiple columns
df_grades[['StudentID','GradeAverage']].head()
```

#### 3. Filtering Records with Boolean Masks
```python
# Keep students paying at least 40k tuition
df_grades[df_grades['Tuition'] >= 40000].head(3)
```
* **Output**:
```text
   StudentID  FirstName LastName          FullName GradeAverage   Faculty  Tuition  OfficeHoursParticipated  ClassesSkipped
0   20123456       John     Park         John Park            B      Arts    44191                        0               5
2   20123458  Sebastian   Taylor  Sebastian Taylor            B  Business    42679                        6               7
3   20123459    Michael      Bay       Michael Bay            A      Math    46478                       15               2
```

#### 4. Sliced Filtering Output
```python
# Find full names of students who skipped more than 5 classes
df_grades[df_grades['ClassesSkipped'] > 5]['FullName'].head(4)
```
* **Output**:
```text
1          Alex Great
2    Sebastian Taylor
4        Scott Foster
6       Ralph Wiggins
Name: FullName, dtype: object
```

#### 5. Multi-Conditional Logic Filtering
Using `&` (AND) requires all masks to evaluate to True. Note that parentheses are mandatory around each condition.
```python
eng_A = df_grades[(df_grades['Faculty'] == 'Engineering') & (df_grades['GradeAverage'] == 'A')]
eng_A
```
* **Output**:
```text
    StudentID FirstName LastName      FullName GradeAverage      Faculty  Tuition  OfficeHoursParticipated  ClassesSkipped
4    20123460     Scott   Foster  Scott Foster            A  Engineering    36784                        5               8
21   20123477      Josh     Hart     Josh Hart            A  Engineering    46468                        4               8
22   20123478    Justin     Kang   Justin Kang            A  Engineering    35859                        2               9
```

#### 6. Filter Using `.query()`
Provides a SQL-like string formatting filter.
```python
df_grades.query("Faculty == 'Engineering' and GradeAverage == 'A'")
```

#### 7. Index Slicing with `.loc` (Labels)
`loc` selects indices and columns by their label name.
```python
df_grades.loc[:, ['StudentID', 'GradeAverage']].head()
```

#### 8. Index Slicing with `.iloc` (Positions)
`iloc` selects records by position numbers (0-indexed).
```python
df_grades.iloc[:, [0, 3]].head()
```

#### 9. Index Range Slicing
* `loc` range is inclusive of the endpoint.
* `iloc` range is exclusive of the endpoint.
```python
# Slicing columns from StudentID to GradeAverage
df_grades.loc[0:3, 'StudentID':'GradeAverage']
```
* **Output**:
```text
   StudentID  FirstName LastName          FullName GradeAverage
0   20123456       John     Park         John Park            B
1   20123457       Alex    Great        Alex Great            B
2   20123458  Sebastian   Taylor  Sebastian Taylor            B
3   20123459    Michael      Bay       Michael Bay            A
```

```python
# iloc range
df_grades.iloc[0:4, 0:5]
```

#### 10. Dropping Rows
```python
# Drop single row by index
df_grades.drop([29]).tail(2)
```

```python
# Drop rows based on conditional values (e.g. drop all Business students)
business_students = df_grades['Faculty'] == 'Business'
df_grades.drop(df_grades[business_students].index).head(4)
```

#### 11. Dropping Columns
```python
df_grades = df_grades.drop(['FullName'], axis = 1)
df_grades.columns
```
* **Output**:
```text
Index(['StudentID', 'FirstName', 'LastName', 'GradeAverage', 'Faculty', 'Tuition', 'OfficeHoursParticipated', 'ClassesSkipped'], dtype='object')
```

#### 12. Element-Wise Column Operations
```python
df_grades['HoursMinusSkips'] = df_grades['OfficeHoursParticipated'] - df_grades['ClassesSkipped']
df_grades[['StudentID','HoursMinusSkips']].head(3)
```
* **Output**:
```text
   StudentID  HoursMinusSkips
0   20123456               -5
1   20123457               -6
2   20123458               -1
```

#### 13. Create Calculated Column using `.assign()`
Assign generates a new column without modifying the source dataframe in-place.
```python
df_grades2 = df_grades.assign(TuitionK = df_grades['Tuition'] / 1000)
df_grades2[['StudentID','Tuition','TuitionK']].head(3)
```
* **Output**:
```text
   StudentID  Tuition  TuitionK
0   20123456    44191    44.191
1   20123457    32245    32.245
2   20123458    42679    42.679
```

#### 14. Insert Column at Specific Position
```python
rate = df_grades['OfficeHoursParticipated'] / (df_grades['OfficeHoursParticipated'] + df_grades['ClassesSkipped'])
# Insert at column index position 5
df_grades.insert(loc=5, column='ParticipationRate', value=rate)
df_grades.head(3)
```

#### 15. Sort Values
```python
# Sort by single column ascending
df_grades.sort_values('Tuition').head(3)

# Sort by multiple columns with mixed sorting orders
df_grades.sort_values(['Faculty','Tuition'], ascending=[True, False]).head(3)
```

#### 16. Sort Index
```python
df_grades.set_index('LastName').sort_index().head(3)
```

#### 17. Groupby Counting
```python
# Count students per faculty
df_grades.groupby(by='Faculty')['StudentID'].count()
```
* **Output**:
```text
Faculty
Arts           5
Business       9
Engineering    8
Math           4
Science        4
Name: StudentID, dtype: int64
```

#### 18. Groupby Sum
```python
# Total tuition fees collected per faculty and grade combo
df_grades.groupby(by=['Faculty','GradeAverage'])['Tuition'].sum().head(5)
```
* **Output**:
```text
Faculty   GradeAverage
Arts      A                85963
          B                80728
          D                31956
Business  A                72607
          B               209423
Name: Tuition, dtype: int64
```

#### 19. Multi-Aggregate Groupings
```python
stats = df_grades.groupby('GradeAverage').agg({
    'Tuition': ['mean','max'],
    'ClassesSkipped': 'sum'
})
stats
```
* **Output**:
```text
                   Tuition        ClassesSkipped
                      mean    max            sum
GradeAverage                                    
A             39597.416667  49298             50
B             41175.285714  49682             63
C             47669.000000  47669              7
D             32591.500000  33227             14
F             44737.000000  44737              8
```

#### 20. Vertical Dataframe Merging (Union)
```python
data2 = {'StudentID': ['20123420','20123421'], 'Age':[33,31], 'FirstName': ['Stephen','Klay'],
         'LastName': ['Curry','Thompson'], 'GradeAverage': ['A','A'], 'Faculty': ['Science','Math'],
         'Tuition': [31000,41000], 'OfficeHoursParticipated': [3,1], 'ClassesSkipped': [4,6],
         'State': ['California','California']}
df_grades2 = pd.DataFrame(data2)

pd.concat([df_grades,df_grades2]).tail(3)
```

#### 21. SQL-like Left Joins
```python
# Simulated secondary database table
sch = pd.DataFrame({
    'StudentID': [20123456, 20123458, 20123460],
    'Scholarship': ['Yes', 'No', 'Yes']
})

df_sch1 = df_grades.merge(sch, on='StudentID', how='left')
df_sch1[['StudentID','FirstName','Scholarship']].head(5)
```
* **Output**:
```text
   StudentID  FirstName Scholarship
0   20123456       John         Yes
1   20123457       Alex         NaN
2   20123458  Sebastian          No
3   20123459    Michael         NaN
4   20123460      Scott         Yes
```

---

### Notebook 2: Statistical Analysis
**File Path**: `12. Python Data Analysis/Learner Files/C2 - Analyzing Data/2 - Complete/2 - Statistical Analysis - Complete.ipynb`

This notebook explores descriptive statistics, standardized score normalization, mapping conditionals, outlier detection (via Interquartile Range fences), and linear correlation tests.

#### 1. Measure Central Tendency
```python
print("Tuition Mean:", df_grades['Tuition'].mean())
print("Office Hours Median:", df_grades['OfficeHoursParticipated'].median())
print("Classes Skipped Mode:", df_grades['ClassesSkipped'].mode()[0])
```
* **Output**:
```text
Tuition Mean: 40307.066666666666
Office Hours Median: 8.5
Classes Skipped Mode: 3
```

#### 2. Full DataFrame Statistical Summary
```python
df_grades.describe()
```

#### 3. Measure Dispersion (Variance & Standard Deviation)
```python
print("Tuition Variance:", df_grades['Tuition'].var())
print("Tuition Std Dev:", df_grades['Tuition'].std())
```
* **Output**:
```text
Tuition Variance: 33555155.44367816
Tuition Std Dev: 5792.681196447648
```

#### 4. Calculate Standardized Z-Scores
A Z-score counts how many standard deviations an observation falls from the mean. Values below average are negative, while values above average are positive.
```python
mean = df_grades['OfficeHoursParticipated'].mean()
std = df_grades['OfficeHoursParticipated'].std()

df_grades['z-score'] = (df_grades['OfficeHoursParticipated'] - mean)/std
df_grades[['FirstName','OfficeHoursParticipated','z-score']].head(5)
```
* **Output**:
```text
   FirstName  OfficeHoursParticipated   z-score
0       John                        0 -1.446912
1       Alex                        4 -0.826807
2  Sebastian                        6 -0.516754
3    Michael                       15  0.878482
4      Scott                        5 -0.671781
```

#### 5. Map String Values using `np.select`
Maps grade average letters to a numerical GPA scale.
```python
df_grades['GPA'] = np.select([df_grades['GradeAverage'] == 'A',
                              df_grades['GradeAverage'] == 'B',
                              df_grades['GradeAverage'] == 'C',
                              df_grades['GradeAverage'] == 'D',
                              df_grades['GradeAverage'] == 'F'],
                             [4,3,2,1,0])
```

#### 6. IQR (Interquartile Range) Outlier Isolation
Calculates dispersion markers to identify statistical outliers.
```python
q3 = np.percentile(df_grades['GPA'], 75)
q1 = np.percentile(df_grades['GPA'], 25)
IQR = q3 - q1

print("Q1 (25th):", q1)
print("Q3 (75th):", q3)
print("IQR:", IQR)
```
* **Output**:
```text
Q1 (25th): 3.0
Q3 (75th): 4.0
IQR: 1.0
```

Apply the $1.5 \times \text{IQR}$ rule:
* Upper boundary limit = $Q3 + (1.5 \times \text{IQR}) = 4.0 + 1.5 = 5.5$
* Lower boundary limit = $Q1 - (1.5 \times \text{IQR}) = 3.0 - 1.5 = 1.5$
```python
IQR_rule = (q3 + 1.5*IQR < df_grades['GPA']) | (q1 - 1.5*IQR > df_grades['GPA'])
df_grades['Outlier'] = np.where(IQR_rule, 'yes', 'no')

# View identified outliers
df_grades[df_grades['Outlier'] == 'yes'][['FullName', 'GradeAverage', 'GPA', 'Outlier']]
```
* **Output**:
```text
         FullName GradeAverage  GPA Outlier
9   Peter Gryffin            D    1     yes
10    Louise King            D    1     yes
27     Chris Dang            F    0     yes
```
* **Note**: Any GPA below $1.5$ is marked as an outlier. Thus, students with a GPA of 1 (Grade average D) or 0 (Grade average F) are flagged.

#### 7. Correlation Analysis
Calculates the Pearson correlation coefficient between numerical columns.
```python
df_grades.corr(numeric_only=True)
```
* **Output**:
```text
                         StudentID   Tuition  OfficeHoursParticipated  ClassesSkipped   z-score       GPA
StudentID                 1.000000  0.070770                 0.214961       -0.019405  0.214961  0.097146
Tuition                   0.070770  1.000000                 0.076881       -0.218489  0.076881  0.010008
OfficeHoursParticipated   0.214961  0.076881                 1.000000       -0.669723  1.000000  0.364155
ClassesSkipped           -0.019405 -0.218489                -0.669723        1.000000 -0.669723 -0.315592
z-score                   0.214961  0.076881                 1.000000       -0.669723  1.000000  0.364155
GPA                       0.097146  0.010008                 0.364155       -0.315592  0.364155  1.000000
```
* **Insights**:
  * A strong negative correlation ($-0.67$) exists between `OfficeHoursParticipated` and `ClassesSkipped`, indicating that students who skip fewer classes participate more in office hours.
  * A positive correlation ($0.36$) exists between `OfficeHoursParticipated` and `GPA`.

#### 8. Visualizing Correlation Heatmap
```python
import seaborn as sns
sns.heatmap(df_grades.corr(numeric_only=True), cmap='coolwarm')
```

### Chapter 2 Exercise: Transforming & Analyzing at Scale (1,000 Rows)
**File Path**: `12. Python Data Analysis/Learner Files/C2 - Analyzing Data/3 - Chapter Exercise/2 - C2 - Chapter Exercise - Complete.ipynb`

This notebook applies transformation, filtering, positional indexing, dropping, and category count workflows onto the 1,000-row order database.

#### 1. Filter Orders spent >= $100
```python
df_100 = df[df['Amount'] >= 100]
df_100
```
* **Output**:
```text
      OrderID  PricePerItem  Quantity  ShippingDistance  CustomerID  Amount
0          1            10         5               3.0        6671      50
1          2            10        10              84.0        8647     100
3          4            10        10              92.0        8452     100
5          6            10         5               0.0        9160      50
7          8            10         8              65.0         809      80
..       ...           ...       ...               ...         ...     ...
993      994            10        10              75.0        1782     100
994      995            10         8              69.0        6587      80
995      996            10         8               2.0        6691      80
996      997            10         9              43.0        9782      90
998      999            10         9              49.0        5319      90

[600 rows x 6 columns]
```

#### 2. Query Customers at Specific Row Indices (299, 599, 899)
```python
df.iloc[[299,599,899],4]
```
* **Output**:
```text
300    2425
600    9647
900    9496
Name: CustomerID, dtype: int64
```

#### 3. Drop Column and Count Orders by Quantity Categories
```python
df = df.drop('ShippingDistance', axis=1)
Count_of_quantity = df.groupby('Quantity')['OrderID'].count()
Count_of_quantity
```
* **Output**:
```text
Quantity
1     113
2      95
3      98
4      94
5      98
6      91
7     103
8     102
9      96
10    110
Name: OrderID, dtype: int64
```

---

## Part 4: Data Visualization

### Notebook 1: Visualizing Data for Exploratory Analysis
**File Path**: `12. Python Data Analysis/Learner Files/C3 - Visualizing Data/2 - Complete/1 - Visualizing Data for Exploratory Analysis - Complete.ipynb`

This notebook focuses on using distribution shapes, variance box ranges, and diagnostics scatter grids to inspect raw datasets before running statistical models.

#### 1. Setup Returns Dataset
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# Load Closing Prices
stocks = pd.read_csv('stocks.csv', parse_dates=True, index_col = 'Date')[['Adj Close']]
bonds = pd.read_csv('bonds.csv', parse_dates=True, index_col = 'Date')[['Adj Close']]
oil = pd.read_csv('oil.csv', parse_dates=True, index_col = 'Date')[['Adj Close']]

# Convert to Daily Returns
stocks = stocks.pct_change()
bonds = bonds.pct_change()
oil = oil.pct_change()

# Combine DataFrames
stocksAndBonds = pd.concat([stocks, bonds, oil], axis=1, join='inner')
stocksAndBonds.columns = ['SPY','TLT','USO']
stocksAndBonds.head(3)
```

#### 2. Plot Single Variable Histogram
Shows the distribution of SPY daily returns.
```python
sns.histplot(stocksAndBonds['SPY'])
```

#### 3. Adjusting Bin Count
```python
# Increase granularity with 50 bins
sns.histplot(stocksAndBonds['SPY'], bins=50)
```

#### 4. Dodge Comparison Plot
Plots multiple column distributions side-by-side.
```python
sns.histplot(stocksAndBonds, bins=25, multiple="dodge")
```

#### 5. Layer Comparison Plot
Overlays histograms with transparency.
```python
sns.histplot(stocksAndBonds[['SPY','TLT']], bins=25, multiple="layer")
```

#### 6. Box Plot Comparison
Compares central values and outlier presence across assets.
```python
sns.boxplot(data = stocksAndBonds)
```

#### 7. Sliced Box Plot Comparison
```python
sns.boxplot(data = stocksAndBonds[['SPY','TLT']])
```

#### 8. Pairplot Grid
Generates a matrix of bivariate scatter plots alongside univariate distribution histograms on the diagonal.
```python
sns.pairplot(stocksAndBonds)
```

#### 9. Heatmap Visualizations
```python
# Standard Heatmap
sns.heatmap(stocksAndBonds.corr())
```

```python
# Styled Heatmap with annotations and custom limits
sns.heatmap(stocksAndBonds.corr(), vmin=-1, annot=True, cmap='coolwarm')
```

---

### Notebook 2: Visualizing Data for Sharing Insights
**File Path**: `12. Python Data Analysis/Learner Files/C3 - Visualizing Data/2 - Complete/2 - Visualizing Data for Sharing Insights - Complete.ipynb`

This notebook covers standard adjustments for styling line grids, mapping palettes to bar charts, adding textual labels, and building multi-dimensional bubble charts.

#### 1. Baseline Line Plot
```python
years = stocksAndBonds.index
stock_value = stocksAndBonds['SPY']

# Semicolon hides Matplotlib's print text output
plt.plot(years, stock_value);
```

#### 2. Styled Line Chart with Labels
```python
plt.plot(years, stock_value)
plt.title('Trend in \'SPY\'')
plt.xlabel('Years')
plt.ylabel('Adj Close')
plt.xticks(rotation=45);
```

#### 3. Adjusting Plot Sizing & Line Color
```python
plt.figure(figsize=(12, 8))
plt.plot(years, stock_value, color='green')
plt.title('Trend in \'SPY\'')
plt.xlabel('Years')
plt.ylabel('Adj Close')
plt.xticks(rotation=45);
```

#### 4. Custom Dotted Red Line Chart
```python
plt.figure(figsize=(12, 8))
# Dotted line styling (--), circular markers (o), marker size 3
plt.plot(years, stock_value, color = 'red', marker = 'o', markersize = 3, linestyle = '--')
plt.title('Trend in \'SPY\'')
plt.xlabel('Years')
plt.ylabel('Adj Close')
plt.xticks(rotation=45);
```

#### 5. Adjusting Axis Slicing (Limits)
```python
plt.figure(figsize=(12, 8))
plt.plot(years, stock_value)
plt.title('Trend in \'SPY\'')
plt.xlabel('Years')
plt.ylabel('Adj Close')
plt.xticks(rotation=45)
# Zoom in on the y-axis
plt.ylim(340, 500);
```

#### 6. Convert Mean Values for Bar Plot
```python
stock_mean = stocksAndBonds.mean()
bar_plot = pd.DataFrame(data = stock_mean, columns = ['mean_value'])
bar_plot
```
* **Output**:
```text
     mean_value
SPY  369.324838
TLT  134.502578
USO   35.617305
```

#### 7. Basic Vertical Bar Plot
```python
plt.figure(figsize=(12, 8))
sns.barplot(x=bar_plot.index, y='mean_value', data=bar_plot);
```

#### 8. Styled Bar Charts (Palettes)
```python
plt.figure(figsize=(12, 8))
sns.barplot(x = bar_plot.index, y = 'mean_value', data=bar_plot, palette = 'coolwarm')
plt.title('Mean Adj Close for stocks')
plt.ylabel('Mean Adj Close')
...
```
* **Output**: Displays bar charts comparing mean prices.

#### 9. Horizontal Bar Plot
Swap x and y variables to generate a horizontal chart.
```python
plt.figure(figsize=(12, 8))
sns.barplot(y = bar_plot.index, x = 'mean_value', data=bar_plot, palette = 'colorblind')
plt.title('Mean Adj Close for stocks')
plt.ylabel('Stocks')
plt.xlabel('Mean Adj Close');
```

#### 10. Horizontal Bar Plot with Annotation Text
```python
plt.figure(figsize=(12, 8))
sns.barplot(y = bar_plot.index, x = 'mean_value', data=bar_plot, palette = 'colorblind')
plt.title('Mean Adj Close for stocks')
plt.ylabel('Stocks')
plt.xlabel('Mean Adj Close')

# Add comment text at (x=300, y=0.5)
plt.annotate('SPY has the highest mean value', xy=(300, 0.5));
```

#### 11. Basic Scatter Plot
```python
stocks_pct = stocks.pct_change()
bonds_pct =  bonds.pct_change()
oil_pct =  oil.pct_change()
stocksAndBonds_pct = pd.concat([stocks_pct, bonds_pct, oil_pct], axis=1, join='inner')
stocksAndBonds_pct.columns = ['SPY','TLT','USO']

plt.figure(figsize=(12, 8))
sns.scatterplot(x = stocksAndBonds_pct['SPY'], y = stocksAndBonds_pct['TLT'])
```

#### 12. Add Year Dimension Column
```python
stocksAndBonds_pct['Year'] = stocksAndBonds_pct.index.year
```

#### 13. Scatter Plot with Style Categorical Coding
Uses different marker shapes (e.g. circles, squares) for each year.
```python
plt.figure(figsize=(12, 8))
sns.scatterplot(x = 'SPY', y = 'TLT', data = stocksAndBonds_pct, style = 'Year')
plt.title('Percent Change in Stocks vs Bonds');
```

#### 14. Scatter Plot with Hue Color Coding
Uses different colors to represent each year.
```python
plt.figure(figsize=(12, 8))
sns.scatterplot(x = stocksAndBonds_pct['SPY'], y = stocksAndBonds_pct['TLT'], data = stocksAndBonds_pct, hue = 'Year')
plt.title('Percent Change in Stocks vs Bonds');
```

#### 15. Scatter Plot with Size Bubble Coding
Varies the size of each dot to represent the year.
```python
plt.figure(figsize=(12, 8))
sns.scatterplot(x = stocksAndBonds_pct['SPY'], y = stocksAndBonds_pct['TLT'], data = stocksAndBonds_pct, size = 'Year')
plt.title('Percent Change in Stocks vs Bonds');
```

#### 16. Multi-Dimensional Scatter Plot
Encodes four dimensions on a single chart:
* **X-axis**: SPY return
* **Y-axis**: TLT return
* **Style shape**: Year
* **Color Hue & Bubble Size**: USO return magnitude
```python
plt.figure(figsize=(12, 8))
sns.scatterplot(x = 'SPY', y = 'TLT', data = stocksAndBonds_pct,
                style = 'Year', hue = 'USO', size = 'USO')
plt.title('Percent Change in Stocks vs Bonds');
```

---

### Chapter 3 Exercise: Visualizing Data at Scale (1,000 Rows)
**File Path**: `12. Python Data Analysis/Learner Files/C3 - Visualizing Data/3 - Chapter Exercise/2 - C3 - Chapter Exercise - Complete.ipynb`

This notebook generates diagnostic plots to visualize discrete frequency patterns, counts of categories, and spending coordinate clusters inside the 1,000-row cleaned orders database.

#### 1. Discrete Frequency Histogram of Order Quantities
```python
sns.histplot(df['Quantity'])
```
* **Output**: A Seaborn histogram showing discrete count bins for integer order quantities from 1 to 10.

#### 2. Grouped Order Counts per Customer
```python
# Count number of OrderID for each CustomerID
cust_orders = pd.DataFrame(df.groupby('CustomerID')['OrderID'].count())

# Count number of Customers for each Order Quantity
orders_by_customers = pd.DataFrame(cust_orders.groupby('OrderID')['OrderID'].count())

# Create bar plot
sns.barplot(x=orders_by_customers.index, y='OrderID', data=orders_by_customers)
plt.xlabel('Num of Orders')
plt.ylabel('Num of Customers')
```
* **Output**: A Seaborn bar plot showing the customer distribution based on the number of times they ordered.

#### 3. Bivariate Scatter Plot: Quantity vs. Amount
```python
sns.scatterplot(x='Quantity', y='Amount', data=df)
```
* **Output**: A Seaborn scatter grid plotting order Quantity on the X-axis and order Amount on the Y-axis.
