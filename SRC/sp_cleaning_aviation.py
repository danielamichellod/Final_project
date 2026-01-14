import pandas as pd

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


