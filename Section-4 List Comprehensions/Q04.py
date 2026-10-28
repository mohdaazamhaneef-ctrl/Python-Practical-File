#Question 4: Find names having more than 4 characters and store them in a new list. 
names = ["Amit", "Rahul", "Neha", "Rohit", "Sneha"]
new_list = [name for name in names if len(name) > 4]
print(new_list)