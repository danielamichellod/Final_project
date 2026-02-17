import pandas as pd
import numpy as np 

def calculate_null_percentage(dataframe):
    """
    Calculates the number and percentage of null values per column in a DataFrame.

    Args:
        dataframe : pandas.DataFrame
            The DataFrame on which null values will be calculated.

    Returns:
        tuple:
            - null_count (pandas.Series): Total number of null values per column.
            - null_percentage (pandas.Series): Percentage of null values per column, rounded to 2 decimal places.
    """
    null_count = dataframe.isnull().sum()
    null_percentage = (dataframe.isnull().sum() / dataframe.shape[0]) * 100
    null_percentage = null_percentage.round(2)
    
    return null_count, null_percentage

def general_categorical_analysis(dataframe):
    """
    Performs a general analysis of the categorical columns in a DataFrame.

    For each column of type 'object', it displays:
    - The number of unique values.
    - The relative distribution (normalized frequency).
    - Basic descriptive statistics.

    Args:
        dataframe : pandas.DataFrame
            The DataFrame containing the categorical columns to analyze.

    Returns:
        None
            The function prints and displays the results using `print()` and `display()`.
    """

    categorical_columns = dataframe.select_dtypes(include="O").columns

    if len(categorical_columns) == 0:
        print("There are no categorical columns.")

    else:
        for col in categorical_columns:
            print(f"Distribution of column {col.upper()}")
            print(f"This column has {len(dataframe[col].unique())} unique values")
            display(dataframe[col].value_counts(normalize=True))
            print("______________")
            display(dataframe[col].describe())
            print("--------------")
