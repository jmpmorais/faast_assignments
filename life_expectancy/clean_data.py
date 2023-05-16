"""Script to clean data"""

from abc import ABC, abstractmethod
import pandas as pd
from life_expectancy.region import Region

class CleaningData(ABC):
    """Abstract class for cleaning data"""

    @abstractmethod
    def clean_data(self, df_data: pd.DataFrame, country: Region) -> pd.DataFrame:
        """Abstract method to clean the data"""

class CleanTSV(CleaningData):
    """Class to clean data coming from a .tsv file"""

    def clean_data(self, df_data: pd.DataFrame, country: Region) -> pd.DataFrame:
        """Cleans data"""
        df_copy = df_data.copy()

        # Splitting the name of the first column by ','
        new_cols = df_copy.columns[0].split(',')

        # Splitting the data of the first column and dropping the column with a bad format
        df_copy[new_cols] = df_copy[df_copy.columns[0]].str.split(',', expand=True)

        df_copy.drop(df_copy.columns[0], axis = 1, inplace = True)

        # Creating a table with unit,sex,age,region,year,value as columns
        df_melt = df_copy.melt(id_vars = new_cols, var_name = 'year', value_name = 'value')

        df_melt.rename(columns={'geo\\time': 'region'}, inplace=True)

        df_melt['year'] = df_melt['year'].astype(int)

        # allowing only floats as values to 'value' column
        df_melt['value'] = (df_melt['value'].str.extract(r'(\d+\.?\d*)').astype(float))

        df_melt.dropna(subset=['value'], inplace = True)

        # filtering by the desired country
        dataframe = df_melt[df_melt['region'] == country.value]

        return dataframe

class CleanJSON(CleaningData):
    """Class to clean data coming from a .json file"""

    def clean_data(self, df_data: pd.DataFrame, country: Region) -> pd.DataFrame:
        """Cleans data"""
        df_copy = df_data.copy()

        # Drop columns that are not in the list we want
        df_copy = df_copy.drop(columns='flag', axis = 1)
        df_copy = df_copy.drop(columns='flag_detail', axis = 1)

        # Rename columns
        df_copy = df_copy.rename(columns={'country': 'region', 'life_expectancy': 'value'})

        # Filter by region
        dataframe = df_copy[df_copy['region'] == country.value]

        return dataframe
