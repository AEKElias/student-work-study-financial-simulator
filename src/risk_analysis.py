from statistics import mean, median


def analyze_results(results, safety_threshold=500):
    ending_balances = [
        result["ending_balance"]
        for result in results
    ]

    ran_out_count = sum(
        result["ran_out_of_money"]
        for result in results
    )

    below_threshold_count = sum(
        balance < safety_threshold
        for balance in ending_balances
    )

    return {
        "worst_ending_balance": min(ending_balances),
        "best_ending_balance": max(ending_balances),
        "average_ending_balance": mean(ending_balances),
        "median_ending_balance": median(ending_balances),
        "probability_of_running_out": ran_out_count / len(results),
        "probability_below_threshold": below_threshold_count / len(results),
    }