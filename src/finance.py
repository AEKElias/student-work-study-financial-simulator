def calculate_semester_finances(
    starting_balance: float,
    hourly_wage: float,
    hours_per_week: float,
    semester_weeks: int,
    weekly_spending: float,
) -> dict:
    """Calculate a student's basic semester finances."""

    total_income = hourly_wage * hours_per_week * semester_weeks
    total_expenses = weekly_spending * semester_weeks
    ending_balance = starting_balance + total_income - total_expenses

    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "ending_balance": ending_balance,
    }