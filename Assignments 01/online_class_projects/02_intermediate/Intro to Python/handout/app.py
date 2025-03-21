# Planetary Weight Calculator

# Dictionary storing gravitational percentages relative to Earth
gravity_factors = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Get user input
earth_weight = float(input("Enter your weight on Earth: "))
planet = input("Enter a planet: ")

# Check if planet is in the dictionary
if planet in gravity_factors:
    planetary_weight = round(earth_weight * gravity_factors[planet], 2)
    print(f"The equivalent weight on {planet}: {planetary_weight}")
else:
    print("Invalid planet name. Please enter a valid planet from the solar system.")
