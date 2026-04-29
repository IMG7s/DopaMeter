import pandas as pd


def iterate_users(data: pd.DataFrame):
    for _, row in data.iterrows():
        yield {
            "user_id": row["user_id"],
            "age": row["age"],
            "work_mode": row["work_mode"],
            "screen_time_hours": row["screen_time_hours"],
            "sleep_hours": row["sleep_hours"],
            "risk_level": row["risk_level"],
        }


def iterate_high_risk_users(data: pd.DataFrame):
    for _, row in data.iterrows():
        if row["risk_level"] == "high":
            yield {
                "user_id": row["user_id"],
                "age": row["age"],
                "work_mode": row["work_mode"],
                "addiction_score": row["addiction_score"],
                "sleep_hours": row["sleep_hours"],
                "risk_level": row["risk_level"],
            }
