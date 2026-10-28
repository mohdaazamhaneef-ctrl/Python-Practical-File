#Question 1: Check Student Result 
#Given a dictionary containing student marks, use a loop to print whether each student has Passed or Failed. 
#Conditions: 
#- Marks >= 40 -> Pass 
#- Marks < 40 -> Fail 
#Data: 
students = { 
        "Rahul": 75, 
        "Amit": 32, 
        "Priya": 88, 
        "Neha": 39, 
        "Rohit": 55 
}
for name, marks in students.items():
    if marks >= 40:
        print(name, "Passed")
    else:
        print(name, "Failed")