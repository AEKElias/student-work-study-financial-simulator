"""Streamlit dashboard for the existing student finance simulator."""

import streamlit as st
import pandas as pd

from src.budget import monthly_budget_summary
from src.finance import calculate_semester_finances
from src.monte_carlo import run_monte_carlo
from src.risk_analysis import analyze_results
from src.simulation import simulate_semester

st.set_page_config(page_title="Student Work-Study Planner", page_icon="💵", layout="wide")
st.title("Student Budget & Work-Study Planner")
st.write("Estimate how your work hours and spending affect your savings during a semester.")

with st.sidebar:
    st.header("Your work and semester")
    starting_balance = st.number_input("Starting balance ($)", min_value=0.0, value=500.0, step=50.0)
    hourly_wage = st.number_input("Hourly pay ($)", min_value=0.0, value=16.0, step=0.5)
    hours_per_week = st.number_input("Work hours per week", min_value=0.0, value=10.0, step=1.0)
    semester_weeks = st.number_input("Weeks in the semester", min_value=1, max_value=52, value=15)

st.subheader("Your estimated monthly expenses")
left, right = st.columns(2)
with left:
    housing = st.number_input("Housing ($/month)", min_value=0.0, value=0.0, step=25.0)
    food = st.number_input("Food ($/month)", min_value=0.0, value=250.0, step=25.0)
    transportation = st.number_input("Transportation ($/month)", min_value=0.0, value=40.0, step=10.0)
with right:
    personal = st.number_input("Personal spending ($/month)", min_value=0.0, value=100.0, step=25.0)
    school = st.number_input("School supplies ($/month)", min_value=0.0, value=30.0, step=10.0)
    other = st.number_input("Other expenses ($/month)", min_value=0.0, value=50.0, step=10.0)

categories = {
    "Housing": housing,
    "Food": food,
    "Transportation": transportation,
    "Personal": personal,
    "School supplies": school,
    "Other": other,
}
monthly = monthly_budget_summary(hourly_wage, hours_per_week, categories)
semester = calculate_semester_finances(
    starting_balance=starting_balance,
    hourly_wage=hourly_wage,
    hours_per_week=hours_per_week,
    semester_weeks=semester_weeks,
    weekly_spending=monthly["weekly_expenses"],
)
history = simulate_semester(
    starting_balance=starting_balance,
    hourly_wage=hourly_wage,
    hours_per_week=hours_per_week,
    semester_weeks=semester_weeks,
    weekly_spending=monthly["weekly_expenses"],
)

st.subheader("Your budget forecast")
a, b, c, d = st.columns(4)
a.metric("Gross monthly income", f"${monthly['monthly_income']:,.2f}")
b.metric("Monthly expenses", f"${monthly['monthly_expenses']:,.2f}")
c.metric("Monthly surplus", f"${monthly['monthly_surplus']:,.2f}")
d.metric("Semester ending balance", f"${semester['ending_balance']:,.2f}")
st.caption("These are estimates before taxes. Monthly spending is converted to weekly spending using 52 weeks per year.")

st.subheader("Set a savings goal")
goal_balance = st.number_input(
    "Target balance at the end of the semester ($)",
    min_value=1.0,
    value=1500.0,
    step=100.0,
)
ending_balance = semester["ending_balance"]
goal_progress = min(max(ending_balance / goal_balance, 0.0), 1.0)
st.progress(goal_progress, text=f"{goal_progress:.0%} of your target balance")
if ending_balance >= goal_balance:
    st.success(
        f"You're on track! The forecast is ${ending_balance - goal_balance:,.2f} above your target."
    )
else:
    st.info(
        f"Your forecast is ${goal_balance - ending_balance:,.2f} below your target."
    )
st.caption("Goal progress uses your projected ending balance, including the money you already have.")

st.subheader("Where your money goes")
expense_df = pd.DataFrame(
    [{"Category": name, "Amount ($)": amount} for name, amount in categories.items()]
)
st.bar_chart(expense_df, x="Category", y="Amount ($)", horizontal=True)

st.subheader("Estimated balance by week")
st.line_chart({"Balance ($)": [round(week["balance"], 2) for week in history]})
st.caption("The chart begins at week 0 (your starting balance). It assumes stable hours and spending, with no emergencies.")

with st.expander("Optional: Explore missed shifts and unexpected expenses"):
    spending_variation_pct = st.slider("Weekly spending variation (%)", 0, 100, 20, 5)
    missed_work_pct = st.slider("Chance of missing some work in a week (%)", 0, 100, 10, 5)
    emergency_pct = st.slider("Chance of an emergency expense in a week (%)", 0, 100, 5, 5)
    emergency_cost = st.number_input("Cost of one emergency ($)", min_value=0.0, value=150.0, step=25.0)
    safety_threshold = st.number_input("Desired minimum ending balance ($)", min_value=0.0, value=500.0, step=50.0)
    run_risk = st.checkbox("Show risk simulation (500 possible semesters)")
    if run_risk:
        results = run_monte_carlo(
            starting_balance=starting_balance,
            hourly_wage=hourly_wage,
            hours_per_week=hours_per_week,
            semester_weeks=semester_weeks,
            weekly_spending=monthly["weekly_expenses"],
            spending_variation=spending_variation_pct / 100,
            missed_work_probability=missed_work_pct / 100,
            emergency_probability=emergency_pct / 100,
            emergency_cost_min=emergency_cost,
            emergency_cost_max=emergency_cost,
            n_simulations=500,
            seed=42,
        )
        risk = analyze_results(results, safety_threshold=safety_threshold)
        x, y, z = st.columns(3)
        x.metric("Average ending balance", f"${risk['average_ending_balance']:,.2f}")
        y.metric("Chance of going below $0", f"{risk['probability_of_running_out']:.1%}")
        z.metric("Chance of ending below your target", f"{risk['probability_below_threshold']:.1%}")
        st.caption("These scenario percentages depend on your assumptions. They are not predictions or financial advice.")
