from src.finance import calculate_semester_finances


def test_calculate_semester_finances():
    result = calculate_semester_finances(
        starting_balance=1000,
        hourly_wage=16,
        hours_per_week=10,
        semester_weeks=15,
        weekly_spending=120,
    )

    assert result["total_income"] == 2400
    assert result["total_expenses"] == 1800
    assert result["ending_balance"] == 1600