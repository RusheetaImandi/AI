import random
import string

def get_most_frequent_letter(word, guessed_letters):
    letter_frequencies = {}
    for letter in word:
        if letter not in guessed_letters:
            letter_frequencies[letter] = letter_frequencies.get(letter, 0) + 1
    return max(letter_frequencies, key=letter_frequencies.get) if letter_frequencies else None

def display_word(word, guessed_letters):
    """Displays the word with guessed letters revealed."""
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman_game():
    words = ["python", "intelligent", "machine", "learning", "hangman"]
    word_to_guess = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_body_parts = 6
    
    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))
    
    while incorrect_guesses < max_body_parts and set(word_to_guess) != guessed_letters:
        guess = get_most_frequent_letter(word_to_guess, guessed_letters)
        if not guess:
            break  # No more guesses possible
        
        print(f"AI Player 1 guesses: {guess}")
        guessed_letters.add(guess)
        
        if guess in word_to_guess:
            print("Correct Guess! Removing a body part.")
        else:
            incorrect_guesses += 1
            print(f"Wrong Guess! Adding a body part. ({incorrect_guesses}/{max_body_parts})")
        
        print(display_word(word_to_guess, guessed_letters))
        print("-" * 20)
    
    if set(word_to_guess) == guessed_letters:
        print("AI Player 1 Wins! Word Completed: ", word_to_guess)
    else:
        print("AI Player 2 Wins! AI Player 1 Failed to Guess the Word.")
        print("The word was: ", word_to_guess)

# Run the game
hangman_game()
