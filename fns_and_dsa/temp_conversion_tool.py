# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temperature_input = input("Enter the temperature to convert: ")
    unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ")

    # Validate temperature input
    try:
        temperature = float(temperature_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Conversion logic
    if unit.upper() == "F":
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted:.2f}°C")

    elif unit.upper() == "C":
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted:.2f}°F")

    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
