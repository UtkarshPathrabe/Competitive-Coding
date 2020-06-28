meal_cost, tip_percent, tax_percent = float(raw_input()), float(raw_input()), float(raw_input())
tip = meal_cost * tip_percent / 100.0
tax = meal_cost * tax_percent / 100.0
total_cost = meal_cost + tip + tax
print 'The total meal cost is ' + str(int(round(total_cost))) + ' dollars.'