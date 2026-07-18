<div align="center">

# Pandas Data Analysis Fundamentals

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-green.svg)](https://www.w3schools.com/python/pandas/default.asp)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Pandas-150458.svg)](https://www.geeksforgeeks.org/python/python-data-analysis-using-pandas/)

A beginner-friendly repository to learn and practice Data Analysis using Pandas.

</div>

---

# Overview

> [!NOTE]
> This notebook demonstrates real-world dataframe operations such as loading datasets, filtering data, cleaning records, grouping information, and exporting processed files.

---
# Terms to Know

---

![Dataset](https://img.shields.io/badge/Dataset-4CAF50)
![Observation](https://img.shields.io/badge/Observation-2196F3)
![Feature](https://img.shields.io/badge/Feature-9C27B0)
![Target Variable](https://img.shields.io/badge/Target-E91E63)
![DataFrame](https://img.shields.io/badge/DataFrame-3F51B5)
![Series](https://img.shields.io/badge/Series-009688)
![Index](https://img.shields.io/badge/Index-795548)
![Shape](https://img.shields.io/badge/Shape-673AB7)
![Dimension](https://img.shields.io/badge/Dimension-FF9800)
![Size](https://img.shields.io/badge/Size-607D8B)
![Data Type](https://img.shields.io/badge/Data%20Type-F44336)
![Missing Value](https://img.shields.io/badge/Missing%20Value-00BCD4)
![Duplicate Data](https://img.shields.io/badge/Duplicate-8BC34A)
![Unique Values](https://img.shields.io/badge/Unique%20Values-FF5722)
![Categorical Data](https://img.shields.io/badge/Categorical-9E9D24)
![Numerical Data](https://img.shields.io/badge/Numerical-3F51B5)
![Continuous Data](https://img.shields.io/badge/Continuous-00ACC1)
![Discrete Data](https://img.shields.io/badge/Discrete-8E24AA)
![Structured Data](https://img.shields.io/badge/Structured-43A047)
![Unstructured Data](https://img.shields.io/badge/Unstructured-E53935)
![Semi Structured Data](https://img.shields.io/badge/Semi--Structured-FDD835)
![Data Cleaning](https://img.shields.io/badge/Data%20Cleaning-1E88E5)
![Aggregation](https://img.shields.io/badge/Aggregation-7CB342)
![Filtering](https://img.shields.io/badge/Filtering-5E35B1)
![Sorting](https://img.shields.io/badge/Sorting-F4511E)
![Mean](https://img.shields.io/badge/Mean-3949AB)
![Median](https://img.shields.io/badge/Median-00897B)
![Mode](https://img.shields.io/badge/Mode-D81B60)
![Standard Deviation](https://img.shields.io/badge/Standard%20Deviation-039BE5)
![Variance](https://img.shields.io/badge/Variance-7E57C2)
![Minimum Value](https://img.shields.io/badge/Minimum-43A047)
![Maximum Value](https://img.shields.io/badge/Maximum-E53935)
![Scaling](https://img.shields.io/badge/Scaling%20%2F%20Normalization-F57C00)
![Training Dataset](https://img.shields.io/badge/Training%20Dataset-2E7D32)
![Test Dataset](https://img.shields.io/badge/Test%20Dataset-C62828)
![Validation Dataset](https://img.shields.io/badge/Validation%20Dataset-6A1B9A)
![Target Vector](https://img.shields.io/badge/Target%20Vector%20(y)-AD1457)
![Merge](https://img.shields.io/badge/Merge%20%2F%20Join-4527A0)

---

### Dataset
***Definition:*** A collection of related data organized in a structured format for analysis.

***Example:*** A CSV file containing customer details such as Name, Age, Country, and Salary.

---

### Observation / Record / Instance / Sample
***Definition:*** A single row in a dataset representing one individual entity or event.

***Example:*** One customer's information in a customer dataset.

---

### Feature / Attribute / Variable / Column
***Definition:*** A measurable property or characteristic of an observation.

***Example:*** Age, Salary, Country, Gender.

---

### Target Variable / Label
***Definition:*** The output variable that a machine learning model aims to predict.

***Example:*** House Price, Customer Churn, Pass/Fail.

---

### DataFrame
***Definition:*** A two-dimensional labeled data structure consisting of rows and columns.

***Example:*** A table containing employee information.

---

### Series
***Definition:*** A one-dimensional labeled array representing a single column of data.

***Example:*** The `Age` column of a dataset.

---

### Index
***Definition:*** Unique labels used to identify rows in a dataset.

***Example:*** 0, 1, 2, 3, ...

---

### Shape
***Definition:*** The dimensions of a dataset represented as the number of rows and columns.

***Example:*** `(1000, 5)` means 1000 rows and 5 columns.

---

### Dimension
***Definition:*** The number of axes in a data structure.

***Example:*** A Series has 1 dimension, while a DataFrame has 2 dimensions.

---

### Size
***Definition:*** The total number of elements present in a dataset.

***Example:*** A dataset with 100 rows and 5 columns has a size of 500.

---

### Data Type (dtype)
***Definition:*** The type of values stored in a column.

***Example:*** Integer, Float, String, Boolean, DateTime.

---

### Missing Value / Null Value
***Definition:*** A data value that is absent or unavailable.

***Example:*** A customer's phone number field left empty.

---

### Duplicate Data
***Definition:*** Repeated observations appearing more than once in a dataset.

***Example:*** The same customer record stored twice.

---

### Unique Values
***Definition:*** Distinct values present in a column.

***Example:*** Countries such as India, USA, and Germany appearing in a `Country` column.

---

### Categorical Data
***Definition:*** Data representing categories or groups rather than numerical quantities.

***Example:*** Gender, Department, Blood Group.

---

### Numerical Data
***Definition:*** Data represented by numbers and used for mathematical operations.

***Example:*** Age, Salary, Temperature.

---

### Continuous Data
***Definition:*** Numerical data that can take any value within a range.

***Example:*** Height = 172.56 cm.

---

### Discrete Data
***Definition:*** Numerical data that can take only specific countable values.

***Example:*** Number of Students = 45.

---

### Structured Data
***Definition:*** Data organized in a predefined tabular format.

***Example:*** Excel files, SQL tables, CSV files.

---

### Unstructured Data
***Definition:*** Data without a predefined format or organization.

***Example:*** Images, Videos, Audio files.

---

### Semi-Structured Data
***Definition:*** Data that has some organizational properties but does not follow a strict tabular structure.

***Example:*** JSON and XML files.

---

### Data Cleaning
***Definition:*** The process of detecting and correcting inaccurate, missing, or inconsistent data.

***Example:*** Filling missing salary values with the average salary.

---

### Data Wrangling
***Definition:*** The process of transforming raw data into a usable format for analysis.

***Example:*** Combining multiple datasets and renaming columns.

---

### Exploratory Data Analysis (EDA)
***Definition:*** The process of analyzing and summarizing datasets to understand patterns and relationships.

***Example:*** Studying sales trends using statistical summaries and plots.

---

### Aggregation
***Definition:*** The process of combining multiple values into summary statistics.

***Example:*** Calculating total sales for each country.

---

### Filtering
***Definition:*** Selecting a subset of data that satisfies specific conditions.

***Example:*** Selecting customers whose salary is greater than ₹50,000.

---

### Sorting
***Definition:*** Arranging data in ascending or descending order.

***Example:*** Sorting products by price.

---

### Correlation
***Definition:*** A statistical measure that indicates the strength and direction of the relationship between two variables.

***Example:*** Height and Weight often have a positive correlation.

---

### Mean
***Definition:*** The arithmetic average of a set of values.

***Example:*** Average marks of students.

---

### Median
***Definition:*** The middle value in an ordered dataset.

***Example:*** Middle salary among employees.

---

### Mode
***Definition:*** The value that appears most frequently in a dataset.

***Example:*** The most common blood group in a hospital dataset.

---

### Standard Deviation
***Definition:*** A measure of how spread out data values are from the mean.

***Example:*** Measuring variation in student marks.

---

### Variance
***Definition:*** The average of the squared differences from the mean.

***Example:*** Determining the spread of monthly sales values.

---

### Minimum Value
***Definition:*** The smallest value in a dataset.

***Example:*** Lowest temperature recorded.

---

### Maximum Value
***Definition:*** The largest value in a dataset.

***Example:*** Highest employee salary.

---

### Quantile
***Definition:*** Values that divide a dataset into equal-sized intervals.

***Example:*** Quartiles divide data into four equal parts.

---

### Outlier
***Definition:*** An observation that differs significantly from the majority of the data.

***Example:*** A salary value of ₹10,00,000 in a dataset where most salaries are below ₹1,00,000.

---

### Feature Engineering
***Definition:*** The process of creating new useful features from existing data.

***Example:*** Creating `Total_Price = Price × Quantity`.

---

### Encoding
***Definition:*** The process of converting categorical data into numerical form.

***Example:*** Male = 0, Female = 1.

---

### Scaling / Normalization
***Definition:*** The process of transforming numerical features into a common range.

***Example:*** Converting values from 0–1000 into 0–1.

---

### Training Dataset
***Definition:*** The portion of data used to train a machine learning model.

***Example:*** 80% of a customer dataset used for model learning.

---

### Test Dataset
***Definition:*** The portion of data used to evaluate a trained model.

***Example:*** Remaining 20% of customer data.

---

### Validation Dataset
***Definition:*** A subset of data used to tune model parameters during training.

***Example:*** A portion of training data reserved for hyperparameter tuning.

---

### Feature Matrix (X)
***Definition:*** The set of input variables used for prediction.

***Example:*** Age, Salary, and Experience columns.

---

### Target Vector (y)
***Definition:*** The output variable associated with the feature matrix.

***Example:*** Employee Promotion Status.

---

### Dimensionality Reduction
***Definition:*** The process of reducing the number of features while preserving important information.

***Example:*** Using PCA to reduce 50 features to 10.

---

### Time Series Data
***Definition:*** Data collected and ordered over time intervals.

***Example:*** Daily stock prices.

---

### Pivot Table
***Definition:*** A summarized table used to aggregate and reorganize data.

***Example:*** Total sales by country and year.

---

### Merge / Join
***Definition:*** The process of combining two or more datasets based on common columns.

***Example:*** Joining customer and order datasets using Customer_ID.

---

### Concatenation
***Definition:*** The process of appending datasets vertically or horizontally.

***Example:*** Combining monthly sales datasets into a yearly dataset.

---
# Prerequisites

- Python 3.10+
- Jupyter Notebook / JupyterLab
- Pandas Library

## Installation

```bash
pip install pandas
```

Import Pandas:

```python
import pandas as pd
```

---

# Dataset Files

- `orders.csv`
- `orders.xlsx`
- `modified_orders.csv`

---

# Functions and Commands Used

---

## Creating DataFrames

### Function

```python
pd.DataFrame(data)
```

#### Syntax

```python
pd.DataFrame(
    data=None,
    index=None,
    columns=None
)
```

#### Parameters

| Parameter | Description |
|-----------|-------------|
| `data` | Dictionary, list, tuple, ndarray or another dataframe |
| `index` | Row labels |
| `columns` | Column names |

#### Example

```python
data = {
    "Name": ["Alex", "John"],
    "Age": [20, 25]
}

df = pd.DataFrame(data)
```

#### Returns

  A Pandas DataFrame object.

---

## Reading CSV Files

### Function

```python
pd.read_csv()
```

#### Syntax

```python
pd.read_csv(
    filepath,
    sep=',',
    header='infer'
)
```

#### Example

```python
df = pd.read_csv("orders.csv")
```

#### Common Parameters

| Parameter | Purpose |
|------------|----------|
| `filepath` | CSV file location |
| `sep` | Separator character |
| `header` | Header row index |
| `index_col` | Set index column |
| `encoding` | File encoding |

#### Returns

  DataFrame containing CSV data.

---

## Reading Excel Files

#### Function

```python
pd.read_excel()
```

###### Syntax

```python
pd.read_excel(
    io,
    sheet_name=0
)
```

###### Example

```python
df = pd.read_excel("orders.xlsx")
```

###### Parameters

| Parameter | Description |
|-----------|-------------|
| `io` | Excel file path |
| `sheet_name` | Sheet to read |

---

## Display First Rows

#### Function

```python
df.head()
```

###### Syntax

```python
df.head(n=5)
```

###### Example

```python
df.head(10)
```

###### Returns

First `n` rows of dataframe.

---

## Display Last Rows

#### Function

```python
df.tail()
```

###### Syntax

```python
df.tail(n=5)
```

###### Example

```python
df.tail(3)
```

---

## Data Information

#### Function

```python
df.info()
```

###### Syntax

```python
df.info()
```

###### Returns

- Total rows
- Non-null count
- Datatypes
- Memory usage

---

## Statistical Summary

#### Function

```python
df.describe()
```

###### Syntax

```python
df.describe()
```

###### Returns

- Count
- Mean
- Standard deviation
- Minimum value
- Maximum value
- Quartiles

---

## Display Column Names

#### Property

```python
df.columns
```

###### Syntax

```python
df.columns
```

###### Example

```python
print(df.columns)
```

Returns all column labels.

---

## Display Index

#### Property

```python
df.index
```

###### Example

```python
print(df.index)
```

Returns row indexing information.

---

## Selecting Columns

#### Single Column

```python
df["Country"]
```

###### Syntax

```python
df[column_name]
```

Returns Series object.

---

#### Multiple Columns

```python
df[["Country","Price"]]
```

###### Syntax

```python
df[[col1,col2,...]]
```

Returns DataFrame.

---

## Integer Based Indexing

#### Function

```python
df.iloc[]
```

###### Syntax

```python
df.iloc[row, column]
```

###### Examples

```python
df.iloc[0]

df.iloc[0:5]

df.iloc[2,3]
```

---

## Label Based Indexing

#### Function

```python
df.loc[]
```

###### Syntax

```python
df.loc[row_label, column_label]
```

###### Examples

```python
df.loc[0]

df.loc[:, "Country"]

df.loc[
    df["Country"]=="USA",
    "Price"
]
```

---

## Conditional Filtering

###### Equality

```python
df[df["Country"]=="USA"]
```

###### Greater Than

```python
df[df["Price"] > 500]
```

###### Less Than

```python
df[df["Quantity"] < 10]
```

###### Syntax

```python
df[condition]
```

---

## Logical Operators

#### AND

```python
&
```

Example:

```python
df[
    (df["Country"]=="USA") &
    (df["Price"]>500)
]
```

---

#### OR

```python
|
```

Example:

```python
df[
    (df["Country"]=="USA") |
    (df["Country"]=="India")
]
```

---

#### NOT

```python
~
```

Example:

```python
~df["Country"].isin(["USA"])
```

---

## Membership Checking

#### Function

```python
isin()
```

###### Syntax

```python
Series.isin(values)
```

###### Example

```python
df["Country"].isin(
    ["USA","India"]
)
```

Returns Boolean Series.

---

## String Operations

#### Starts With

```python
df["Name"].str.startswith("A")
```

###### Syntax

```python
Series.str.startswith(pattern)
```

---

#### Ends With

```python
df["Name"].str.endswith("n")
```

###### Syntax

```python
Series.str.endswith(pattern)
```

---

#### Convert to Uppercase

```python
df["Country"].str.upper()
```

###### Syntax

```python
Series.str.upper()
```

---

#### Convert to Lowercase

```python
df["Country"].str.lower()
```

###### Syntax

```python
Series.str.lower()
```

---

#### Convert to Title Case

```python
df["Country"].str.title()
```

###### Syntax

```python
Series.str.title()
```

---

## Updating Values

```python
df.loc[
    condition,
    "column"
] = value
```

###### Example

```python
df.loc[
    df["Country"]=="UAE",
    "Country"
] = "United Arab Emirates"
```

---

## Removing Rows or Columns

#### Function

```python
drop()
```

###### Syntax

```python
df.drop(
    labels,
    axis=0
)
```

###### Examples

```python
df.drop(5)

df.drop(
    "Country",
    axis=1
)
```

---

## Removing Missing Values

#### Function

```python
dropna()
```

###### Syntax

```python
df.dropna(
    axis=0,
    how='any'
)
```

###### Example

```python
df.dropna()
```

---

## Filling Missing Values

#### Function

```python
fillna()
```

###### Syntax

```python
df.fillna(value)
```

###### Example

```python
df.fillna(0)
```

---

## Renaming Columns

#### Function

```python
rename()
```

###### Syntax

```python
df.rename(
    columns={
        old:new
    }
)
```

###### Example

```python
df.rename(
    columns={
        "OrderID":"Order_ID"
    }
)
```

---

## Counting Unique Values

#### Function

```python
value_counts()
```

###### Syntax

```python
Series.value_counts()
```

###### Example

```python
df["Country"].value_counts()
```

---

## Grouping Data

#### Function

```python
groupby()
```

###### Syntax

```python
df.groupby(column)
```

###### Example

```python
df.groupby(
    "Country"
)["Price"].sum()
```

---

## Sorting Data

#### Function

```python
sort_values()
```

###### Syntax

```python
df.sort_values(
    by,
    ascending=True
)
```

###### Example

```python
df.sort_values(
    "Price",
    ascending=False
)
```

---

## Exporting Data

#### Function

```python
to_csv()
```

###### Syntax

```python
df.to_csv(
    path,
    index=False
)
```

###### Example

```python
df.to_csv(
    "modified_orders.csv",
    index=False
)
```

---

## Frequently Used Small Commands

#### Shape of Dataset

```python
df.shape
```

###### Syntax

```python
df.shape
```

Returns:

```python
(rows, columns)
```

---

#### Data Types

```python
df.dtypes
```

###### Syntax

```python
df.dtypes
```

---

#### Number of Rows

```python
len(df)
```

###### Syntax

```python
len(object)
```

---

#### Unique Values

```python
df["Country"].unique()
```

###### Syntax

```python
Series.unique()
```

---

#### Number of Unique Values

```python
df["Country"].nunique()
```

###### Syntax

```python
Series.nunique()
```

---

#### Copy DataFrame

```python
df.copy()
```

###### Syntax

```python
df.copy(deep=True)
```

---

#### Save Excel File

```python
df.to_excel()
```

###### Syntax

```python
df.to_excel(
    path,
    index=False
)
```

---

# Learning Outcomes

After completing this notebook, users will be able to:

- Create DataFrames.
- Load CSV and Excel files.
- Inspect and analyze datasets.
- Filter data efficiently.
- Clean and preprocess data.
- Update records.
- Aggregate and summarize information.
- Export processed datasets.
- Apply Pandas operations in real-world projects.

---

# Author

**S Sabari Poornesh**  
Automation and Robotics Engineering  
Amrita Vishwa Vidyapeetham, Coimbatore
