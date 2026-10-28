#Question 7: Extract digits from a string and store the result in a new list. 
data = "Python123Programming456"
new_list = [char for char in data if char.isdigit()]
print(new_list)