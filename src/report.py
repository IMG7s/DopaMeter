from src.analysis import DataAnalyser


def build_report(analyser: DataAnalyser) -> str:
    summary = analyser.get_summary_statistics()
    correlation = analyser.get_leisure_and_sleep_connection()
    risk = analyser.risk_level()
    age = analyser.age_group_analysis()
    work = analyser.work_mode_analysis()
    top_users = analyser.top_users_analysis()

    total = sum(risk)

    risk_text = ""
    for level, count in risk.items():
        percent = (count / total) * 100
        risk_text += f"{level}: {count} ({percent:.1f}%)\n"

    report = f"""
    DOPAMETER REPORT
    ===============
    
    GENERAL STATISTICS
    ------------------
    Average screen time: {summary["average_screen_time_hours"]:.2f} hours
    Average leisure time: {summary["average_leisure_time_hours"]:.2f} hours
    Average work time: {summary["average_work_time_hours"]:.2f} hours
    Average sleep time: {summary["average_sleep_time_hours"]:.2f} hours
    Average addiction score: {summary["average_addiction_score"]:.2f}
    
    
    SCREEN TIME & SLEEP
    ------------------
    Correlation: {correlation:.2f}
    
    
    RISK DISTRIBUTION
    -----------------
    {risk_text}
    
        Majority of users fall into medium or high risk categories
    
    
    AGE GROUP ANALYSIS
    ------------------
    {age}
    
        Younger users tend to show slightly higher addiction levels.
    
    WORK MODE ANALYSIS
    ------------------
    {work}
    
        Hybrid users show the highest addiction levels. 
        Remote users have higher total screen time but lower leisure ratio.
    
    TOP RISK USERS
    ----------------
    {top_users}

        High-risk users tend to have high leisure time and reduced sleep.
    
    ==============
    """

    return report
