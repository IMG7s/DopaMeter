from src.loader import DataLoader
from src.preprocessing import DataPreprocessor


def test_preprocessing_adds_required_columns():
    loader = DataLoader("data/raw/ScreenTimeMentalWellness.csv")
    preprocessor = DataPreprocessor(loader)
    data = preprocessor.preprocess_data()

    required_columns = {
        "leisure_ratio",
        "work_ratio",
        "sleep_deficit",
        "addiction_score",
        "risk_level",
        "age_group",
    }

    assert required_columns.issubset(set(data.columns))


def test_preprocessing_removes_unnamed_columns():
    loader = DataLoader("data/raw/ScreenTimeMentalWellness.csv")
    preprocessor = DataPreprocessor(loader)
    data = preprocessor.preprocess_data()

    unnamed_columns = [col for col in data.columns if col.lower().startswith("unnamed")]
    assert len(unnamed_columns) == 0
