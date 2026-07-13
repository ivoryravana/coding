import random

items = ["korean fried chicken", "powdered water", "sashimi", "coffee", "decaf", "chai tea"]
specials = ["french onion soup", "liquid oxygen"]

menuprices = {
    "korean fried chicken": 16,
    "powdered water": 649.99,
    "sashimi": 500,
    "coffee": 5,
    "decaf": 4,
    "chai tea": 100,
}
specialmenuprices = {"french onion soup": 99.99, "liquid oxygen": 99.99}

print("Welcome to The 6 or 7 Guys cafe!!")
print("Here is our regular menu:")
for item in items:
    print(f"- {item} (${menuprices[item]:.2f})")

special = random.choice(specials)
print(f"Today's special is {special} (${specialmenuprices[special]:.2f})")
print("Type 'done' when you are finished ordering.")

cost = 0.0
while True:
    order = input("What do you want to order? ").strip().lower()
    if not order or order == "done":
        break

    if order in menuprices:
        price = menuprices[order]
        cost += price
        print(f"Added {order}: ${price:.2f}. Running total: ${cost:.2f}")
    elif order in specialmenuprices:
        price = specialmenuprices[order]
        cost += price
        print(f"Added special {order}: ${price:.2f}. Running total: ${cost:.2f}")
    else:
        print(f"Sorry, we don't have '{order}'. Please choose from the menu or the special.")

print(f"Your total comes to ${cost:.2f}. Thank you for visiting The 6 or 7 Guys cafe!")
