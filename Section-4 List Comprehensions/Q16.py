#Question 16: Find names of employees from the IT department. 
employees = [ 
        {"name": "Amit", "department": "IT"}, 
        {"name": "Rahul", "department": "HR"}, 
        {"name": "Neha", "department": "IT"}, 
        {"name": "Rohit", "department": "Sales"} 
]
new_list = [emp["name"] for emp in employees if emp["department"] == "IT"]
print(new_list)