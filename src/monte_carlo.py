import random

from src.simulation import simulate_semester


def run_monte_carlo(
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
    n_simulations: int = 1000,
    seed: int | None = None,
) -> list[dict]:
    """Run many possible semester simulations."""

    master_rng = random.Random(seed)

    results = []

    for simulation_number in range(1, n_simulations + 1):
        simulation_seed = master_rng.randrange(0, 2**32)

        history = simulate_semester(
            starting_balance=starting_balance,
            hourly_wage=hourly_wage,
            hours_per_week=hours_per_week,
            semester_weeks=semester_weeks,
            weekly_spending=weekly_spending,
            spending_variation=spending_variation,
            missed_work_probability=missed_work_probability,
            worked_fraction_if_missed=worked_fraction_if_missed,
            emergency_probability=emergency_probability,
            emergency_cost_min=emergency_cost_min,
            emergency_cost_max=emergency_cost_max,
            seed=simulation_seed,
        )

        balances = [week["balance"] for week in history]

        minimum_balance = min(balances)
        ending_balance = history[-1]["balance"]

        results.append(
            {
                "simulation": simulation_number,
                "ending_balance": ending_balance,
                "minimum_balance": minimum_balance,
                "ran_out_of_money": minimum_balance < 0,
            }
        )

    return results