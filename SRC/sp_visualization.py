import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt 

def subplot_categorical_columns_top(dataframe, top_n=20, hspace=1.2, wspace=0.4):
    """
    Generates subplots with bar charts (countplots) for all categorical columns in a DataFrame,
    showing only the top N categories per column.

    Layout: 2 plots per row.
    Figure height automatically scales with vertical spacing to avoid shrinking plots.

    Args:
        dataframe : pandas.DataFrame
        top_n : int, default=20
        hspace : float, default=0.6 (vertical spacing between rows)
        wspace : float, default=0.3 (horizontal spacing between plots)

    Returns:
        None
    """

    # Select categorical columns
    categorical_cols = dataframe.select_dtypes(include=['object', 'category']).columns
    num_cols = len(categorical_cols)

    if num_cols == 0:
        print("There are no categorical columns in the DataFrame.")
        return

    # Two plots per row
    rows = (num_cols + 1) // 2

    # Automatic figure height scaling
    base_height_per_row = 5
    spacing_factor = 1 + hspace
    fig_height = rows * base_height_per_row * spacing_factor

    fig, axes = plt.subplots(rows, 2, figsize=(18, fig_height))
    axes = axes.flatten()

    for i, col in enumerate(categorical_cols):
        top_categories = dataframe[col].value_counts().nlargest(top_n).index
        
        sns.countplot(
            data=dataframe[dataframe[col].isin(top_categories)],
            x=col,
            ax=axes[i],
            palette="pastel",
            order=top_categories
        )

        axes[i].set_title(f'Distribution of {col}', fontsize=12)
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Frequency')
        axes[i].tick_params(axis='x', rotation=90)

    # Remove unused axes if odd number of columns
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Apply spacing
    fig.subplots_adjust(hspace=hspace, wspace=wspace)

    plt.show()
    
def subplot_numeric_columns(dataframe, columns):
    """
    Generates subplots with histograms and boxplots for each provided numeric column.

    For each column:
    - A histogram is displayed showing the frequency distribution.
    - A boxplot is displayed to visually identify potential outliers.

    The plots are organized in multiple rows, with two plots per row:
    - Left column: Histogram
    - Right column: Boxplot

    Args:
        dataframe : pandas.DataFrame
            The DataFrame containing the numeric data.
        
        columns : list of str
            List of numeric column names to visualize.

    Returns:
        None
            The function directly displays the plots using matplotlib and seaborn.
            It does not return any value.

    Notes:
    ------
    - Column names in `columns` should correspond to numeric columns.
    - The number of rows is automatically calculated based on the number of columns.
    - Requires `matplotlib.pyplot` as `plt` and `seaborn` as `sns`.
    - Histograms use 200 bins by default.
    """

    num_graphs = len(columns)

    if num_graphs == 0:
        print("No numeric columns were provided.")
        return

    # One row per numeric column (each row has 2 plots)
    fig, axes = plt.subplots(num_graphs, 2, figsize=(15, num_graphs * 5))

    # If only one column, axes needs reshaping
    if num_graphs == 1:
        axes = [axes]

    for i, col in enumerate(columns):
        # Histogram
        sns.histplot(data=dataframe, x=col, ax=axes[i][0], bins=200)
        axes[i][0].set_title(f'Distribution of {col}')
        axes[i][0].set_xlabel(col)
        axes[i][0].set_ylabel('Frequency')

        # Boxplot
        sns.boxplot(data=dataframe, x=col, ax=axes[i][1])
        axes[i][1].set_title(f'Boxplot of {col}')

    plt.tight_layout()
    plt.show()



