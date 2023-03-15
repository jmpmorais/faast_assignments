""" Cleaning Data """
import pathlib
import argparse
import pandas as pd

life_path = pathlib.Path(__file__).parent
data_path = life_path / 'data'
FILE_NAME = 'eu_life_expectancy_raw.tsv'


def load_data(file_name: str)-> pd.DataFrame:
    """        
    Function to load data from data folder, given a file_name    
    """
    df_expectancy = pd.read_csv(data_path / file_name, sep = '\t')

    return df_expectancy


def clean_data(initial_df: pd.DataFrame, region: str = 'PT') -> pd.DataFrame:
    """        
    Function to clean data    
    """

        # transform string into list
    initial_columns = initial_df.columns[0]

    new_columns = initial_df.columns[0].split(',')

        # split columns and add to df
    initial_df[new_columns] = initial_df[initial_columns].str.split(',', expand=True)

        # drop initial columns
    initial_df = initial_df.drop(columns=initial_columns)


        # unpivots the table
    pivoted_df = pd.melt(
                initial_df,
                new_columns,
                var_name='year',
                value_name='value'
                )


        # rename the column
    pivoted_df = pivoted_df.rename(columns={pivoted_df.columns[3]: 'region'})


        # year as an int
    pivoted_df['year'] = pivoted_df['year'].astype('int')

        #value as a float and drop NaN
    pivoted_df['value'] = (pivoted_df['value'].str.extract(r'(\d+\.?\d*)').astype(float))
    pivoted_df = pivoted_df.dropna(subset=['value'])


        # Get only PT region
    pivoted_df = pivoted_df[pivoted_df['region']==region]

    return pivoted_df

def save_data(df_country: pd.DataFrame, file_name: str, file_path: pathlib.Path) -> None:
    """        
    Function to save data, given a file_name and a path    
    """
    df_country.to_csv(file_path / file_name, index = False)

def main(region: str) -> None:
    """        
    Function that loads, cleans and saves data    
    """
    data_df = load_data(FILE_NAME)
    clean_df = clean_data(initial_df = data_df, region = region)
    save_data(df_country = clean_df, file_name = 'pt_life_expectancy.csv', file_path = data_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('region')
    args = parser.parse_args()
    main(args.region)
