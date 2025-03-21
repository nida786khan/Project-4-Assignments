import random

# Likelihood of stopping (Adjust for testing)
DONE_LIKELIHOOD = 0.3  

def done():
    """Returns True with a probability of DONE_LIKELIHOOD"""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # Function execution yahan hi stop ho jayega
        print(curr_num, end=" ")  # Numbers ek hi line me print karne ke liye end=" "

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")  # \n newline add kiya taake format acha lage

if __name__ == "__main__":
    main()
