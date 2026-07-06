import time
print("welcome to the online pet game, you must try to keep your pet alive for as much time as possible.")
print()
print()
print("you must keep your pet happy, fed, and healthy")
print()
print("if any stats hit 0, your pet will lose 30 health")
print()
print("the stats all have a max of 100 and a min of 0")
print()
print()
print("good luck!")
time.sleep(10)
score = 0
days = 0
hunger = 80
happiness = 80
health = 100
name = input("what is your pets name? ")
pet_type = input("what type of pet is it? (dog/cat/dragon) ").strip().lower()
while pet_type not in ["dog", "cat", "dragon"]:
    print("Invalid pet type. Please choose from dog, cat, or dragon.")
    pet_type = input("what type of pet is it? (dog/cat/dragon) ").strip().lower()
if pet_type == "dog":
    print("you have a cute pet dog!")
elif pet_type == "cat":
    print("you have a cute pet cat!")
elif pet_type == "dragon":
    print("you have a firey pet dragon!")
while 5 == 5:
    print(f"Day {days}:")

    print("hunger:", "x" * (hunger // 10), f"({hunger})")
    print("happiness:", "x" * (happiness // 10), f"({happiness})")
    print("health:", "x" * (health // 10), f"({health})")
    print()
    action = input("What would you like to do? (feed/play/sleep) ").strip().lower()
    if action == "feed":
        print()
        print(f"You chose to feed {name}.")
        print()
        print(f"{name} is eating...")
        print()
        time.sleep(2)
        hunger = min(hunger + 30, 100)
        happiness = min(happiness - 10, 100)
        health = min(health -10, 100)
        print(f"You fed {name}. Hunger is now", "x" * (hunger // 10), f"({hunger}), Happiness is now", "x" * (happiness // 10), f"({happiness}), Health is now", "x" * (health // 10), f"({health}).")
    elif action == "play":
        print()
        print("you are playing with your pet.")
        time.sleep(2)
        happiness = min(happiness + 20, 100)
        hunger = max(hunger - 20, 0)
        health = min(health -10, 100)
        print()
        print(f"You played with {name}. Happiness is now", "x" * (happiness // 10), f"({happiness}), Hunger is now", "x" * (hunger // 10), f"({hunger}), Health is now", "x" * (health // 10), f"({health}).")
    elif action == "sleep":
        print()
        print(" your pet is sleeping")
        time.sleep(3)
        print()
        hunger = max(hunger - 10, 0)
        happiness = max(happiness - 10, 0)
        health = min(health + 20, 100)
        print(f"You put {name} to sleep. Hunger is now", "x" * (hunger // 10), f"({hunger}), Happiness is now", "x" * (happiness // 10), f"({happiness}), Health is now", "x" * (health // 10), f"({health}).")
    else:
        print()
        print("Invalid action. Please choose feed, play, or sleep.")
    if hunger <= 0 or happiness <= 0:
        health -= 50
        print()
        print(f"{name} is not doing well! Health decreased to", "x" * (health // 10), f"({health}).")
    if hunger <=20 and hunger >= 0:
        health -= 10
        print()
        print(f"{name} is getting hungry! Please feed it! Health decreased to", "x" * (health // 10), f"({health}).")
    if happiness <=20 and happiness >= 0:
        health -= 10
        print()
        print(f"{name} is getting sad! Please play with it! Health decreased to", "x" * (health // 10), f"({health}).")
    health = min(health, 100)
    print()
    end = input("Do you want to continue to the next day? (yes/no) ").strip().lower()
    if end == "no":
        print(f"You ended the game on day {days}. {name}'s final stats - Hunger:", "x" * (hunger // 10), f"({hunger}), Happiness:", "x" * (happiness // 10), f"({happiness}), Health:", "x" * (health // 10), f"({health}).")
        print(f"Your final score is {score} points.")
        if score <= 500:
            print("You did not do well/ended the run too early!. Try again!")
        elif score <= 1000:
            print("You did okay! Try again to get a better score!")
        elif score <= 2000:
            print("You did well! Try again to get a better score!")
        elif score <= 3000:
            print("You did very well! one of the best i've seen!")
        elif score <= 5000:
            print("You did excellent! You're a pet parenting master!")
        else:
            print("You did amazing! You're a pet parenting legend!")
        break
    else:
        if pet_type == "dog":
            print()
            print(f"{name} is a happy dog! It wags its tail and barks happily. (doesn't lose hunger at the end of the day)")
            health = min(health - 10, 100)
            hunger = min(hunger - 10, 100)
            print("your pets stats are now - Hunger:", "x" * (hunger // 10), f"({hunger}), Happiness:", "x" * (happiness // 10), f"({happiness}), Health:", "x" * (health // 10), f"({health}).")
        elif pet_type == "cat":
            print()
            print(f"{name} is a curious cat, it doesn't need you to keep it happy. (doesn't lose happiness at the end of the day)")
            health = min(health - 10, 100)
            hunger = min(hunger - 10, 100)
            print()
            print("your pets stats are now - Hunger:", "x" * (hunger // 10), f"({hunger}), Happiness:", "x" * (happiness // 10), f"({happiness}), Health:", "x" * (health // 10), f"({health}).")

        elif pet_type == "dragon":
            print()
            print(f"{name} is a resilient fire breathing dragon. It doesn't lose health at the end of the day.")
            hunger = min(hunger - 10, 100)
            happiness = min(happiness - 10, 100)
            print("your pets stats are now - Hunger:", "x" * (hunger // 10), f"({hunger}), Happiness:", "x" * (happiness // 10), f"({happiness}), Health:", "x" * (health // 10), f"({health}).")
        print(f"Continuing to day {days + 1}...")
        time.sleep(2)
    days += 1
    score += 100
    if health <= 0:
        print()
        print(f"{name} has passed away. Game over. you get 0 points. your pet lasted for {days} days.")
        break
