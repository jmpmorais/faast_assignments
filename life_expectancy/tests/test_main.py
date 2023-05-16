"""Tests for the main module"""
import pandas as pd
from life_expectancy.main import main
from life_expectancy.region import Region
from . import OUTPUT_DIR, FIXTURES_DIR

EU_CSV_PATH = OUTPUT_DIR / 'eu_life_expectancy_raw.tsv'
EU_ZIP_PATH = OUTPUT_DIR / 'eurostat_life_expect.zip'
PT_EXPECTED_PATH = OUTPUT_DIR / 'pt_life_expectancy_expected.csv'
EUROSTAT_CSV_PATH = FIXTURES_DIR / "eurostat_life_expectancy_expected.csv"


def test_main_csv(pt_life_expectancy_expected):
    """Run the main function and compare the output to the expected output"""
    pt_life_expectancy_actual = main(EU_CSV_PATH, PT_EXPECTED_PATH, Region.PT) \
            .reset_index(drop = True)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )

def test_main_json(eurostat_life_expectancy_expected):
    """Run the main function and compare the output to the expected output"""

    pt_life_expectancy_actual = main(EU_ZIP_PATH, EUROSTAT_CSV_PATH, Region.PT) \
            .reset_index(drop = True)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, eurostat_life_expectancy_expected
    )
