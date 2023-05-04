"""Tests for the region enum"""
import numpy as np

from life_expectancy.region import Region

def test_regions_list(all_regions_expected):
    """Test for the region listing function"""

    region_list = Region.list_countries()
    np.testing.assert_array_equal(
        region_list, all_regions_expected
    )