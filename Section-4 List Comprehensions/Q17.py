#Question 17: Find employees who earn more than ₹60,000 and belong to IT. 
employees = [ 
        {"name": "Amit", "department": "IT", "salary": 55000}, 
        {"name": "Rahul", "department": "HR", "salary": 70000}, 
        {"name": "Neha", "department": "IT", "salary": 80000}, 
        {"name": "Rohit", "department": "IT", "salary": 45000} 
]
new_list = [
    emp["name"] for emp in employees
    if emp["salary"] > 60000 and emp["department"] == "IT"
]
print(new_list)