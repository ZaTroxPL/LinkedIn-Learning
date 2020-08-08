# The Shimmy 

def Shimmy():
    print("Take one step to the right and stomp")
    print("Take one step to the left and stomp")
    print("Shake those hips")

# Shimmy()
# Shimmy()
# Shimmy()

# Car wash

def Car_Wash(amount_paid):
    if amount_paid == 6:
        print("Basic Wash")

    if amount_paid == 12:
        print("Platinum Wash")

# Car_Wash(6)
# Car_Wash(12)

# withdraw money

def widthdraw_monney(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance    

balance = widthdraw_monney(100, 85)

print("The balance is", balance)

# Challenge

def fav_city(name):
    if (name == "Fav City"):
        print("Yes! Fav City is my Fav City")
    else: 
        print("Nope")

fav_city("no")
fav_city("no")
fav_city("Fav City")