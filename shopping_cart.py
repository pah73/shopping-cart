# This project was completed with the help of Professor Rossetti's Guidance Screencast
# Sean Minson and I also worked together to work out some kinks and for mapping out coding logic

import time

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# TODO: write some Python code here to produce the desired output
# I wrote this code with help from Professor Rosetti's Shopping Cart Walkthrough
# The try/ except statement was written with help from https://medium.com/better-programming/how-to-indefinitely-request-user-input-until-valid-in-python-388a7c85aa6e
gross_price=0
selected_items=[]

# Here, I am setting up a while loop so consumer can input
while True:   # will contunue to ask for more items until done
    user_input = input("Please input a user idenifier, or 'DONE' if there are no more items: ")
    if user_input=="DONE": 
        break # break while loop for checkout
    else:
        try:
            if int(user_input)<0: #check if the value is between 1 and the number of products for sale.
                print("There are no negative product idetifiers. Please enter a valid input. ")
            else:
                if int(user_input) <=len(products): # other end of range (products for sale)
                    selected_items.append(user_input)
                else:
                    print("We do not have any products matching that identifier. Please enter a valid input")
  
        except:
            print("Please enter a valid product identifier") # if its not a number


# user interface setup
print("-----------------")
print("GREEN FOODS GROCERY")
print("WWW.GREEN-FOODS-GROCERY.COM")

print("-----------------")

# setting up time
date = time.strftime("%m/%d/%Y %I:%M %p")
print("Checkout at: ", date)
print("-----------------")
print("Selected Products:")

#for-loop for price accumulation with each product purchase inputted
for selected_item in selected_items:

    items = [p for p in products if str(p["id"]) == str(selected_item)]
    item=items[0]
    gross_price=gross_price+item["price"] 
    print("... "+item["name"]+" ("+str(to_usd(item["price"]))+")")

# setting up taxes
tax_amount = gross_price*0.0875
total_price = gross_price + tax_amount

