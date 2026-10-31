"""Helpers for converting a monthly student budget into a weekly simulation."""

from collections.abc import Mapping

WEEKS_PER_YEAR = 52
MONTHS_PER_YEAR = 12


def monthly_expenses_to_weekly(categories: Mapping[str, float]) -> float:
    """Convert the total monthly budget to a weekly equivalent (52 weeks/year)."""
    if any(amount < 0 for amount in categories.values()):
        raise ValueError("Expense amounts cannot be negative.")
    return sum(categories.values()) * MONTHS_PER_YEAR / WEEKS_PER_YEAR


def monthly_budget_summary(
    hourly_wage: float,
    hours_per_week: float,
    categories: Mapping[str, float],
) -> dict[str, float]:
    """Return estimated gross monthly income, expenses, and surplus."""
    if hourly_wage < 0 or hours_per_week < 0:
        raise ValueError("Wage and hours cannot be negative.")
    weekly_expenses = monthly_expenses_to_weekly(categories)
    monthly_income = hourly_wage * hours_per_week * WEEKS_PER_YEAR / MONTHS_PER_YEAR
    monthly_expenses = sum(categories.values())
    return {
        "monthly_income": monthly_income,
        "monthly_expenses": monthly_expenses,
        "monthly_surplus": monthly_income - monthly_expenses,
        "weekly_expenses": weekly_expenses,
    }
