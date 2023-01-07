"""CSC108: Fall 2022 -- Assignment 3: Hypertension and Low Income

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2022 Jacqueline Smith and David Liu
"""
from typing import TextIO
import statistics  # Note that this requires Python 3.10

ID = "id"
HT_KEY = "hypertension"
TOTAL = "total"
LOW_INCOME = "low_income"

# Indexes in the inner lists of hypertension data in CityData
# HT is an abbreviation of hypertension, NBH is an abbreviation of neighbourhood
HT_20_44 = 0
NBH_20_44 = 1
HT_45_64 = 2
NBH_45_64 = 3
HT_65_UP = 4
NBH_65_UP = 5

# columns in input files
ID_COL = 0
NBH_NAME_COL = 1
POP_COL = 2
LI_POP_COL = 3

SAMPLE_DATA = {
    "West Humber-Clairville": {
        "id": 1,
        "hypertension": [703, 13291, 3741, 9663, 3959, 5176],
        "total": 33230,
        "low_income": 5950,
    },
    "Mount Olive-Silverstone-Jamestown": {
        "id": 2,
        "hypertension": [789, 12906, 3578, 8815, 2927, 3902],
        "total": 32940,
        "low_income": 9690,
    },
    "Thistletown-Beaumond Heights": {
        "id": 3,
        "hypertension": [220, 3631, 1047, 2829, 1349, 1767],
        "total": 10365,
        "low_income": 2005,
    },
    "Rexdale-Kipling": {
        "id": 4,
        "hypertension": [201, 3669, 1134, 3229, 1393, 1854],
        "total": 10540,
        "low_income": 2140,
    },
    "Elms-Old Rexdale": {
        "id": 5,
        "hypertension": [176, 3353, 1040, 2842, 948, 1322],
        "total": 9460,
        "low_income": 2315,
    },
}

SMALL_CITY_DATA = {
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
    "Honey-Bee": {
        "id": 8,
        "hypertension": [266, 530, 440, 990, 740, 2270],
        "total": 22222,
        "low_income": 5050,
    },
}


# Task 1
def get_hypertension_data(d: dict, HT_file: TextIO) -> None:
    """
    Modify d so that it contains data from HT_file.
    """
    lst = []
    HT_file.readline()
    line = HT_file.readline().strip()
    while line != '':
        lst.append(line.split(','))
        line = HT_file.readline().strip()
    for sublst in lst:
        if sublst[NBH_NAME_COL] not in d:
            d[sublst[NBH_NAME_COL]] = {ID: int(sublst[ID_COL])}
        else:
            d[sublst[NBH_NAME_COL]][ID] = int(sublst[ID_COL])
        d[sublst[NBH_NAME_COL]][HT_KEY] = []
    for sub in lst:
        for data in sub[NBH_NAME_COL + 1:]:
            d[sub[NBH_NAME_COL]][HT_KEY].append(int(data))
#        for i in range(len(sub)):
#            if i not in (ID_COL, NBH_NAME_COL):
#                d[sub[NBH_NAME_COL]][HT_KEY].append(int(sub[i]))


def get_low_income_data(d: dict, LI_file: TextIO) -> None:
    """
    Modify d so that it contains data from LI_file.
    """
    lst = []
    LI_file.readline()
    line = LI_file.readline().strip()
    while line != '':
        lst.append(line.split(','))
        line = LI_file.readline().strip()
    for sublst in lst:
        if sublst[NBH_NAME_COL] not in d:
            d[sublst[NBH_NAME_COL]] = {ID: int(sublst[ID_COL])}
        else:
            d[sublst[NBH_NAME_COL]][ID] = int(sublst[ID_COL])
        d[sublst[NBH_NAME_COL]][TOTAL] = int(sublst[POP_COL])
        d[sublst[NBH_NAME_COL]][LOW_INCOME] = int(sublst[LI_POP_COL])


