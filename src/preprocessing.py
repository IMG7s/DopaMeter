from src.loader import DataLoader
import pandas as pd
from typing import Final


class DataPreprocessor:
    def __init__(self, data_loader: DataLoader):
        self.data_loader: Final[DataLoader] = data_loader

    def preprocess_data(self) -> pd.DataFrame:
        data: pd.DataFrame = self.data_loader.load_data

        # Clean columns
        if data.empty:
            print("No data to preprocess.")
            return data

        data.columns = (
            data.columns.str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace(r"[^\w]", "", regex=True)
        )

        data = data.dropna(axis=1, how="all")  # type: ignore

        columns_to_keep = [
            col for col in data.columns if not col.lower().startswith("unnamed")
        ]
        data = data[columns_to_keep]

        # Add new columns
        data["leisure_ratio"] = (
            data["leisure_screen_hours"] / data["screen_time_hours"]
        ).round(2)
        data["work_ratio"] = (
            data["work_screen_hours"] / data["screen_time_hours"]
        ).round(2)
        data["sleep_deficit"] = (8 - data["sleep_hours"]).round(2)
        data["addiction_score"] = (
            data["leisure_screen_hours"] / data["sleep_hours"]
        ).round(2)

        return data


if __name__ == "__main__":
    data_loader = DataLoader(file_path="data/raw/ScreenTimeMentalWellness.csv")
    preprocessor = DataPreprocessor(data_loader)
    data = preprocessor.preprocess_data()
    data.to_csv("data/processed/cleaned_screen_time.csv", index=False)
