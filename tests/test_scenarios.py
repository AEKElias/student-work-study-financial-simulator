import pytest

from src.scenarios import compare_work_schedules


def test_compare_work_schedules():
    scenarios = compare_work_schedules(
        starting_balance=500,
        hourly_wage=16,
        semester_weeks=15,
        weekly_spending=100,
    )
    assert [s["hours_per_week"] for s in scenarios] == [5, 10, 15]
    assert [s["total_income"] for s in scenarios] == [1200, 2400, 3600]
    assert [s["ending_balance"] for s in scenarios] == [200, 1400, 2600]


def test_comparison_sorts_and_removes_duplicate_hours():
    scenarios = compare_work_schedules(100, 10, 2, 30, [15, 5, 15, 0])
    assert [s["hours_per_week"] for s in scenarios] == [0, 5, 15]


@pytest.mark.parametrize(
    "kwargs",
    [
        {"hourly_wage": -1},
        {"starting_balance": -1},
        {"weekly_spending": -1},
        {"semester_weeks": 0},
        {"hours_options": []},
        {"hours_options": [-5]},
    ],
)
def test_comparison_rejects_invalid_input(kwargs):
    inputs = dict(
        starting_balance=500,
        hourly_wage=16,
        semester_weeks=15,
        weekly_spending=100,
    )
    inputs.update(kwargs)
    with pytest.raises(ValueError):
        compare_work_schedules(**inputs)
