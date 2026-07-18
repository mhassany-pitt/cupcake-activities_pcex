# Step 1 : Define the calculatePay function that returns the final pay.
def calculate_pay(work_hours):
        # Step 1.1: establish base pay rate
        base_rate = 10.0
        # Step 1.2 determine total pay based on hours worked (including possible overtime)
        if work_hours <= 40:
                pay = work_hours * base_rate
        else:
                overtime_hours = work_hours - 40
                normal_pay = 40 * base_rate
                overtime_pay = overtime_hours * (base_rate * 1.5)
                pay = normal_pay + overtime_pay
        return pay
# Step 2: Define the budget function that returns the current saving
def budget(rent, utilities, food, work_hours, current_savings):
        # Step 2.1:#add up all expenses for the month
        total_expenses = rent + utilities + food
        # Step 2.2:calculate total paycheck amount based on hours
        paycheck = calculate_pay(work_hours)
        # Step 2.3: find the current saving after getting paid
        current_savings = current_savings + paycheck
        # Step 2.4 find the current saving left after expenses
        current_savings = current_savings - total_expenses
        return current_savings
print("after payday and expenses, you will have: ", budget(900, 150, 300, 41, 1500))
