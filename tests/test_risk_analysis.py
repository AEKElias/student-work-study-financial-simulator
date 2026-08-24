from src.risk_analysis import analyze_results


def test_analyze_results():
    results = [
        {
            "ending_balance": 1000,
            "ran_out_of_money": False,
        },
        {
            "ending_balance": 1500,
            "ran_out_of_money": False,
        },
        {
            "ending_balance": -100,
            "ran_out_of_money": True,
        },
    ]

    analysis = analyze_results(results, safety_threshold=500)

    assert analysis["worst_ending_balance"] == -100
    assert analysis["best_ending_balance"] == 1500

    assert analysis["average_ending_balance"] == 800
    assert analysis["median_ending_balance"] == 1000
    assert analysis["probability_of_running_out"] == 1 / 3
    assert analysis["probability_below_threshold"] == 1 / 3