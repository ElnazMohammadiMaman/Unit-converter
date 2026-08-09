# Length Unit Converter

def length_converter():
    length_units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }
    try:
        value = float(input("Enter value: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    from_unit = get_valid_unit(length_units, "From unit (mm, cm, m, km): ")

    to_unit = get_valid_unit(length_units, "To unit (mm, cm, m, km): ")

    # Convert to meters
    meters = value * length_units[from_unit]

    # Convert from meters to destination
    result = meters / length_units[to_unit]

    print(f"\nResult: {result} {to_unit}")

# Weight Unit Converter


def weight_converter():


    weight_units = {
        "g": 0.001,
        "kg": 1,
        "mg": 0.000001,
        "ton": 1000,
        "lb": 0.453592,
        "oz": 0.0283495
    }

    try:
        value = float(input("Enter value: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    from_unit = get_valid_unit(weight_units, "From unit (g, kg, mg, ton, lb, oz): ")

    to_unit = get_valid_unit(weight_units, "To unit (g, kg, mg, ton, lb, oz): ")


    #convert to kilograms
    kilograms = value * weight_units[from_unit]

    #convert from kilograms to destinations
    result = kilograms / weight_units[to_unit]

    print(f"\nResult: {result} {to_unit}")


#temperature unit convertor

def temperature_converter():

    temperature_units = {
        "C" : "Celsius",
        "F" : "Fahrenheit",
        "K" : "Kelvin",

    }

    try:
        value = float(input("Enter temperature: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    from_unit = get_valid_unit(temperature_units, "From (C/F/K): ", "upper")

    to_unit = get_valid_unit(temperature_units, "To (C/F/K): ", "upper")

    if from_unit == "C":
        celsius = value

    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9

    elif from_unit == "K":
        celsius = value - 273.15
    else:
        print("Invalid unit")
        return

    if to_unit == "C":
        result = celsius

    elif to_unit == "F":
        result = (celsius * 9 / 5) + 32

    elif to_unit == "K":
        result = celsius + 273.15

    else:
        print("Invalid unit")
        return

    print(f"Result: {result:.2f} {to_unit}")

def get_valid_unit(units, message, case="lower"):
    while True:
        unit = input(message)

        if case == "lower":
            unit = unit.lower()
        elif case == "upper":
            unit = unit.upper()

        if unit in units:
            return unit

        print("Invalid unit. Please try again.")

while True:
    print("========================")
    print("      UNIT CONVERTER")
    print("========================")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        length_converter()

    elif choice == "2":
        weight_converter()

    elif choice == "3":
        temperature_converter()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a number from 1 to 4.")