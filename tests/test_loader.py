import pandas as pd
from src.loader import DataLoader


def test_load_data_returns_dataframe():
    loader = DataLoader("data/raw/ScreenTimeMentalWellness.csv")
    data = loader.load_data

    assert isinstance(data, pd.DataFrame)


def test_load_data_is_not_empty():
    loader = DataLoader("data/raw/ScreenTimeMentalWellness.csv")
    data = loader.load_data

    assert not data.empty
