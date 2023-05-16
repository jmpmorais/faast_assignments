"""Tests for the loading and saving module"""
import pathlib
from unittest import mock
import pandas as pd
from life_expectancy import load_data
from . import FIXTURES_DIR, OUTPUT_DIR

PARENT_PATH = pathlib.Path(__file__).parent
DATA_PATH = PARENT_PATH.parent / 'data'
EXP_FILE_NAME = 'eu_life_expectancy_raw.tsv'
PT_FILE_NAME = 'pt_life_expectancy.csv'
EXP_FILE_PATH = DATA_PATH / EXP_FILE_NAME
PT_FILE_PATH = DATA_PATH / PT_FILE_NAME

def test_load_data_tsv(eu_life_expectancy_raw_tsv):
    """Test load_data function"""
    load_class = load_data.LoadTSV()
    dataframe = load_class.load_data(FIXTURES_DIR / 'eu_life_expectancy_raw.tsv') \
            .reset_index(drop=True)
    pd.testing.assert_frame_equal(dataframe, eu_life_expectancy_raw_tsv)

def test_load_data_json(eu_life_expectancy_raw_json):
    """Test load_data function"""
    load_class = load_data.LoadJSON()
    dataframe = load_class.load_data(FIXTURES_DIR / 'eurostat_life_expect.zip') \
            .reset_index(drop=True)
    pd.testing.assert_frame_equal(dataframe, eu_life_expectancy_raw_json)

@mock.patch("life_expectancy.load_data.pd.DataFrame.to_csv")
def test_save_data(mock_to_csv, pt_life_expectancy_expected):

    """Test save_data function"""
    load_data.save_data(pt_life_expectancy_expected, OUTPUT_DIR / 'pt_life_expectancy.csv')
    mock_to_csv.assert_called_with(OUTPUT_DIR / 'pt_life_expectancy.csv', index=False)