# Task 2
def get_bigger_neighbourhood(data: 'CityData', name1: str, name2: str) -> str:
    """
    Return the name of neighbourhood (name1 or name2) with higher population,
    return name1 if name1 NBH have same population as name2 NBH.

    >>> d = SAMPLE_DATA
    >>> get_bigger_neighbourhood(d, "Elms-Old Rexdale", "West Humber-Clairville")
    'West Humber-Clairville'
    >>> data = SMALL_CITY_DATA
    >>> get_bigger_neighbourhood(data, "Super-Lemon", "Big-Apple")
    'Super-Lemon'
    """
    pop_1 = 0
    pop_2 = 0
    if name1 in data:
        pop_1 = data[name1][TOTAL]
    if name2 in data:
        pop_2 = data[name2][TOTAL]
    if pop_1 >= pop_2:
        return name1
    else:
        return name2


# helper for get_high_hypertension_rate
def get_hypertension_rate(data: 'CityData') -> dict[str, float]:
    """
    Return a dict contains the hypertension rate in data.

    >>> d = SAMPLE_DATA
    >>> get_hypertension_rate(d)['Thistletown-Beaumond Heights']
    0.31797739151574084
    >>> data = SMALL_CITY_DATA
    >>> get_hypertension_rate(data)['Big-Apple']
    0.29107981220657275
    """
    result = {}
    for name in data:
        HT_sum = (data[name][HT_KEY][HT_20_44]
                  + data[name][HT_KEY][HT_45_64]
                  + data[name][HT_KEY][HT_65_UP])
        POP_sum = (data[name][HT_KEY][NBH_20_44]
                   + data[name][HT_KEY][NBH_45_64]
                   + data[name][HT_KEY][NBH_65_UP])
        result[name] = HT_sum / POP_sum
    return result


# helper for getting low_income_rate
def get_low_income_rate(data: 'CityData') -> dict[str, float]:
    """
    Return a dict contains the low income rate in data.

    >>> d = SAMPLE_DATA
    >>> get_low_income_rate(d)['Thistletown-Beaumond Heights']
    0.19343945972021226
    >>> get_low_income_rate(d)['Elms-Old Rexdale']
    0.24471458773784355
    """
    result = {}
    for name in data:
        result[name] = (data[name][LOW_INCOME]) /\
                       ((data)[name][TOTAL])
    return result


def get_high_hypertension_rate(data: 'CityData',
                               threshold: float) -> list[tuple[str, float]]:
    """
    Return a list of tuple representing all neighbourhoods
    in data with a hypertension rate
    greater than or equal to the threshold.

    Precondition: 0.0 <= threshold <= 1.0

    >>> d = SAMPLE_DATA
    >>> r = get_high_hypertension_rate(d, 0.3)
    >>> r[0]
    ('Thistletown-Beaumond Heights', 0.31797739151574084)
    >>> r[1]
    ('Rexdale-Kipling', 0.3117001828153565)
    >>> data = SMALL_CITY_DATA
    >>> get_high_hypertension_rate(data, 0.33)
    [('Super-Lemon', 0.3422222222222222), ('Honey-Bee', 0.38153034300791555)]
    """
    result = []
    hyper_rate_d = get_hypertension_rate(data)
    for key, value in hyper_rate_d.items():
        if value >= threshold:
            result.append((key, value))
    return result


def get_ht_to_low_income_ratios(data: 'CityData') -> dict[str, float]:
    """
    Return a dictionary from data, of which the keys are the same
    as in date, the values are the ratio of hypertension rate
    to the low income rate for that neighbourhood.
    >>> d = SAMPLE_DATA
    >>> get_ht_to_low_income_ratios(d)['West Humber-Clairville']
    1.6683148168616895
    >>> get_ht_to_low_income_ratios(d)['Mount Olive-Silverstone-Jamestown']
    0.9676885451091314
    """
    HT_d = get_hypertension_rate(data)
    LI_d = get_low_income_rate(data)
    result = {}
    for NBH in data:
        result[NBH] = (HT_d[NBH]) / (LI_d[NBH])
    return result


