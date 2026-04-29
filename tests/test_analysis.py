import pandas as pd
from src.loader import DataLoader
from src.preprocessing import DataPreprocessor
from src.analysis import DataAnalyser


def get_preprocessed_data():
    loader = DataLoader("data/raw/ScreenTimeMentalWellness.csv")
    preprocessor = DataPreprocessor(loader)
    return preprocessor.preprocess_data()


def test_summary_statistics_returns_dict():
    data = get_preprocessed_data()
    analyser = DataAnalyser(data)

    result = analyser.get_summary_statistics()

    assert isinstance(result, dict)


def test_summary_statistics_contains_expected_keys():
    data = get_preprocessed_data()
    analyser = DataAnalyser(data)

    result = analyser.get_summary_statistics()

    expected_keys = {
        "average_screen_time_hours",
        "average_leisure_time_hours",
        "average_sleep_time_hours",
        "average_work_time_hours",
        "average_addiction_score",
    }

    assert expected_keys.issubset(result.keys())


def test_leisure_sleep_connection_returns_float():
    data = get_preprocessed_data()
    analyser = DataAnalyser(data)

    correlation = analyser.get_leisure_and_sleep_connection()

    assert isinstance(correlation, float)


def test_risk_level_distribution_is_not_empty():
    data = get_preprocessed_data()
    analyser = DataAnalyser(data)

    risk = analyser.risk_level()

    assert not risk.empty


def test_top_users_analysis_respects_limit():
    data = get_preprocessed_data()
    analyser = DataAnalyser(data)

    result = analyser.top_users_analysis(top_n=5)

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 5


def test_age_group_analysis_returns_dataframe():
    data = get_preprocessed_data()
    analyser = DataAnalyser(data)

    result = analyser.age_group_analysis()

    assert isinstance(result, pd.DataFrame)


def test_work_mode_analysis_returns_dataframe():
    data = get_preprocessed_data()
    analyser = DataAnalyser(data)

    result = analyser.work_mode_analysis()

    assert isinstance(result, pd.DataFrame)
