import main
import pandas as pd

data = pd.read_csv("forbes_2022_billionaires.csv")


def test_values():
    assert (main.stats_mean(data)) == 64.21068938807126
    assert (main.stats_median(data)) == 64.0
    assert (main.stats_std(data)) == 13.401258058138897


test_values()
