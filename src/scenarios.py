"""Compare different weekly work schedules using the existing budget model."""

from collections.abc import Iterable

from src.finance import calculate_semester_finances


def compare_work_schedules(
    starting_balance: float,
    hourly_wage: float,
    semester_weeks: int,
    weekly_spending: float,
    hours_options: Iterable[float] = (5, 10, 15),
) -> list[dict]:
    """Estimate gross income and ending balance for each weekly hours option.

    Assumes hours, wage, and weekly spending stay constant for the semester.
    """
    if starting_balance < 0 or hourly_wage < 0 or weekly_spending < 0:
        raise ValueError("Money inputs cannot be negative.")
    if semester_weeks < 1:
        raise ValueError("Semester length must be at least one week.")

    options = sorted(set(hours_options))
    if not options or any(hours < 0 for hours in options):
        raise ValueError("Provide at least one nonnegative work-hours option.")

    comparison = []
    for hours in options:
        finance = calculate_semester_finances(
            starting_balance=starting_balance,
            hourly_wage=hourly_wage,
            hours_per_week=hours,
            semester_weeks=semester_weeks,
            weekly_spending=weekly_spending,
        )
        comparison.append({
            "hours_per_week": hours,
            "total_income": finance["total_income"],
            "ending_balance": finance["ending_balance"],
        })
    return comparison
