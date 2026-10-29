#Q3: Employee Bonus 
#Conditions:
#- If experience >= 1 year and salary >= ₹50,000:
#- Performance >= 90 -> 20% bonus 
#- Performance >= 75 -> 10% bonus 
#- Otherwise -> 5% bonus 
#- If salary < ₹50,000: 
#- Performance >= 90 -> 15% bonus 
#- Otherwise -> 5% bonus

experience = float(input("Enter experience (in years): "))
salary = float(input("Enter salary: ₹"))
performance = float(input("Enter performance score: "))
if experience >= 1:
    if salary >= 50000:
        if performance >= 90:
            bonus = salary * 20 / 100
        elif performance >= 75:
            bonus = salary * 10 / 100
        else:
            bonus = salary * 5 / 100
    else:
        if performance >= 90:
            bonus = salary * 15 / 100
        else:
            bonus = salary * 5 / 100

    print("Bonus Amount: ₹", bonus)
    print("Total Salary: ₹", salary + bonus)
else:
    print("Not Eligible for Bonus")