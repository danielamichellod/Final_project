import pandas as pd
import numpy as np 

def preliminary_eda(df):
    """
    Performs a preliminary exploratory analysis on a DataFrame.

    Displays:
    - A random sample of 5 rows from the DataFrame.
    - General information about the DataFrame (columns, types, memory usage, etc.).
    - Percentage of null values per column.
    - Total number of duplicate rows.
    - Count of unique values in categorical columns (type 'object').

    Args:
    df : pandas.DataFrame
        The DataFrame on which to perform the exploratory analysis.

    Returns:
    None
    The function displays the results directly using `print()` and `display()`.
    """

    display(df.sample(5))
    
    print('----------------')
    
    print('INFO')
    
    display(df.info())
    
    print('----------------')
    
    print('NULL')
    
    display(round(df.isnull().sum()/df.shape[0]*100,2))
    
    print('----------------')
    
    print('DUPLICATES')
    
    print(df.duplicated().sum())
    
    print('----------------')
    
    print('VALUE COUNTS')
    
    for col in df.select_dtypes(include ='O').columns:
        print(df[col].value_counts())
        print('---------------------------')

def zero_fill(df, list_col):
    """
    Replaces missing values (NaN) with zero in the specified columns of a DataFrame.

    This function is useful when you want to impute missing values
    with zero in numerical or categorical columns where zero is a meaningful value.

    Args:
    df : pandas.DataFrame
        The DataFrame containing the data.
    lista_col : list of str
        List of column names where NaN values should be replaced with 0.
    
    Returns:
    None
        The function modifies the original DataFrame directly (in-place).
    """
    for col in list_col:
        df[col] = df[col].fillna(0)

def fill_unknown(df, list_col):
    """
    Replaces missing values (NaN) with "UNKNOWN" in the specified categorical columns
    of a DataFrame.

    This function is useful when imputing missing values in categorical variables
    where assigning an explicit category such as "UNKNOWN" is more appropriate
    than dropping the rows.

    Args:
    df : pandas.DataFrame
        The DataFrame containing the data.
    list_col : list of str
        List of categorical column names where NaN values should be replaced 
        with "UNKNOWN".
    
    Returns:
    None
        The function modifies the original DataFrame directly (in-place).
    """
    for col in list_col:
        df[col] = df[col].fillna("UNKNOWN")

def hhmm_to_str_inplace(df, hhmm_columns):
    """
    Converts HHMM integer columns to string format "HHhMM" in-place,
    replacing the original columns.

    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame containing HHMM columns.
    hhmm_columns : list of str
        List of HHMM columns to convert.

    Returns:
    --------
    None
        The DataFrame columns are replaced in-place with formatted strings.
    """

    def convert(x):
        if pd.isna(x) or x == 0:
            return np.nan
        x = int(x)
        hours = x // 100
        minutes = x % 100
        return f"{hours:02d}h{minutes:02d}"

    for col in hhmm_columns:
        if col in df.columns:
            df[col] = df[col].apply(convert)
        else:
            print(f"Warning: Column '{col}' not found, skipping.")




