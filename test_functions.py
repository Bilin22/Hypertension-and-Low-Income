""" Tests to test function get_bigger_neighbourhood in functions.py """
from functions import get_bigger_neighbourhood as gbn
from functions import SAMPLE_DATA
from functions import SMALL_CITY_DATA


EMPTY_DATA = {}


ONE_ITEM_DATA = {
    "Big-Apple": {
        "id": 6,
        "hypertension": [100, 500, 190, 640, 330, 990],
        "total": 12345,
        "low_income": 2000,
    },
}


TWO_ITEMS_SAME = {
    "Big-Apple": {
        "id": 6,
        "hypertension": [100, 500, 190, 640, 330, 990],
        "total": 12345,
        "low_income": 2000,
    },
    "Super-Lemon": {
        "id": 7,
        "hypertension": [110, 560, 210, 690, 450, 1000],
        "total": 12345,
        "low_income": 2200,
    },
}


TWO_ITEMS_DIFFER = {
    "Super-Lemon": {
        "id": 7,
        "hypertension": [110, 560, 210, 690, 450, 1000],
        "total": 12345,
        "low_income": 2200,
    },
    "Honey-Bee": {
        "id": 8,
        "hypertension": [266, 530, 440, 990, 740, 2270],
        "total": 22222,
        "low_income": 5050,
    },
}


def test_empty_data() -> None:
    """Test that test_empty_data correctly returns the first neighbourhood
    when data input is an empty dict.
    """
    result = gbn(EMPTY_DATA, "Rexdale-Kipling", "Elms-Old Rexdale")
    assert result == "Rexdale-Kipling"


def test_one_item_data_1() -> None:
    """Test that test_one_item_data_1 correctly returns the first neighbourhood
    when it is found in the data, while the second is not.
    """
    result = gbn(ONE_ITEM_DATA, "Big-Apple", "big-apple")
    assert result == "Big-Apple"


def test_one_item_data_2() -> None:
    """Test that test_one_item_data_2 correctly returns second neighbourhood
    when it is found in the data, while the first is not.
    """
    result = gbn(ONE_ITEM_DATA, "big-apple", "Big-Apple")
    assert result == "Big-Apple"


def test_one_item_data_both_not_found() -> None:
    """Test that test_one_item_data_both_not_found
    correctly returns the first neighbourhood
    when both neighbourhood are not found in data.
    """
    result = gbn(ONE_ITEM_DATA, "bi-apple", "Big-aPple")
    assert result == "bi-apple"


def test_two_same_data_both_in() -> None:
    """Test that test_two_same_data_both_in
    correctly returns the first neighbourhood
    when both neighbourhood are found in data.
    """
    result = gbn(TWO_ITEMS_SAME, "Super-Lemon", "Big-Apple")
    assert result == "Super-Lemon"


def test_two_same_data_1_not_found() -> None:
    """Test that test_two_same_data_1_not_found
    correctly returns the second neighbourhood
    when the first neighbourhood is not found in data.
    """
    result = gbn(TWO_ITEMS_SAME, "Super-LemoN", "Big-Apple")
    assert result == "Big-Apple"


def test_two_same_data_2_not_found() -> None:
    """Test that test_two_same_data_2_not_found
    correctly returns the first neighbourhood
    when the second neighbourhood is not found in data.
    """
    result = gbn(TWO_ITEMS_SAME, "Super-Lemon", "big-ApplE")
    assert result == "Super-Lemon"


def test_two_same_data_both_not_found() -> None:
    """Test that test_two_same_data_both_not_found
    correctly returns the first neighbourhood
    when the both neighbourhoods are not found in data.
    """
    result = gbn(TWO_ITEMS_SAME, "Super-LemoN", "big-ApplE")
    assert result == "Super-LemoN"


def test_two_differ_1_large() -> None:
    """Test that test_two_differ_1_large
    correctly returns the first neighbourhood
    when the first neighbourhood is larger.
    """
    result = gbn(TWO_ITEMS_DIFFER, "Honey-Bee", "Super-Lemon")
    assert result == "Honey-Bee"


def test_two_differ_2_large() -> None:
    """Test that test_two_differ_2_large
    correctly returns the second neighbourhood
    when the second neighbourhood is larger.
    """
    result = gbn(TWO_ITEMS_DIFFER, "Super-Lemon", "Honey-Bee")
    assert result == "Honey-Bee"


def test_two_differ_1_not_found() -> None:
    """Test that test_two_differ_1_not_found
    correctly returns the second neighbourhood
    when the first neighbourhood is not found.
    """
    result = gbn(TWO_ITEMS_DIFFER, "SuPer-Lemon", "Honey-Bee")
    assert result == "Honey-Bee"


