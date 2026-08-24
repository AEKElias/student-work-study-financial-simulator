from src.monte_carlo import run_monte_carlo


def test_monte_carlo_runs_requested_number():
    results = run_monte_carlo(
        starting_balance=1000,
        hourly_wage=16,
        hours_per_week=10,
        semester_weeks=15,
        weekly_spending=120,
        spending_variation=0.20,
        n_simulations=100,
        seed=42,
    )

    assert len(results) == 100
    assert results[0]["simulation"] == 1
    assert results[-1]["simulation"] == 100

def test_monte_carlo_is_reproducible():
    results_1 = run_monte_carlo(
        starting_balance=1000,
        hourly_wage=16,
        hours_per_week=10,
        semester_weeks=15,
        weekly_spending=120,
        spending_variation=0.20,
        n_simulations=10,
        seed=42,
    )

    results_2 = run_monte_carlo(
        starting_balance=1000,
        hourly_wage=16,
        hours_per_week=10,
        semester_weeks=15,
        weekly_spending=120,
        spending_variation=0.20,
        n_simulations=10,
        seed=42,
    )

    assert results_1 == results_2