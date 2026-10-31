import pytest

from src.budget import monthly_budget_summary, monthly_expenses_to_weekly


def test_monthly_expenses_to_weekly():
    assert monthly_expenses_to_weekly({"Food": 260, "Other": 260}) == 120


def test_monthly_budget_summary():
    result = monthly_budget_summary(15, 10, {"Food": 300, "Other": 100})
    assert result["monthly_income"] == 650
    assert result["monthly_expenses"] == 400
    assert result["monthly_surplus"] == 250


def test_negative_expenses_rejected():
    with pytest.raises(ValueError):
        monthly_expenses_to_weekly({"Food": -20})


def test_negative_hours_rejected():
    with pytest.raises(ValueError):
        monthly_budget_summary(15, -5, {"Food": 100})
