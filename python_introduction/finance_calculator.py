Monthly_income = int(input("Enter your monthly income:"))
Monthly_expenses = int(input("Enter your monthly expenses:"))

(Monthly_savings) = (Monthly_income) - (Monthly_expenses)

Projectedsavings  = Monthly_savings*12 + (Monthly_savings*12*0.05)
Projected_savings = int(Projectedsavings)
print(f"Your monthly savings are  ${Monthly_savings}")
print(f"Projected savings after one year, with interest, is:  ${Projected_savings}") 