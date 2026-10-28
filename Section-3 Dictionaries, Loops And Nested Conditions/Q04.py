#Question 4: Employee Salary and Department 
#The dictionary contains employee salary and department. Display the employee category. 
#Conditions: 
#- Salary >= ₹50,000: 
#- IT -> Senior IT Employee 
#- HR -> Senior HR Employee 
#- Other departments -> Senior Employee 
#- Salary < ₹50,000 -> Junior Employee 
#Data: 
employees = { 
        "Rahul": {"salary": 60000, "department": "IT"}, 
        "Amit": {"salary": 40000, "department": "HR"}, 
        "Priya": {"salary": 70000, "department": "IT"}, 
        "Neha": {"salary": 45000, "department": "Finance"} 
}
for name,info in employees.items():
    salary=info["salary"]
    department=info["department"]
    if salary>=50000:
        if department=="IT":
            print(name,"Senior IT Employee")
        elif department=="HR":
            print(name,"Senior HR Employee")
        else:
            print(name,"Senior Employee")
    else:
        print(name,"Junior Employee")