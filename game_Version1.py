import random

player = {
    "name": "",
    "health": 100,
    "gold": 20,
    "inventory": ["Torch"],
    "location": "Village",
    "offense":10,
    "travel_count": 0
}

locations = ["Village", "Forest", "Cave", "Castle"]
treasures = ["Ruby","Emerald","Diamond","Gold Coin","Magic Ring"]
enemies = {
    "Forest": {"name":"Wolf","health":30},
    "Cave": {"name":"Goblin","health":45},
    "Castle": {"name":"Dragon","health":80}
}

final_boss = {"name":"Shadow Lord","health":120}

def show_stats():
    print("\n------ PLAYER ------")
    print("Name:", player["name"])
    print("Health:", player["health"])
    print("Gold:", player["gold"])
    print("Location:", player["location"])
    print("Offense:", player["offense"])
    print("Travels:", player["travel_count"])
    print("Inventory:", ", ".join(player["inventory"]))

def travel():
    print("\nWhere would you like to go?")
    for place in locations:
        if place != player["location"]:
            print("-", place)
    choice = input("> ").strip().title()
    if choice in locations:
        player["location"] = choice
        player["travel_count"] += 1
        print("You travel to the", choice + ".")
        
        if player["travel_count"] >= 10:
            print("\n⚠️ A shadow falls over the land...")
            print("The Shadow Lord emerges from the darkness!")
            battle_final_boss()
        elif choice in enemies:
            battle(choice)
    else:
        print("That location doesn't exist.")

def battle(place):
    enemy = enemies[place].copy()
    print(f"\nA {enemy['name']} attacks!")
    print(f"{enemy['name']} Health: {enemy['health']}")
    while enemy["health"] > 0 and player["health"] > 0:
        action = input("Attack or Run? ").strip().lower()
        if action == "attack":
            damage = random.randint(player["offense"], player["offense"]+10)
            enemy["health"] -= damage
            print(f"You deal {damage} damage!")
            print(f"{enemy['name']} Health: {max(enemy['health'],0)}")
            if enemy["health"] <= 0:
                print("You defeated the", enemy["name"])
                player["gold"] += random.randint(10,30)
                loot=random.choice(treasures)
                player["inventory"].append(loot)
                drop=animal_drops.get(enemy["name"])
                if drop:
                    player["inventory"].append(drop)
                    print(f"{enemy['name']} dropped: {drop}")
                return
            
            # Increased damage for Goblin and Dragon
            if enemy["name"] == "Goblin":
                ed = random.randint(12, 25)
            elif enemy["name"] == "Dragon":
                ed = random.randint(20, 35)
            else:
                ed = random.randint(5, 18)
            
            player["health"] -= ed
            print(f"The {enemy['name']} hits you for {ed} damage.")
            print(f"Your health is now {player['health']}/100")
        elif action == "run":
            return
        else:
            print("Invalid action.")
    if player["health"] <= 0:
        print("Game Over!")
        raise SystemExit

def battle_final_boss():
    boss = final_boss.copy()
    print(f"\nShadow Lord Health: {boss['health']}")
    while boss["health"] > 0 and player["health"] > 0:
        action = input("Attack or Run? ").strip().lower()
        if action == "attack":
            damage = random.randint(player["offense"], player["offense"]+10)
            boss["health"] -= damage
            print(f"You deal {damage} damage!")
            print(f"Shadow Lord Health: {max(boss['health'],0)}")
            if boss["health"] <= 0:
                print("\n✨ You have defeated the Shadow Lord!")
                print("The land is saved! YOU WIN!")
                raise SystemExit
            
            # Boss does heavy damage
            ed = random.randint(25, 40)
            player["health"] -= ed
            print(f"The Shadow Lord strikes you for {ed} damage!")
            print(f"Your health is now {player['health']}/100")
        elif action == "run":
            print("You cannot escape the Shadow Lord!")
        else:
            print("Invalid action.")
    if player["health"] <= 0:
        print("Game Over! The Shadow Lord has defeated you.")
        raise SystemExit

animal_drops={
    "Wolf":"Wolf Pelt",
    "Goblin":"Goblin Ear",
    "Dragon":"Dragon Scale"
}

def sell_items():
    if player["location"]!="Village":
        print("You can only sell items in the Village.")
        return
    prices={"Wolf Pelt":15,"Goblin Ear":20,"Dragon Scale":100,
            "Ruby":40,"Emerald":50,"Diamond":75,"Gold Coin":10,"Magic Ring":200}
    sold=False
    for item in player["inventory"][:]:
        if item in prices:
            player["inventory"].remove(item)
            player["gold"]+=prices[item]
            print(f"Sold {item} for {prices[item]} gold.")
            sold=True
    if not sold:
        print("You have nothing to sell.")

def shop():
    if player["location"] != "Village":
        print("There is no shop here.")
        return
    print(f"\nYou have {player['gold']} gold.")
    print("1. Potion (15 gold)")
    print("2. Sword (40 gold)")
    print("3. Leave")
    c=input("> ")
    if c=="1":
        if player["gold"]>=15:
            player["gold"]-=15
            player["health"]=min(100,player["health"]+30)
            print("You bought a Potion.")
        else:
            print("You can't afford a Potion.")
    elif c=="2":
        if player["gold"]>=40:
            player["gold"]-=40
            player["inventory"].append("Sword")
            player["offense"] += 10
            print(f"You bought a Sword! Offense increased to {player['offense']}.")
        else:
            print("You can't afford a Sword.")

print("TEXT ADVENTURE GAME")
player["name"]=input("Enter your name: ").strip().title()
while True:
    print("\n1.Travel\n2.Shop\n3.Stats\n4.Inventory\n5.Sell Items\n6.Quit")
    c=input("> ").strip()
    if c=="1":
        travel()
    elif c=="2":
        shop()
    elif c=="3":
        show_stats()
    elif c=="4":
        print(", ".join(player["inventory"]))
    elif c=="5":
        sell_items()
    elif c=="6":
        break
    else:
        print("Invalid choice.")
    if "Magic Ring" in player["inventory"] and player["location"]=="Castle":
        print("You win!")
        break