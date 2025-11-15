weather = input("What's the weather like today? (sunny/rainy/cold): ")
What's the weather like today? (sunny/rainy/cold): sunny
weather = weather.lower()
if weather in ["sunny", "rainy", "cold"]:
print(f"The weather today is {weather}.")
 else:
print("Invalid input! Please enter sunny, rainy or cold.")
The weather today is sunny.