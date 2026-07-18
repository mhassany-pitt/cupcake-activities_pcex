# Step 1 : Define the budget function that returns the current savings.
def budget(rent, utilities, food, paycheck, current_savings):
        # Step 1.1: add up all expenses for the month
        total_expenses = rent + utilities + food
        # Step 1.2: find total amount left after getting paid
        current_savings = current_savings + paycheck
        # Step 1.3: find total amount left after expenses
        current_savings = current_savings - total_expenses
        return (current_savings)
# Step 2: Display the current saving
print("after payday and expenses, you will have: ""$", budget(900, 150, 300, 700, 1500))
