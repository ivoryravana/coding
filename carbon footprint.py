carbon = 0

bus = float(input("enter how many times you take the bus in a day: "))
computer = float(input("enter how many hours do you use the computer in a day: "))
showers = float(input("enter how many showers do you take in a day: "))
meals = float(input("enter how many meals do you cook in a day: "))
stove = input("what kind of stove do you have (induction, electric, gas)? ").strip().lower()
if stove == "induction":
    print("induction stoves have the lowest carbon footprint, good job.")
    carbon += meals * 0.33
elif stove == "electric":
    carbon += meals * 0.66
    print("electric stoves are better than gas stoves, but induction stoves are the best. Consider changing to an induction stove.")
elif stove == "gas":
    carbon += meals * 0.992
    print("gas stoves have the highest carbon footprint. Consider changing to an induction stove.")
caruse = float(input("how many miles do you drive in a day: "))
cartype = input("what type of car do you have (electric, hybrid, gas)? ").strip().lower()
if cartype == "electric":
    carbon += caruse * 0.30
    print("electric cars have the lowest carbon footprint, good job.")
elif cartype == "hybrid":
    carbon += caruse * 0.55
    print("you're trying, and thats what counts.")
elif cartype == "gas":
    carbon += caruse * 0.88
    print("gas cars have the highest carbon footprint. Consider changing to an electric car.")

light = float(input("how many hours do you use lights in a day: "))
ac = float(input("how many hours do you use air conditioning in a day: "))
plane = float(input("how many times do you take a plane in a year: "))
ferry = float(input("how many times do you take a ferry on foot in a day: "))
ferrycar = float(input("how many times do you take a ferry in a car in a day: "))
lightrail = float(input("how many times do you take a light rail in a day: "))


carbon += bus * 1.6
carbon += computer * 0.132
carbon += showers * 2.64
carbon += light * 0.045


carbon += ac * 2.5
carbon += plane * 13.88
carbon += ferry * 0.875
carbon += ferrycar * 2.33
carbon += lightrail * 3.0

print("Your total carbon footprint is: " + str(carbon) + " lbs CO2e per day.")
carbon = float(carbon)
if carbon < 50:
    print("Your carbon footprint is low. Keep up the good work!")
elif carbon > 50 and carbon < 100:
    print("Your carbon footprint is moderate. Consider making some changes to reduce it.")

elif carbon > 100 and carbon < 1000:
    print("Your carbon footprint is the highest ive ever seen. turn off everything and go live in the woods.")
if carbon == 0.0:
    print("Your carbon footprint is zero. You are clearly lying. Get a job and stop living in your parents basement.")
