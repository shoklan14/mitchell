hr_wage = float(input("Enter your hourly wage"))
total_regular_hr = float(input("Enter your total regular hours"))
total_overtime = float(input("Enter yout total evertime hours"))
overtime_pay = total_overtime*1.5*hr_wage
total_weekly = str(hr_wage * total_regular_hr + overtime_pay)
print("Your total weekly pay is" + total_weekly)