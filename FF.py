#Load possible logins 
Logins = {
    "Alice": {"password": "password123", "points": 100, "level": "Bronze"},
    "Bob": {"password": "securepass", "points": 150, "level": "Silver"},
    "Charlie": {"password": "charliepw", "points": 200, "level": "Gold"},
    "Diana": {"password": "diana2025", "points": 250, "level": "Platinum"},
    "Eve": {"password": "evepass", "points": 300, "level": "Diamond"}
}

def get_level(points):
    if points >= 300:
        return "Diamond"
    elif points >= 250:
        return "Platinum"
    elif points >= 200:
        return "Gold"
    elif points >= 150:
        return "Silver"
    else:
        return "Bronze"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username in Logins and Logins[username]["password"] == password:
    print("Login successful!")
    customer = True
    points = Logins[username]["points"]
    level = Logins[username]["level"]
    print(f"{username} has {points} points and is at level {level}.")
else:
    print("Invalid username or password. Goodbye.")
    exit(1)

# If login is successful, proceed with the rest of the program
print("Welcome to the rewards program!")
while customer:
    print("\nMenu:")
    print("1. View Points")
    print("2. Redeem Points")
    print("3. Spend Points")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print(f"You have {points} points and your level is {level}.")
    elif choice == "2":
        redeem_points = int(input("Enter points to redeem: "))
        points += redeem_points
        level = get_level(points)
        Logins[username]["points"] = points  # Update points in the login dictionary
        Logins[username]["level"] = level    # Update level in the login dictionary
        print(f"Redeemed {redeem_points} points. You now have {points} points and your level is {level}.")
    elif choice == "3":
        print("\nItems you can buy with points:")
        items = {
            "A": {"name": "Coffee Mug", "cost": 50},
            "B": {"name": "T-Shirt", "cost": 120},
            "C": {"name": "Gift Card", "cost": 200}
        }
        for key, item in items.items():
            print(f"{key}. {item['name']} - {item['cost']} points")
        item_choice = input("Select an item to buy (A/B/C) or type 'back' to return: ").upper()
        if item_choice in items:
            if points >= items[item_choice]["cost"]:
                points -= items[item_choice]["cost"]
                level = get_level(points)
                Logins[username]["points"] = points
                Logins[username]["level"] = level
                print(f"You bought a {items[item_choice]['name']}! You now have {points} points and your level is {level}.")
            else:
                print("Not enough points to buy this item.")
        elif item_choice == "BACK":
            continue
        else:
            print("Invalid selection.")
    elif choice == "4":
        print("Exiting the program. Thank you!")
        customer = False
    else:
        print("Invalid choice, please try again.")

# End of the program
print("Goodbye!")
