import pandas as pd
import numpy as np
from src.generators import iterate_users, iterate_high_risk_users
from src.decorators import cache_results, validate_columns


class DataAnalyser:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    @cache_results
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

    @validate_columns(["screen_time_hours", "sleep_hours"])
    def get_leisure_and_sleep_connection(self):
        correlation = self.data["leisure_screen_hours"].corr(self.data["sleep_hours"])
        return correlation

    @validate_columns(["risk_level"])
    def risk_level(self):
        counts = self.data["risk_level"].value_counts()
        return counts

    @cache_results
    @validate_columns(["age_group"])
    def age_group_analysis(self):
        result = (
            self.data.groupby("age_group", observed=False)[
                [
                    "screen_time_hours",
                    "sleep_hours",
                    "addiction_score",
                    "leisure_screen_hours",
                ]
            ]
            .mean()
            .round(2)
        )
        return result

    @cache_results
    @validate_columns(["work_mode"])
    def work_mode_analysis(self):
        result = (
            self.data.groupby("work_mode")[
                [
                    "screen_time_hours",
                    "leisure_screen_hours",
                    "sleep_hours",
                    "addiction_score",
                ]
            ]
            .mean()
            .round(2)
        )
        return result

    def top_users_analysis(self, top_n=10):
        result = self.data.sort_values(by="addiction_score", ascending=False).head(
            top_n
        )

        return result[
            [
                "user_id",
                "age",
                "work_mode",
                "screen_time_hours",
                "leisure_screen_hours",
                "sleep_hours",
                "addiction_score",
                "risk_level",
            ]
        ]

    def users_preview(self, limit=5):
        users = []
        for i, user in enumerate(iterate_users(self.data)):
            if i >= limit:
                break
            users.append(user)
        return users

    def high_risk_users_preview(self, limit=5):
        users = []
        for i, user in enumerate(iterate_high_risk_users(self.data)):
            if i >= limit:
                break
            users.append(user)
        return users


if __name__ == "__main__":
    # Example usage
    data = pd.read_csv("data/processed/cleaned_screen_time.csv")
    analyser = DataAnalyser(data)
    summary = analyser.get_summary_statistics()

    for key, value in summary.items():
        print(f"{key}: {value:.2f}")

    print("\n\nRisk Level Distribution:")

    counts = analyser.risk_level()
    total = len(data)

    for level, count in counts.items():
        percent = (count / total) * 100
        print(f"{level}: {count} ({percent:.1f}%)")

    print("\n\nAge Group Analysis:")
    print(analyser.age_group_analysis())

    print("\n\nWork Mode Analysis:")
    print(analyser.work_mode_analysis())

    print("\n\nTop Risk Users:")
    print(analyser.top_users_analysis())

    print("\n\nUsers Preview (Generator):")
    print(analyser.users_preview())

    print("\n\nHigh Risk Users Preview (Generator):")
    print(analyser.high_risk_users_preview())
