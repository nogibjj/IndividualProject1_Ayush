import polars as pl
from lib import add_numbers, subtract_numbers

data = pl.read_csv("forbes_2022_billionaires.csv")


def stats_mean(df):
    return df["age"].mean()


def stats_median(df):
    return df["age"].median()


def stats_std(df):
    return df["age"].std()



