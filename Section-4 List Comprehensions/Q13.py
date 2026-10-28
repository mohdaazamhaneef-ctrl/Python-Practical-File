#Question 13: Give a 20% discount only to products costing more than ₹2,000. 
prices = [500, 1200, 2500, 3000, 1500, 5000] 
new_prices = [price * 0.80 if price > 2000 else price for price in prices]
print(new_prices)