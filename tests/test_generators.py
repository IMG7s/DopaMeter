from src.loader import DataLoader
from src.preprocessing import DataPreprocessor
from src.generators import iterate_users, iterate_high_risk_users


def get_preprocessed_data():
    loader = DataLoader("data/raw/ScreenTimeMentalWellness.csv")
    preprocessor = DataPreprocessor(loader)
    return preprocessor.preprocess_data()


def test_iterate_users_yields_data():
    data = get_preprocessed_data()

    first_user = next(iterate_users(data))

    assert isinstance(first_user, dict)
    assert "user_id" in first_user


def test_iterate_high_risk_users_yields_only_high_risk():
    data = get_preprocessed_data()

    high_risk_user = next(iterate_high_risk_users(data))

    assert isinstance(high_risk_user, dict)
    assert high_risk_user["risk_level"] == "high"
