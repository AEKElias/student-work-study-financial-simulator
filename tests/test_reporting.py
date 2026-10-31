import csv
from io import StringIO

from src.reporting import build_financial_report_csv


def sample_report(categories=None):
    return build_financial_report_csv(
        starting_balance=500,
        hourly_wage=16,
        hours_per_week=10,
        semester_weeks=2,
        categories=categories or {"Food": 100, "Transport": 50},
        monthly={
            "monthly_income": 693.33,
            "monthly_expenses": 150,
            "monthly_surplus": 543.33,
        },
        semester={
            "total_income": 320,
            "total_expenses": 69.23,
            "ending_balance": 750.77,
        },
        goal_balance=900,
        comparisons=[
            {"hours_per_week": 5, "total_income": 160, "ending_balance": 590.77},
            {"hours_per_week": 10, "total_income": 320, "ending_balance": 750.77},
        ],
        history=[
            {"week": 0, "balance": 500},
            {"week": 1, "balance": 625.38},
            {"week": 2, "balance": 750.77},
        ],
    )


def test_csv_report_includes_correct_sections_and_values():
    rows = list(csv.DictReader(StringIO(sample_report())))
    assert rows[0] == {
        "Section": "Inputs",
        "Item": "Starting balance",
        "Value": "500.00",
        "Unit": "USD",
    }
    assert any(row["Section"] == "Monthly expenses" and row["Item"] == "Food" for row in rows)
    assert any(
        row["Section"] == "Forecast"
        and row["Item"] == "Projected ending balance"
        and row["Value"] == "750.77"
        for row in rows
    )
    assert any(
        row["Section"] == "Savings goal" and row["Value"] == "-149.23"
        for row in rows
    )
    assert sum(row["Section"] == "Weekly projection" for row in rows) == 3
    assert sum(row["Section"] == "Work schedule comparison" for row in rows) == 4


def test_csv_report_escapes_categories_with_commas():
    rows = list(csv.DictReader(StringIO(sample_report({"Food, snacks": 100}))))
    assert any(row["Item"] == "Food, snacks" for row in rows)
