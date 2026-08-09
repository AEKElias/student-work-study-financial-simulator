import random


def simulate_semester(
    starting_balance: float,
    hourly_wage: float,
    hours_per_week: float,
    semester_weeks: int,
    weekly_spending: float,
    spending_variation: float = 0.0,
    seed: int | None = None,
) -> list[dict]:
    """Simulate a student's balance week by week."""

    rng = random.Random(seed)

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
        variation = rng.uniform(-spending_variation, spending_variation)
        actual_spending = weekly_spending * (1 + variation)

        balance = balance + weekly_income - actual_spending

        history.append(
            {
                "week": week,
                "income": weekly_income,
                "spending": actual_spending,
                "balance": balance,
            }
        )

    return history