# This function is provided for use in Tasks 3 and 4. You should not change it.
def get_age_standardized_ht_rate(ndata: 'CityData', name: str) -> float:
    """Return the age standardized hypertension rate from the neighbourhood in
    ndata matching the given name.

    Precondition: name is in ndata

    >>> get_age_standardized_ht_rate(SAMPLE_DATA, 'Elms-Old Rexdale')
    24.44627521389894
    >>> get_age_standardized_ht_rate(SAMPLE_DATA, 'Rexdale-Kipling')
    24.72562462246556
    """
    rates = calculate_ht_rates_by_age_group(ndata, name)

    # These rates are normalized for only 20+ ages, using the census data
    # that our datasets are based on.
    canada_20_44 = 11_199_830 / 19_735_665  # Number of 20-44 / Number of 20+
    canada_45_64 = 5_365_865 / 19_735_665  # Number of 45-64 / Number of 20+
    canada_65_plus = 3_169_970 / 19_735_665  # Number of 65+ / Number of 20+

    return (rates[0] * canada_20_44
            + rates[1] * canada_45_64
            + rates[2] * canada_65_plus)


def calculate_ht_rates_by_age_group(data: 'CityData',
                                    name: str) -> tuple[float, float, float]:
    """
    Return a tuple of 3 values, representing the hypertension
    rate for each of the three age groups in name from data as
    a percentage.

    >>> d = SAMPLE_DATA
    >>> calculate_ht_rates_by_age_group(d, 'Elms-Old Rexdale')[0:2]
    (5.24903071875932, 36.593947923997185)
    >>> calculate_ht_rates_by_age_group(d, 'Elms-Old Rexdale')[2]
    71.70953101361573
    """
    result = ()
    result += (data[name][HT_KEY][HT_20_44]
               / data[name][HT_KEY][NBH_20_44] * 100, )
    result += (data[name][HT_KEY][HT_45_64]
               / data[name][HT_KEY][NBH_45_64] * 100, )
    result += (data[name][HT_KEY][HT_65_UP]
               / data[name][HT_KEY][NBH_65_UP] * 100, )
    return result


def get_stats_summary(data: 'CityData') -> float:
    """
    Return the correlation between
    age standardized hypertension rates and
    low income rates across all neighbourhoods in data.

    >>> d = SAMPLE_DATA
    >>> get_stats_summary(d)
    0.28509539188554994
    >>> data = SMALL_CITY_DATA
    >>> get_stats_summary(data)
    0.9872052330581085
    """
    LI_dict = get_low_income_rate(data)
    HT_values = []
    LI_values = []
    for NBH in data:
        HT_values.append(get_age_standardized_ht_rate(data, NBH))
        LI_values.append(LI_dict[NBH])
    return statistics.correlation(HT_values, LI_values)
# there's no order in dict!


def order_by_ht_rate(data: 'CityData') -> list[str]:
    """
    Return a list of the names
    of the neighbourhoods in data, ordered from
    lowest to highest age-standardized hypertension rate.

    >>> d = SAMPLE_DATA
    >>> order_by_ht_rate(d)[1]
    'Rexdale-Kipling'
    >>> order_by_ht_rate(d)[2:4]
    ['Thistletown-Beaumond Heights', 'West Humber-Clairville']
    """
    HT_dict = {}
    for NBH in data:
        HT_dict[NBH] = get_age_standardized_ht_rate(data, NBH)
    HT_lst = list(HT_dict.values())
    sorted_lst = sorted(HT_lst)
    result = []
    for i in sorted_lst:
        for key in HT_dict:
            if HT_dict[key] == i:
                result.append(key)
    return result

   
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Using the small data files
    small_data = {}

    # Add hypertension data
    ht_file = open("hypertension_data_small.csv")
    get_hypertension_data(small_data, ht_file)
    ht_file.close()

    # Add low income data
    li_file = open("low_income_small.csv")
    get_low_income_data(small_data, li_file)
    li_file.close()

    # Created dictionary should be the same as SAMPLE_DATA
    print(small_data == SAMPLE_DATA)
