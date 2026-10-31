"""Create a spreadsheet-friendly CSV report from the student's budget forecast."""

import csv
from io import StringIO
from collections.abc import Mapping, Sequence


def build_financial_report_csv(
    *,
    starting_balance: float,
    hourly_wage: float,
    hours_per_week: float,
    semester_weeks: int,
    categories: Mapping[str, float],
    monthly: Mapping[str, float],
    semester: Mapping[str, float],
    goal_balance: float,
    comparisons: Sequence[Mapping[str, float]],
    history: Sequence[Mapping[str, float]],
) -> str:
    """Export the current deterministic budget forecast and scenario comparison."""
    output = StringIO()
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(["Section", "Item", "Value", "Unit"])

    def amount(section: str, label: str, value: float, unit: str) -> None:
        writer.writerow([section, label, f"{value:.2f}", unit])

    amount("Inputs", "Starting balance", starting_balance, "USD")
    amount("Inputs", "Hourly pay", hourly_wage, "USD/hour")
    amount("Inputs", "Hours per week", hours_per_week, "hours/week")
    writer.writerow(["Inputs", "Semester length", semester_weeks, "weeks"])

    for category, value in categories.items():
        amount("Monthly expenses", category, value, "USD/month")

    amount("Forecast", "Gross monthly income", monthly["monthly_income"], "USD/month")
    amount("Forecast", "Monthly expenses", monthly["monthly_expenses"], "USD/month")
    amount("Forecast", "Monthly surplus", monthly["monthly_surplus"], "USD/month")
    amount("Forecast", "Gross semester income", semester["total_income"], "USD")
    amount("Forecast", "Semester expenses", semester["total_expenses"], "USD")
    amount("Forecast", "Projected ending balance", semester["ending_balance"], "USD")
    amount("Savings goal", "Target ending balance", goal_balance, "USD")
    amount(
        "Savings goal",
        "Forecast above or below goal",
        semester["ending_balance"] - goal_balance,
        "USD",
    )

    for scenario in comparisons:
        hours = scenario["hours_per_week"]
        amount(
            "Work schedule comparison",
            f"{hours:g} hours/week: gross semester income",
            scenario["total_income"],
            "USD",
        )
        amount(
            "Work schedule comparison",
            f"{hours:g} hours/week: projected ending balance",
            scenario["ending_balance"],
            "USD",
        )

    for week in history:
        amount("Weekly projection", f"Week {week['week']:g} ending balance", week["balance"], "USD")

    writer.writerow([
        "Notes",
        "Assumptions",
        "Gross income before taxes; fixed work hours and spending; no emergencies in base forecast.",
        "",
    ])
    return output.getvalue()
