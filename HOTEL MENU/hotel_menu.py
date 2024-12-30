# Dfine the menu of hotel 

menu = {
    'Pizza' : 250,
    'Burger' : 150,
    'Pasta' : 200,
    'French Fries' : 100,
    'Sandwich' : 150,
    'Coke' : 50,
    'Pepsi' : 150,
    'Sprite' : 450,
    'Thumbs Up' : 40,
    'Mountain Dew' : 850,
    'Diet Coke' : 70,
    'Diet Pepsi' : 70,
    'Diet Sprite' : 550,
    'Diet Thumbs Up' : 50,
    'Veg Biryani' : 200,
}
# Greet
print("Welcome to the Python Hotel")
print("Here is the menu for today")
print("Pizza : Rs250\nBurger : Rs150\nPasta : Rs200\nFrench Fries : Rs100\nSandwich : Rs150\nCoke : Rs50\nPepsi : Rs150\nSprite : Rs450\nThumbs Up : Rs40\nMountain Dew : Rs850\nDiet Coke : Rs70\nDiet Pepsi : Rs70\nDiet Sprite : Rs550\nDiet Thumbs Up : Rs50\nVeg Biryani : Rs200")

order_total = 0

# Ask for the order

item_1 = input("Enter the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to the cart")
else:
    print("Sorry, the {item_1} you entered is not avaialable in the menu")    

another_order = input("Do you want to order another item? (yes/no): ")
if another_order == "yes":
    item_2 = input("Enter the item you want to order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to the cart")
    else:
        print("Sorry, the {item_2} you entered is not avaialable in the menu")

# print the total amount
print(f"Your total order amount is Rs{order_total}")       