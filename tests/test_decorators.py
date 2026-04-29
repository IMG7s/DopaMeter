import pandas as pd
import pytest
from src.decorators import validate_columns


class DummyAnalyzer:
    def __init__(self, data):
        self.data = data

    @validate_columns(["required_column"])
    def test_method(self):
        return "ok"


def test_validate_columns_raises_error_when_column_missing():
    data = pd.DataFrame({"other_column": [1, 2, 3]})
    analyzer = DummyAnalyzer(data)

    with pytest.raises(ValueError):
        analyzer.test_method()


def test_validate_columns_passes_when_column_exists():
    data = pd.DataFrame({"required_column": [1, 2, 3]})
    analyzer = DummyAnalyzer(data)

    assert analyzer.test_method() == "ok"
