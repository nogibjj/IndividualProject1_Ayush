import polars as pl
from lib import stats_mean, stats_median, stats_std

data = pl.read_csv("forbes_2022_billionaires.csv")


print("mean =", stats_mean(data))
print("median =", stats_median(data))
print("Standard_deviation =", stats_std(data))
