#Question 10: Give a 10% discount to products costing ₹1,000 or more; otherwise, give a 5% discount. Store the final 
#prices in a new list. 
prices = [500, 1200, 800, 2000, 1500]
new_prices = [price * 0.90 if price >= 1000 else price * 0.95 for price in prices]
print(new_prices)