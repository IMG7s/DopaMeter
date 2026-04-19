import pandas as pd
from typing import Final


class DataLoader:
    def __init__(self, file_path: str):
        self.file_path: Final[str] = file_path

    @property
    def load_data(self) -> pd.DataFrame:
        try:
            data = pd.read_csv(self.file_path)
            return data
        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}")
            return pd.DataFrame()  # Return emptu DataFrame if file is not found
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            return pd.DataFrame()  # Return empty DataFrame if any other error

    def __str__(self) -> str:
        return f"DataLoader(file_path='{self.file_path}')"
