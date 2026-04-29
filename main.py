import argparse
from src.loader import DataLoader
from src.preprocessing import DataPreprocessor
from src.analysis import DataAnalyser
from src.report import build_report


def main():
    parser = argparse.ArgumentParser(description="DopaMeter CLI")
    parser.add_argument(
        "command",
        choices=["stats", "risk", "analyze", "report", "users", "highrisk"],
        help="Command to run",
    )

    args = parser.parse_args()

    data_loader = DataLoader(file_path="data/raw/ScreenTimeMentalWellness.csv")
    preprocessor = DataPreprocessor(data_loader)
    data = preprocessor.preprocess_data()

    analyser = DataAnalyser(data)

    if args.command == "stats":
        summary = analyser.get_summary_statistics()
        print("Summary Statistics:")
        for key, value in summary.items():
            print(f"{key}: {value:.2f}")

    elif args.command == "risk":
        risk = analyser.risk_level()
        total = risk.sum()

        print("Risk Level Distribution:")
        for level, count in risk.items():
            percent = (count / total) * 100
            print(f"{level}: {count} ({percent:.1f}%)")

    elif args.command == "analyze":
        print(
            f"Correlation between leisure screen time and sleep: "
            f"{analyser.get_leisure_and_sleep_connection():.2f}"
        )
        print("\nAge Group Analysis:")
        print(analyser.age_group_analysis())

        print("\nWork Mode Analysis:")
        print(analyser.work_mode_analysis())

        print("\nTop Risk Users:")
        print(analyser.top_users_analysis())

    elif args.command == "report":
        report = build_report(analyser)
        print(report)

    elif args.command == "users":
        print("Users Preview (Generator):")
        for i, user in enumerate(analyser.users_preview(limit=5), start=1):
            print(f"\nUser {i}")
            print("-" * 20)
            print(f"ID: {user['user_id']}")
            print(f"Age: {user['age']}")
            print(f"Work mode: {user['work_mode']}")
            print(f"Screen time: {user['screen_time_hours']} h")
            print(f"Sleep: {user['sleep_hours']} h")
            print(f"Risk level: {user['risk_level']}")

    elif args.command == "highrisk":
        print("High Risk Users Preview (Generator):")
        for i, user in enumerate(analyser.high_risk_users_preview(limit=5), start=1):
            print(f"\nHigh-risk user {i}")
            print("-" * 25)
            print(f"ID: {user['user_id']}")
            print(f"Age: {user['age']}")
            print(f"Work mode: {user['work_mode']}")
            print(f"Addiction score: {user['addiction_score']}")
            print(f"Sleep: {user['sleep_hours']} h")
            print(f"Risk level: {user['risk_level']}")


if __name__ == "__main__":
    main()
