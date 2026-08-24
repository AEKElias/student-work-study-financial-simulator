from src.simulation import simulate_semester


def test_simulate_semester():
    history = simulate_semester(
        starting_balance=1000,
        hourly_wage=16,
        hours_per_week=10,
        semester_weeks=3,
        weekly_spending=120,
    )

    assert len(history) == 4

    assert history[0]["balance"] == 1000
    assert history[1]["balance"] == 1040
    assert history[2]["balance"] == 1080
    assert history[3]["balance"] == 1120

def test_spending_variation_is_reproducible():
    history_1 = simulate_semester(
        starting_balance=1000,
        hourly_wage=16,
        hours_per_week=10,
        semester_weeks=3,
        weekly_spending=120,
        spending_variation=0.20,
        seed=42,
    )

    history_2 = simulate_semester(
        starting_balance=1000,
        hourly_wage=16,
        hours_per_week=10,
        semester_weeks=3,
        weekly_spending=120,
        spending_variation=0.20,
        seed=42,
    )

    assert history_1 == history_2

def test_spending_stays_within_variation_range():
    history = simulate_semester(
        starting_balance=1000,
        hourly_wage=16,
        hours_per_week=10,
        semester_weeks=20,
        weekly_spending=120,
        spending_variation=0.20,
        seed=42,
    )

    for week in history[1:]:
        assert 96 <= week["spending"] <= 144

def test_missed_work_reduces_income():
    history = simulate_semester(
        starting_balance=1000,
        hourly_wage=16,
        hours_per_week=10,
        semester_weeks=1,
        weekly_spending=120,
        missed_work_probability=1.0,
        worked_fraction_if_missed=0.5,
        seed=42,
    )

    assert history[1]["missed_work"] is True
    assert history[1]["hours_worked"] == 5
    assert history[1]["income"] == 80

def test_emergency_expense_reduces_balance():
    history = simulate_semester(
        starting_balance=1000,
        hourly_wage=16,
        hours_per_week=10,
        semester_weeks=1,
        weekly_spending=120,
        emergency_probability=1.0,
        emergency_cost_min=200,
        emergency_cost_max=200,
        seed=42,
    )

    assert history[1]["emergency_cost"] == 200
    assert history[1]["balance"] == 840