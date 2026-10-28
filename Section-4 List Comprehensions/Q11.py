#Question 11: Find employees earning more than ₹50,000. 
employees = [ 
{"name": "Amit", "salary": 45000}, 
{"name": "Rahul", "salary": 60000}, 
{"name": "Neha", "salary": 75000}, 
{"name": "Rohit", "salary": 35000} 
]
new_list = [emp for emp in employees if emp["salary"] > 50000]
print(new_list)