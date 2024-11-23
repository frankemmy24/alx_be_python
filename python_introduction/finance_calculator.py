<<<<<<< HEAD
=======

# finance_calculator.py

# Prompt the user for their financial details
monthly_income = input("Enter your monthly income: ")  # User input for income
monthly_expenses = input("Enter your total monthly expenses: ")  # User input for expenses

# Ensure both inputs are converted to floats
monthly_savings = float(monthly_income) - float(monthly_expenses)  # Correct monthly savings calculation

# Project savings over one year with a 5% annual interest rate
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output the results
print(f"Your monthly savings are: {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {projected_savings}.")
>>>>>>> 6231c198f00a86ba850d6ece6e5241c5a6a72f17
