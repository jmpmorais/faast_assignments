""" Cleaning Script """

import pandas as pd

def clean_data(initial_df: pd.DataFrame, region: str = 'PT') -> pd.DataFrame:
    """
    Function used to clean data.
    Args:
        initial_df [pd.DataFrame]: The initial dataframe that is going to be cleaned.
        region [str]: Region to be selected from the dataframe.
    Returns:
        [pd.DataFrame]: Data cleaned and filtered by region.
    """

    copy_initial_df = initial_df.copy()

    initial_columns = copy_initial_df.columns[0]

    new_columns = copy_initial_df.columns[0].split(',')

    copy_initial_df[new_columns] = copy_initial_df[initial_columns].str.split(',', expand=True)

    copy_initial_df = copy_initial_df.drop(columns=initial_columns)

    pivoted_df = copy_initial_df.melt(
                new_columns,
                var_name='year',
                value_name='value'
                )

    pivoted_df = pivoted_df.rename(columns={pivoted_df.columns[3]: 'region'})

    pivoted_df['year'] = pivoted_df['year'].astype('int')

    pivoted_df['value'] = (pivoted_df['value'].str.extract(r'(\d+\.?\d*)').astype(float))
    pivoted_df = pivoted_df.dropna(subset=['value'])

    pivoted_df = pivoted_df[pivoted_df['region']==region]

    return pivoted_df
