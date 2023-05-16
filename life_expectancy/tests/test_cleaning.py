"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy import clean_data
from life_expectancy.region import Region

def test_clean_data_tsv(eu_life_expectancy_raw_tsv, pt_life_expectancy_expected):

    """Test clean_data function"""
    clean_class = clean_data.CleanTSV()
    dataframe = clean_class.clean_data(eu_life_expectancy_raw_tsv, Region.PT) \
            .reset_index(drop = True)
    pd.testing.assert_frame_equal(dataframe, pt_life_expectancy_expected)

def test_clean_data_json(eu_life_expectancy_raw_json, pt_life_expectancy_expected):

    """Test clean_data function"""
    clean_class = clean_data.CleanJSON()
    dataframe = clean_class.clean_data(eu_life_expectancy_raw_json, Region.PT) \
            .reset_index(drop = True)
    pd.testing.assert_frame_equal(dataframe, pt_life_expectancy_expected)
