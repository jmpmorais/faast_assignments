"""Pytest configuration file"""
import pandas as pd
import pytest

from . import FIXTURES_DIR, OUTPUT_DIR

LIST_ALL_COUNTRIES = ["AL","AM","AT","AZ","BE","BG","BY","CH","CY","CZ","DE","DE_TOT",
                    "DK","EE","EL","ES","FI","FR","FX","GE","HR","HU","IE","IS","IT",
                    "LI","LT","LU","LV","MD","ME","MK","MT","NL","NO","PL","PT","RO",
                    "RS","RU","SE","SI","SK","SM","TR","UA","UK","XK"]

@pytest.fixture(autouse=True)
def run_before_and_after_tests() -> None:
    """Fixture to execute commands before and after a test is run"""
    # Setup: fill with any logic you want

    yield # this is where the testing happens

    # Teardown : fill with any logic you want
    file_path = OUTPUT_DIR / "pt_life_expectancy.csv"
    file_path.unlink(missing_ok=True)

@pytest.fixture(scope="session")
def eu_life_expectancy_raw_tsv() -> pd.DataFrame:
    """Fixture to load the raw life expectancy data tsv"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw.tsv", delimiter='\t')

@pytest.fixture(scope="session")
def eu_life_expectancy_raw_json() -> pd.DataFrame:
    """Fixture to load the raw eurostat file (json)"""
    return pd.read_json(FIXTURES_DIR / "eurostat_life_expect.json")

@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output from csv"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")

@pytest.fixture(scope="session")
def eurostat_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output from json"""
    return pd.read_csv(FIXTURES_DIR / "eurostat_life_expectancy_expected.csv")

@pytest.fixture(scope="session")
def all_regions_expected() -> pd.DataFrame:
    """Fixture to return the list of all countries in enum"""
    return LIST_ALL_COUNTRIES
