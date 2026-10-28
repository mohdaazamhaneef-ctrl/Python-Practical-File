#Question8: Replace every even number with "Even" and every odd number with "Odd", then store the result in a new list. 
numbers = [10, 15, 20, 25, 30] 
new_list = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(new_list)