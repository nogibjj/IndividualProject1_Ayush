import pandas as pd
from lib import stats_mean, stats_median, stats_std

data = pd.read_csv("forbes_2022_billionaires.csv")


def mean1(df):
    return stats_mean(data)


def median1(df):
    return stats_median(data)


def std1(df):
    return stats_std(data)


print("mean =", mean1(data))
print("median =", median1(data))
print("Standard_deviation =", std1(data))
