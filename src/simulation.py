import random


def simulate_semester(
    starting_balance: float,
    hourly_wage: float,
    hours_per_week: float,
    semester_weeks: int,
    weekly_spending: float,
    spending_variation: float = 0.0,
    missed_work_probability: float = 0.0,
    worked_fraction_if_missed: float = 0.5,
    emergency_probability: float = 0.0,
    emergency_cost_min: float = 0.0,
    emergency_cost_max: float = 0.0,
    seed: int | None = None,
) -> list[dict]:
    """Simulate a student's balance week by week."""

    rng = random.Random(seed)

    balance = starting_balance

    history = [
        {
            "week": 0,
            "hours_worked": 0,
            "income": 0,
            "spending": 0,
            "emergency_cost": 0,
            "missed_work": False,
            "balance": balance,
        }
    ]

    for week in range(1, semester_weeks + 1):
        actual_hours = hours_per_week
        missed_work = False

        if (
            missed_work_probability > 0
            and rng.random() < missed_work_probability
        ):
            missed_work = True
            actual_hours = hours_per_week * worked_fraction_if_missed

        weekly_income = hourly_wage * actual_hours

        variation = rng.uniform(
            -spending_variation,
            spending_variation,
        )

        actual_spending = weekly_spending * (1 + variation)

        emergency_cost = 0.0

        if (
            emergency_probability > 0
            and rng.random() < emergency_probability
        ):
            emergency_cost = rng.uniform(
                emergency_cost_min,
                emergency_cost_max,
            )

        balance = (
            balance
            + weekly_income
            - actual_spending
            - emergency_cost
        )

        history.append(
            {
                "week": week,
                "hours_worked": actual_hours,
                "income": weekly_income,
                "spending": actual_spending,
                "emergency_cost": emergency_cost,
                "missed_work": missed_work,
                "balance": balance,
            }
        )

    return history