#Question 2: Find numbers between 20 and 50 and store them in a new list. 
numbers = [10, 25, 35, 60, 45, 15, 50, 70]
new_list = [num for num in numbers if 20 < num < 50]
print(new_list)