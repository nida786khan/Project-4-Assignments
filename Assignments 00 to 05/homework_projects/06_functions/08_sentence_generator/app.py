def make_sentence(word: str, part_of_speech: int):
    """
    Generates a sentence using the given word based on its part of speech.
    """
    sentences = {
        0: f"I am thrilled to add this {word} to my incredible collection!",
        1: f"Wow, what a beautiful day! It makes me want to {word} right now!",
        2: f"Through my window, I see the sky is so wonderfully {word}!"
    }
    
    print(sentences.get(part_of_speech, "Oops! Please enter 0 for noun, 1 for verb, or 2 for adjective."))

def main():
    word = input("Please enter a word (noun, verb, or adjective): ")
    print("What type of word is this?")
    try:
        part_of_speech = int(input("Type 0 for noun, 1 for verb, or 2 for adjective: "))
        make_sentence(word, part_of_speech)
    except ValueError:
        print("Invalid input! Please enter a number (0, 1, or 2).")

if __name__ == '__main__':
    main()