def test_two_differ_2_not_found() -> None:
    """Test that test_two_differ_2_not_found
    correctly returns the first neighbourhood
    when the second neighbourhood is not found.
    """
    result = gbn(TWO_ITEMS_DIFFER, "Super-Lemon", "HOnEy-Bee")
    assert result == "Super-Lemon"


def test_two_differ_both_not_found() -> None:
    """Test that test_two_differ_both_not_found
    correctly returns the first neighbourhood
    when the both neighbourhoods are not found.
    """
    result = gbn(TWO_ITEMS_DIFFER, "SuPer-LeMon", "HOnEy-Bee")
    assert result == "SuPer-LeMon"


def test_first_bigger() -> None:
    """Test that test_first_bigger correctly returns the first neighbourhood
    when its population is strictly greater than the population of the second
    neighbourhood.
    """
    result = gbn(SAMPLE_DATA, "Rexdale-Kipling", "Elms-Old Rexdale")
    assert result == "Rexdale-Kipling"


def test_second_bigger() -> None:
    """Test that test_second_bigger correctly returns the second neighbourhood
    when its population is strictly greater than the population of the first
    neighbourhood.
    """
    result = gbn(SAMPLE_DATA, "Elms-Old Rexdale", "Rexdale-Kipling")
    assert result == "Rexdale-Kipling"

def test_same_1() -> None:
    """Test that test_same_1 correctly returns the first neighbourhood
    when both neighbourhood have same population.
    """
    result = gbn(SMALL_CITY_DATA, "Big-Apple", "Super-Lemon")
    assert result == "Big-Apple"


def test_same_2() -> None:
    """Test that test_same_2 correctly returns the first neighbourhood
    when both neighbourhood have same population.
    """
    result = gbn(SMALL_CITY_DATA, "Super-Lemon", "Big-Apple")
    assert result == "Super-Lemon"


def test_first_not_found() -> None:
    """ Test that test_first_not_found correctly returns the
    second neighbourhood when the first neighbourhood doesn't
    in data.
    """
    result = gbn(SAMPLE_DATA, "ELms-Old Rexdale", "Rexdale-Kipling")
    assert result == "Rexdale-Kipling"
    

def test_first_not_found_2() -> None:
    """ Test that test_first_not_found_2 correctly returns the
    second neighbourhood when the first neighbourhood doesn't
    in data.
    """
    result = gbn(SAMPLE_DATA, "RExdale-Kipling", "Elms-Old Rexdale")
    assert result == "Elms-Old Rexdale"


def test_second_not_found() -> None:
    """ Test that test_second_not_found correctly returns the
    first neighbourhood when the second neighbourhood doesn't
    in data.
    """
    result = gbn(SAMPLE_DATA, "Elms-Old Rexdale", "RexdAle-Kipling")
    assert result == "Elms-Old Rexdale"


def test_both_not_found() -> None:
    """ Test that test_both_not_found correctly returns the
    first neighbourhood when both neighbourhoods are not found
    in data.
    """
    result = gbn(SAMPLE_DATA, "REXdale-Kipling", "Elms-OlD Rexdale")
    assert result == "REXdale-Kipling"


def test_2_with_comma() -> None:
    """ Test that test_2_with_comma correctly returns the
    first neighbourhood when the second neighbourhood doesn't
    in data.
    """
    result = gbn(SAMPLE_DATA, "Elms-Old Rexdale", "Rexda,le-Kipling")
    assert result == "Elms-Old Rexdale"


def test_2_with_space() -> None:
    """ Test that test_2_with_space correctly returns the
    first neighbourhood when the second neighbourhood doesn't
    in data.
    """
    result = gbn(SAMPLE_DATA, "Elms-Old Rexdale", "Rexdale-Kip ling")
    assert result == "Elms-Old Rexdale"


def test_2_with_less_char() -> None:
    """ Test that test_2_with_less_char correctly returns the
    first neighbourhood when the second neighbourhood doesn't
    in data.
    """
    result = gbn(SAMPLE_DATA, "Elms-Old Rexdale", "R")
    assert result == "Elms-Old Rexdale"


def test_2_with_number() -> None:
    """ Test that test_2_with_number correctly returns the
    first neighbourhood when the second neighbourhood doesn't
    in data.
    """
    result = gbn(SAMPLE_DATA, "Elms-Old Rexdale", "Rexdale-Kip1li1ng11")
    assert result == "Elms-Old Rexdale"

def test_2_with_more_char() -> None:
    """ Test that test_2_with_comma correctly returns the
    first neighbourhood when the second neighbourhood doesn't
    in data.
    """
    result = gbn(SAMPLE_DATA, "Elms-Old Rexdale", "Rexdale-Kiplinggg")
    assert result == "Elms-Old Rexdale"


if __name__ == '__main__':
    import pytest
    pytest.main(['test_functions.py'])
