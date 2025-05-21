import random as r
def hangman_game():
    # 1st chunk - adding the words
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    word = r.choice(words)

    # 2nd chunk - Game state
    lives = 5
    guessed_letters = []
    display = ["_" for _ in word]

    # Hangman stages (Unicode-enhanced visuals)
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
         |     😐
         |     │
         |    
         |
        =========
        😐 Lives left: 4
        """,
        """
         _______
         |     |
         |     😰
         |    ╱│
         |    
         |
        =========
        😰 Lives left: 3
        """,
        """
         _______
         |     |
         |     😨
         |    ╱│╲
         |    
         |
        =========
        😨 Lives left: 2
        """,
        """
         _______
         |     |
         |     😵
         |    ╱│╲
         |    ╱ 
         |
        =========
        😵 Lives left: 1
        """,
        """
         _______
         |     |
         |     💀
         |    ╱│╲
         |    ╱ ╲
         |
        =========
        💀 Lives left: 0
        """
    ]

    # 3rd chunk - Game loop
    while lives > 0 and '_' in display:
        print(stages[5 - lives])  # Show hangman stage
        print(' '.join(display))

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            # Reveal all instances of guessed letter
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
            print("✅ Correct!")
        else:
            lives -= 1
            print("❌ Incorrect!")

    # Final stage display and result
    print(stages[5 - lives])
    print(' '.join(display))

    if '_' not in display:
        print("🎉 You win!")
    else:
        print("💀 You lost! The word was:", word)

# Replay option to play the game multiple times
while True:
    hangman_game()
    replay = input("Do you want to play again? (y/n): ").lower()
    if replay != 'y':
        print("Thanks for playing! Goodbye!")
        break
