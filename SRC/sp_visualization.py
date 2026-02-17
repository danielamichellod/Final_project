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



