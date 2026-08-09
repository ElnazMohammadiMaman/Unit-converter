# Unit Converter

A simple unit converter written in Python.

This project can convert different measurement units including **length**, **weight**, and **temperature**. It was created to practice Python fundamentals and improve the structure of a small Python project.

## Features

### Length Converter

Supported units:

* Millimeter (mm)
* Centimeter (cm)
* Meter (m)
* Kilometer (km)

### Weight Converter

Supported units:

* Milligram (mg)
* Gram (g)
* Kilogram (kg)
* Ton
* Pound (lb)
* Ounce (oz)

### Temperature Converter

Supported units:

* Celsius (C)
* Fahrenheit (F)
* Kelvin (K)

## Error Handling

The program handles:

* Invalid number inputs
* Invalid unit inputs
* Invalid menu choices

If an invalid unit is entered, the program asks the user to try again instead of stopping.

## Menu System

The program uses a menu that allows the user to choose which type of conversion they want to perform.

After completing a conversion, the user can return to the main menu and perform another conversion or exit the program.

## Technologies Used

* Python 3

## How to Run

1. Clone this repository:

```bash
git clone your-repository-link
```

2. Run the program:

```bash
python unit_converter.py
```

## What I Learned

While building this project, I practiced:

* Functions
* Variables and data types
* Dictionaries
* `if / elif / else` statements
* `while` loops
* User input handling
* Type conversion using `float`
* Exception handling using `try / except`
* `return` and `break`
* String formatting using f-strings
* Unit conversion logic
* Reusing functions to reduce repeated code

## Project Structure

The project is organized into separate functions for each type of conversion:

* `length_converter()`
* `weight_converter()`
* `temperature_converter()`
* `get_valid_unit()`

The `get_valid_unit()` function is used to validate unit inputs and reduce repeated code between the different converters.

## Project Status

Version 2.0

The project has been updated from the original basic converter to include functions, a menu system, input validation, error handling, and reusable code.

Created by Elnaz Mohammadi