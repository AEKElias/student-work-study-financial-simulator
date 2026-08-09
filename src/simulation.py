def simulate_semester(
    starting_balance: float,
    hourly_wage: float,
    hours_per_week: float,
    semester_weeks: int,
    weekly_spending: float,
) -> list[dict]:
    """Simulate a student's balance week by week."""

    balance = starting_balance
    weekly_income = hourly_wage * hours_per_week

    history = [
        {
            "week": 0,
            "income": 0,
            "spending": 0,
            "balance": balance,
        }
    ]

    for week in range(1, semester_weeks + 1):
        balance = balance + weekly_income - weekly_spending

        history.append(
            {
                "week": week,
                "income": weekly_income,
                "spending": weekly_spending,
                "balance": balance,
            }
        )

    return history