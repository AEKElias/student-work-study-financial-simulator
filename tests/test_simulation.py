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