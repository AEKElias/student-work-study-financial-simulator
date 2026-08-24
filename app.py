from src.monte_carlo import run_monte_carlo
from src.risk_analysis import analyze_results


def main():
    print("Student Work-Study Financial Simulator")
    print("--------------------------------------")
    starting_balance = float(input("Starting balance ($): "))
    hourly_wage = float(input("Hourly wage ($): "))
    hours_per_week = float(input("Hours worked per week: "))
    semester_weeks = int(input("Number of semester weeks: "))
    weekly_spending = float(input("Average weekly spending ($): "))
    spending_variation = float(
    input("Spending variation (0-1, e.g. 0.20 = 20%): ")
    )

    missed_work_probability = float(
        input("Probability of missing work each week (0-1): ")
    )

    emergency_probability = float(
        input("Probability of an emergency expense each week (0-1): ")
    )

    emergency_cost_min = float(
        input("Minimum emergency cost ($): ")
    )

    emergency_cost_max = float(
        input("Maximum emergency cost ($): ")
    )

    n_simulations = int(
        input("Number of simulations: ")
    )

    safety_threshold = float(
        input("Safety balance threshold ($): ")
    )
    results = run_monte_carlo(
        starting_balance=starting_balance,
        hourly_wage=hourly_wage,
        hours_per_week=hours_per_week,
        semester_weeks=semester_weeks,
        weekly_spending=weekly_spending,
        spending_variation=spending_variation,
        missed_work_probability=missed_work_probability,
        emergency_probability=emergency_probability,
        emergency_cost_min=emergency_cost_min,
        emergency_cost_max=emergency_cost_max,
        n_simulations=n_simulations,
    )

    analysis = analyze_results(
        results,
        safety_threshold=safety_threshold,
    )

    print()
    print("------ Financial Risk Report ------")
    print()

    print(
        f"Average ending balance: "
        f"${analysis['average_ending_balance']:,.2f}"
    )

    print(
        f"Median ending balance: "
        f"${analysis['median_ending_balance']:,.2f}"
    )

    print(
        f"Worst ending balance: "
        f"${analysis['worst_ending_balance']:,.2f}"
    )

    print(
        f"Best ending balance: "
        f"${analysis['best_ending_balance']:,.2f}"
    )

    print()

    print(
        f"Chance of running out of money: "
        f"{analysis['probability_of_running_out']:.1%}"
    )

    print(
        f"Chance of ending below ${safety_threshold:,.2f}: "
        f"{analysis['probability_below_threshold']:.1%}"
    )

    print()
    print(f"Based on {n_simulations:,} simulated semesters.")

if __name__ == "__main__":
    main()