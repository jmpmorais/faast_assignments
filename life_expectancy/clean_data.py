"""Script to clean data"""

from abc import ABC, abstractmethod
import pandas as pd
from life_expectancy.region import Region

class CleaningData(ABC):
    """Abstract class for cleaning data"""

    @abstractmethod
    def clean_data(self, initial_df: pd.DataFrame, region: Region) -> pd.DataFrame:
        """Abstract method to clean the data"""

class CleanTSV(CleaningData):
    """Class to clean data coming from a .tsv file"""

    def clean_data(self, initial_df: pd.DataFrame, region: Region) -> pd.DataFrame:
        """Cleans data"""

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

        pivoted_df = pivoted_df[pivoted_df['region']==region.value]

        return pivoted_df

class CleanJSON(CleaningData):
    """Class to clean data coming from a .json file"""

    def clean_data(self, initial_df: pd.DataFrame, region: Region) -> pd.DataFrame:
        """Cleans data"""

        copy_initial_df = initial_df.copy()

        # Drop columns that are not in the list we want
        copy_initial_df = copy_initial_df.drop(columns='flag', axis = 1)
        copy_initial_df = copy_initial_df.drop(columns='flag_detail', axis = 1)

        # Rename columns
        copy_initial_df = copy_initial_df.rename(
                columns={'country':'region', 'life_expectancy':'value'}
                )

        # Filter by region
        final_df = copy_initial_df[copy_initial_df['region'] == region.value]

        return final_df
