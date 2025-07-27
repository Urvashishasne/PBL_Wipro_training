charge_per_hour=0.51
budget=918
cost_day=charge_per_hour*24
cost_week=cost_day*7
cost_month=cost_day*30
daysforbudget= budget/cost_day
print(f"cost to operate one server per day : ${cost_day:.2f}")
print(f"cost to operate one server per week : ${cost_week:.2f}")
print(f"cost to operate one server per month : ${cost_month:.2f}")
print(f"With ${budget}, you can operate one server for {daysforbudget :.2f} days.")