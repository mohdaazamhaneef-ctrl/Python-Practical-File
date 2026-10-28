#Question 5: Find names starting with "A" and store them in a new list. 
names = ["Amit", "Rahul", "Ankit", "Neha", "Arjun", "Rohit"] 
new_list = [name for name in names if name.startswith("A")]
print(new_list)