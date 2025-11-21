weather = input("What's the weather like today? (sunny/rainy/cold): ")

if weather in ["sunny", "rainy", "cold"]:
    print(f"The weather today is {weather}.")
else:
    print("Invalid input! Please enter sunny, rainy or cold.")

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
