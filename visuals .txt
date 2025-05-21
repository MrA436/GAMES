import random as r

# List of words
words = ['devloper', 'human', 'bullet', 'millionaire', 'animal', 'birds']

# Choose a random word
word = r.choice(words)
length = len(word)

# Hangman stages (for visuals) - define BEFORE game loop
stages = [
    """
     _______
     |     |
     |     
     |    
     |    
     |
    =========
    😀 Lives left: 5
    """,
    """
     _______
     |     |
     |     O
     |     |
     |    
     |
    =========
    😐 Lives left: 4
    """,
    """
     _______
     |     |
     |     O
     |    /|
     |    
     |
    =========
    😰 Lives left: 3
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |    
     |
    =========
    😨 Lives left: 2
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |    / 
     |
    =========
    😵 Lives left: 1
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |    / \\
     |
    =========
    💀 Lives left: 0
    """
]


# Game state variables
lives = 5
guessed_letters = []
display = ["_" for _ in word]

# Game loop
while lives > 0 and '_' in display:
    print(stages[5 - lives])  # Show hangman stage at the start of loop
    print(' '.join(display))
    
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        # Reveal all instances of guessed letter in the display
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("✅ Correct!")
    else:
        lives -= 1
        print("❌ Incorrect!")

# Final display and result
print(stages[5 - lives])
print(' '.join(display))

if '_' not in display:
    print("🎉 You win!")
else:
    print("💀 You lost! The word was:", word)
