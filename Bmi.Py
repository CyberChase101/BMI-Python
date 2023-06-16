def calculate_bmi(weight, height):
    """
    Calculates the Body Mass Index (BMI) based on weight and height.
    Formula: BMI = (weight / (height^2)) * 703
    """

    # Calculate BMI
    bmi = (weight / (height ** 2)) * 703
    return bmi


def interpret_bmi(bmi):
    """
    Interprets the BMI value and returns the corresponding category.
    """

    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# Prompt user for weight and height input
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in feet: "))

# Convert height to inches
height_inches = height * 12

# Calculate BMI
bmi = calculate_bmi(weight, height_inches)

# Interpret BMI
category = interpret_bmi(bmi)

# Print the result
print("Your BMI is:", round(bmi, 2))
print("Category:", category)
