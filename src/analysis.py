import pandas as pd
import numpy as np


class DataAnalyser:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def get_summary_statistics(self):
        average_screen_time_hours = self.data["screen_time_hours"].mean()
        average_leisure_time_hours = self.data["leisure_screen_hours"].mean()
        average_sleep_time_hours = self.data["sleep_hours"].mean()
        average_work_time_hours = self.data["work_screen_hours"].mean()
        average_addiction_score = self.data["addiction_score"].mean()
        return {
            "average_screen_time_hours": average_screen_time_hours,
            "average_leisure_time_hours": average_leisure_time_hours,
            "average_sleep_time_hours": average_sleep_time_hours,
            "average_work_time_hours": average_work_time_hours,
            "average_addiction_score": average_addiction_score,
        }

    # -0.26
    def get_leisure_and_sleep_connection(self):
        correlation = self.data["leisure_screen_hours"].corr(self.data["sleep_hours"])
        return correlation

    def risk_level(self):
        counts = self.data["risk_level"].value_counts()
        return counts

    def age_group_analysis(self): ...

    def work_mode_analysis(self): ...

    def top_users_analysis(self, top_n=10): ...


if __name__ == "__main__":
    # Example usage
    data = pd.read_csv("data/processed/cleaned_screen_time.csv")
    analyser = DataAnalyser(data)
    for i in analyser.get_summary_statistics():
        print(f"{i}: {analyser.get_summary_statistics()[i]:.2f}")

    print(
        f"\n\nCorrelation between leisure screen hours and sleep hours: {analyser.get_leisure_and_sleep_connection():.2f}"
    )

    print("\n\nRisk Level Distribution:")
    print(analyser.risk_level())
