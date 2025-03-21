# Constants for gravitational force relative to Earth
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
    """Calculates weight on a given planet using gravity factors."""
    if planet in GRAVITY_FACTORS:
        return round(earth_weight * GRAVITY_FACTORS[planet], 2)
    else:
        return None  # Returns None for invalid planets

def main():
    """Main function to get user input and display planetary weight."""
    try:
        earth_weight = float(input("Enter your weight on Earth: "))
        planet = input("Enter a planet: ")

        planetary_weight = calculate_weight(earth_weight, planet)

        if planetary_weight is not None:
            print(f"The equivalent weight on {planet}: {planetary_weight}")
        else:
            print("Invalid planet name. Please enter a valid planet from the solar system.")

    except ValueError:
        print("Please enter a valid numerical weight.")

if __name__ == "__main__":
    main()
