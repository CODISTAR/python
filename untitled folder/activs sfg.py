# 1) Ask for the temperature
temp_input = input("Enter today's temperature in Celsius: ")
temperature = int(temp_input)

# 2) Choose the main outfit
if temperature < 20:
    outfit = "jacket"
else:
    outfit = "t-shirt"

# 3) Ask about rain
is_raining = input("Is it raining? (yes/no): ").strip().lower()

# 4) Add an umbrella reminder
if is_raining == "yes":
    print("Reminder: Don't forget to bring an umbrella!")

# 5) Ask for wind speed
wind_input = input("Enter the wind speed in km/h: ")
wind_speed = int(wind_input)

# 6) Decide about a windbreaker
if wind_speed > 30:
    needs_windbreaker = "Yes, you need a windbreaker."
else:
    needs_windbreaker = "No, the weather is calm."

# 7) Ask about puddles
has_puddles = input("Are there puddles on the ground? (yes/no): ").strip().lower()

# 8) Choose the shoes
if has_puddles == "yes":
    shoes = "boots"
else:
    shoes = "sneakers"

# 9) Print the completion message
print()  # Blank line
print("Weather check is complete.")

# 10) Print the final outfit summary
print("\n=== WEATHER OUTFIT PICKER ===")
print(f"Temperature: {temperature}°C")
print(f"Main Outfit: {outfit}")
print(f"Rain Status: {is_raining}")
print(f"Windbreaker: {needs_windbreaker}")
print(f"Shoes: {shoes}")
print("=============================")
