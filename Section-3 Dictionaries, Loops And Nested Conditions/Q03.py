#Question 3: Product Stock Management 
#A dictionary contains products and their available stock. Use a loop and nested conditions to display the stock status. 
#Conditions: 
#- Stock == 0 -> Out of Stock 
#- Stock <= 5 -> Low Stock 
#- Stock > 5 -> Available 
#Data: 
products = {
    "Laptop": 10,
    "Mouse": 3,
    "Keyboard": 0,
    "Monitor": 7,
    "Printer": 2
}
for product,stock in products.items():
    if stock==0:
        print(product,"Out of stock")
    elif stock<=5:
        print(product,"Low Stock")
    else:
        print(product,"Availble")