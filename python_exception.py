
# Exceptional Weather Forecast

# Task 1: Start
# Task 2: Temperature conversion
# Task 3: User Experience

def temp():
    try:
        while True:
            user_input = input("Hello there!! Welcome to JDoggs Temperature Helper!\nDo you prefer Celsius or Farenheit? Type 'C', 'F', or 'quit' to quit. ")
            if user_input == "quit":
                break
            while user_input == "F":
                try:
                    user_input = int(input(f"What is the temperature where you are? Type '0000' to go back. "))
                    if user_input == 0000:
                        break
                    else:
                        celsius = (user_input - 32) * (5 / 9)
                        print(f"The temperature is {user_input}°F, and {celsius}°C where you are!")
                except:
                    if user_input is not True:
                        print("Woops numbers only please!")
            while user_input == "C":
                try:
                    user_input = int(input(f"What is the temperature where you are? Type '0000' to go back. "))
                    if user_input == 0000:
                        break
                    else:
                        farenheit = (user_input * (9/5)) + 32
                        print(f"The temperature is {user_input}°C, and {farenheit}°F where you are!")
                except:
                    if user_input is not True:
                        print("Woops numbers only please!")
    finally:
        print("Thanks for using JDoggs Temperature Helper!")

temp()


 