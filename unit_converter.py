# Length Unit Converter

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
    exit()

from_unit = input("From unit (mm, cm, m, km): ").lower()

to_unit = input("To unit (mm, cm, m, km): ").lower()

if from_unit not in length_units:
    print("Invalid unit.")
    exit()

if to_unit not in length_units:
    print("Invalid unit.")
    exit()

# Convert to meters
meters = value * length_units[from_unit]

# Convert from meters to destination
result = meters / length_units[to_unit]

print(f"\nResult: {result} {to_unit}")

# Weight Unit Converter

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
    exit()

from_unit = input("From unit (g, kg, mg, ton, lb, oz): ").lower()

to_unit = input("To unit (g, kg, mg, ton, lb, oz): ").lower()

if from_unit not in weight_units:
    print("Invalid unit.")
    exit()

if to_unit not in weight_units:
    print("Invalid unit.")
    exit()

#convert to kilograms
kilograms = value * weight_units[from_unit]

#convert from kilograms to destinations
result = kilograms / weight_units[to_unit]

print(f"\nResult: {result} {to_unit}")


#temperature unit convertor

temperature_units = {
    "C" : "Celsius",
    "F" : "Fahrenheit",
    "K" : "Kelvin",

}

try:
    value = float(input("Enter temperature: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

from_unit = input("From (C/F/K): ").upper()
to_unit = input("To (C/F/K): ").upper()

if from_unit == "C":
    celsius = value

elif from_unit == "F":
    celsius = (value - 32) * 5 / 9

elif from_unit == "K":
    celsius = value - 273.15
else:
    print("Invalid unit")
    exit()

if to_unit == "C":
    result = celsius

elif to_unit == "F":
    result = (celsius * 9 / 5) + 32

elif to_unit == "K":
    result = celsius + 273.15

else:
    print("Invalid unit")
    exit()

print(f"Result: {result:.2f} {to_unit}")