#Q10: Count even and odd numbers between 1 and 50. 
count_even=0
count_odd=0
for i in range(1,51):
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print("Even Numbers Count:",count_even)
print("Odd Numbers Count:",count_odd)