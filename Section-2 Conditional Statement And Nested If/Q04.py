# Q4: E-Commerce Discount
#An online shopping website provides discounts based on the following conditions: 
#- If cart amount >= ₹5,000: 
#- If the customer is a premium member, discount = 20%. 
#- Otherwise, discount = 10%. 
#- If cart amount < ₹5,000: 
#- If the customer is a premium member, discount = 5%. 
#- Otherwise, no discount. 
#- Print the final amount. 
amount = float(input("Enter cart amount: ₹"))
pMember = input("Are you a premium member? (True/False): ").lower()

if amount >= 5000:
    if pMember == "true":
        discount = amount * 20 / 100
    else:
        discount = amount * 10 / 100
else:
    if pMember == "true":
        discount = amount * 5 / 100
    else:
        discount = 0

final_amount = amount - discount

print("Discount amount is: ₹", discount)
print("Your Final Amount is: ₹", final_amount)