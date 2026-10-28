#Question 6: Extract vowels from a string and store the result in a new list. 
text = "programming"
new_list = [char for char in text if char in "aeiou"]
print(new_list)