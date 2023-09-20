import main
import pandas as pd

data = pd.read_csv("forbes_2022_billionaires.csv")


def test_values():
    assert (main.mean1(data)) == 64.21068938807126
    assert (main.median1(data)) == 64.0
    assert (main.std1(data)) == 13.401258058138897


test_values()
