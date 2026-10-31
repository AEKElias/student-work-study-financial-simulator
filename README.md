# Student Work-Study Financial Simulator

A Python and Streamlit app that helps students understand how part-time work, everyday expenses, and unexpected costs can affect their finances during a semester.

## Features

- **Student budget:** Enter your hourly wage, weekly work hours, starting balance, semester length, and monthly expenses.
- **Budget forecast:** Estimate gross monthly income, monthly surplus, and your ending semester balance.
- **Savings goal:** Choose a target ending balance and see how your projected balance compares with it.
- **Work-schedule comparison:** Compare 5, 10, and 15 hours of work per week alongside your selected hours.
- **Charts:** Explore a breakdown of your monthly spending and an estimated weekly balance.
- **Risk scenarios:** Simulate possible missed shifts, variable spending, and emergency expenses using Monte Carlo sampling.
- **CSV export:** Download the budget forecast, expense categories, work-schedule comparisons, and weekly balances to open in a spreadsheet.

## Getting started

Requires **Python 3.10+**. From Terminal:

```bash
git clone https://github.com/AEKElias/student-work-study-financial-simulator.git
cd student-work-study-financial-simulator
python3 -m venv .venv
source .venv/bin/activate  # Mac / Linux
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

Open the local URL shown in Terminal (usually http://localhost:8501). Press **Control+C** to stop the server.

If you already cloned the repository, open its folder and run `git pull` to get the latest changes.

### Test the code

```bash
python -m pytest -v
```

The `tests/` folder checks the budget, simulations, financial risk calculations, work-schedule comparisons, and CSV export.

## How the estimates work

- **Gross weekly pay** = hourly wage × work hours per week.
- **Estimated gross monthly pay** = gross weekly pay × 52 / 12.
- **Estimated weekly spending** = total monthly expenses × 12 / 52.
- **Semester ending balance** = starting balance + semester gross income − semester estimated expenses.
- Work-schedule comparisons assume the same hourly pay and expenses at each schedule.
- The optional risk feature runs multiple random semester scenarios to illustrate how changing assumptions can affect results.

## Project structure

```text
streamlit_app.py         # Interactive web dashboard
app.py                   # Original command-line simulator
src/
  budget.py              # Monthly budget helpers
  finance.py             # Basic semester calculations
  simulation.py          # One semester's week-by-week outcomes
  monte_carlo.py         # Repeated random scenarios
  risk_analysis.py       # Simulation statistics
  scenarios.py           # Compare work schedules
  reporting.py           # Export a CSV financial report
tests/                   # Automated Python tests
requirements.txt         # Dependencies
```

## Limits and assumptions

This is an **educational budgeting tool**, not a financial advice service. Income is **before taxes**; the app does not calculate payroll deductions or benefits. The base forecast assumes constant work hours and expenses and does not include emergencies. The optional Monte Carlo results are illustrations based on the inputs, not predictions.

Expense values are entered as **monthly estimates** and converted to weekly values using 52 weeks per year. The downloaded CSV contains the regular budget forecast, not the optional risk simulation output. User entries are not saved to a database by this version.

## Future improvements

- Add better input validation and clearer charts.
- Let users save and reopen budget scenarios.
- Gather feedback from students and make the interface easier to use.

Built with **Python**, **Streamlit**, **pandas**, and **pytest**.
