import random

def guess_the_word():
    words = ['python', 'developer', 'algorithm', 'program']
    word = random.choice(words)
    jumbled_word = ''.join(random.sample(word, len(word)))
    
    print(f"Guess the word: {jumbled_word}")
    
    while True:
        guess = input("Your guess: ")
        if guess == word:
            print("Correct! You win!")
            break
        else:
            print("Incorrect. Try again.")

# Run the game
guess_the_word()
