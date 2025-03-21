

# Dictionary storing gravitational force relative to Earth
GRAVITY_FACTORS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def calculate_weight(earth_weight, planet):
    """Calculates the weight on a given planet based on its gravity factor."""
    return round(earth_weight * GRAVITY_FACTORS[planet], 2)

def main():
    """Main function to get user input and display equivalent weight on another planet."""
    earth_weight = float(input("Enter your weight on Earth: "))
    planet = input("Enter a planet: ")

    if planet in GRAVITY_FACTORS:
        planetary_weight = calculate_weight(earth_weight, planet)
        print(f"The equivalent weight on {planet}: {planetary_weight}")
    else:
        print("Invalid planet name. Please enter a valid planet from the solar system.")

if __name__ == "__main__":
    main()
