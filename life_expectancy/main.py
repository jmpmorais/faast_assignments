"""
Script to load, clean and save data
"""

import argparse
import pathlib
import pandas as pd
from life_expectancy.clean_data import clean_data
from life_expectancy.load_data import load_data, save_data



PARENT_PATH = pathlib.Path(__file__).parent
FILE_PATH = PARENT_PATH / 'data'
INPUT_FILE_NAME = 'eu_life_expectancy_raw.tsv'
OUTPUT_FILE_NAME = 'pt_life_expectancy.csv'
INPUT_FILE_PATH = FILE_PATH / INPUT_FILE_NAME
OUTPUT_FILE_PATH = FILE_PATH / OUTPUT_FILE_NAME


def main(country: str = 'PT')-> pd.DataFrame:
    """
        Function that loads, cleans and saves data
    """
    data_df = load_data(INPUT_FILE_PATH)
    clean_df = clean_data(initial_df = data_df, region = country)
    save_data(dataframe = clean_df, file_path = OUTPUT_FILE_PATH)
    return clean_df

if __name__ == "__main__": #pragma: no cover

    parser = argparse.ArgumentParser()
    parser.add_argument('country')
    args = parser.parse_args()
    main(args.country)
