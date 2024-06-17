monthly_income = int(input("Enter your monthly income: "))
total_expenses = int(input("Enter your total monthly expenses: "))
# Monthly savings is the difference between monthly income and total expenses
monthly_savings = monthly_income - total_expenses
print("Your monthly savings are $", monthly_savings, ".", sep="")
# Annual savings is the product of monthly savings and 12
interest_rate = 0.05
annual_savings = monthly_savings * 12 * (1 + interest_rate)
print("Projected savings after one year, with interest, is: $",
      annual_savings, ".", sep="")
