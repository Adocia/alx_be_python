weather = input("What's the weather like today? (sunny/rainy/cold): ")
What's the weather like today? (sunny/rainy/cold): sunny
weather = weather.lower()
if weather in ["sunny", "rainy", "cold"]:
print(f"The weather today is {weather}.")
else:
print("Invalid input! Please enter sunny, rainy or cold.")
The weather today is sunny.
if weather == "sunny":
print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
print("Don't forger your umbrella and a raincoat.")
elif weather == "cold":
print("Make sure to wear a warm coat and a scarf.")
else:
print("Sorry, I don't have recommendations for this wearth.")
Wear a t-shirt and sunglasses.
