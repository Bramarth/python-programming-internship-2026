
import random

# ==========================================
# HANGMAN WORD GUESSING GAME
# ==========================================

# Word bank
WORDS = [
    "python", "computer", "programming", "education",
    "keyboard", "software", "developer", "internet",
    "database", "technology", "algorithm", "application",
    "network", "hardware", "website", "security",
    "artificial", "intelligence", "cybersecurity",
    "information", "communication", "processor",
    "operating", "system", "monitor", "printer",
    "smartphone", "laptop", "tablet", "android",
    "javascript", "variable", "function", "iteration",
    "condition", "firewall", "encryption", "password",
    "wireless", "bluetooth", "digital", "innovation",
    "research", "university", "student", "teacher",
    "classroom", "curriculum", "learning", "knowledge",
    "assessment", "assignment", "examination",
    "mathematics", "science", "geography", "biology",
    "chemistry", "physics", "literature", "history",
    "management", "leadership", "business", "marketing",
    "finance", "economics", "project", "planning",
    "development", "analysis", "design", "testing",
    "debugging", "interface", "browser", "download",
    "upload", "document", "spreadsheet", "presentation",
    "graphics", "animation", "simulation", "robotics",
    "automation", "machine", "electricity", "energy",
    "environment", "agriculture", "hospital", "medicine",
    "community", "government", "democracy", "freedom",
    "culture", "society", "friendship", "happiness",
    "success", "challenge", "opportunity", "confidence",
    "creativity", "discipline", "determination",
    "achievement", "experience", "adventure", "mountain",
    "elephant", "butterfly", "beautiful", "chocolate",
    "sandwich", "telephone", "airplane", "bicycle",
    "football", "basketball", "volleyball", "champion",
    "victory", "diamond", "rainbow", "sunshine", "universe"
]

# Remove duplicate words
WORDS = list(set(WORDS))


# ==========================================
# HANGMAN ASCII ART
# ==========================================

HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
     =========
    """,
    """
       +---+
       |   |
      \\O   |
       |   |
      / \\  |
           |
     =========
    """,
    """
       +---+
       |   |
      \\O/  |
       |   |
      / \\  |
           |
     =========
    """
]


# ==========================================
# DIFFICULTY LEVELS
# ==========================================

DIFFICULTIES = {
    "1": ("Easy", 8),
    "2": ("Medium", 6),
    "3": ("Hard", 4)
}


# ==========================================
# DISPLAY THE HIDDEN WORD
# ==========================================

def display_word(secret_word, guessed_letters):

    display = []

    for letter in secret_word:

        if letter in guessed_letters:
            display.append(letter.upper())
        else:
            display.append("_")

    return " ".join(display)


# ==========================================
# SELECT DIFFICULTY
# ==========================================

def select_difficulty():

    print("\nSELECT DIFFICULTY")
    print("1. Easy   - 8 incorrect attempts")
    print("2. Medium - 6 incorrect attempts")
    print("3. Hard   - 4 incorrect attempts")

    while True:

        choice = input("\nChoose difficulty (1-3): ").strip()

        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]

        print("Invalid choice. Please select 1, 2 or 3.")


# ==========================================
# DISPLAY GAME INFORMATION
# ==========================================

def display_game_status(secret_word, guessed_letters,
                        guessed_words, incorrect_guesses,
                        max_attempts):

    # Scale gallows according to difficulty
    stage = round(
        (incorrect_guesses / max_attempts) *
        (len(HANGMAN_STAGES) - 1)
    )

    print(HANGMAN_STAGES[stage])

    print("WORD:", display_word(secret_word, guessed_letters))

    print("\nIncorrect guesses:", incorrect_guesses)
    print("Attempts remaining:", max_attempts - incorrect_guesses)

    print(
        "Guessed letters:",
        ", ".join(sorted(guessed_letters))
        if guessed_letters else "None"
    )

    print(
        "Previous word guesses:",
        ", ".join(sorted(guessed_words))
        if guessed_words else "None"
    )


# ==========================================
# MAIN GAME FUNCTION
# ==========================================

def play_game():

    secret_word = random.choice(WORDS)

    guessed_letters = set()
    guessed_words = set()

    incorrect_guesses = 0

    difficulty, max_attempts = select_difficulty()

    print("\n" + "=" * 40)
    print("          HANGMAN GAME")
    print("=" * 40)

    print("Difficulty:", difficulty)
    print("Guess the hidden word one letter at a time.")
    print("You can also guess the entire word.")
    print("=" * 40)

    # Main game loop
    while incorrect_guesses < max_attempts:

        display_game_status(
            secret_word,
            guessed_letters,
            guessed_words,
            incorrect_guesses,
            max_attempts
        )

        guess = input("\nEnter a letter or word: ").lower().strip()

        # Validate empty input
        if not guess:
            print("Input cannot be empty.")
            continue

        # Validate letters only
        if not guess.isalpha():
            print("Invalid input! Please enter letters only.")
            continue

        # ==================================
        # WHOLE WORD GUESSING
        # ==================================

        if len(guess) > 1:

            if guess in guessed_words:
                print("You have already guessed that word!")
                continue

            guessed_words.add(guess)

            # Check the entire word
            if guess == secret_word:

                print("\n" + "=" * 40)
                print("       CONGRATULATIONS!")
                print("=" * 40)
                print("Correct word:", secret_word.upper())
                print("YOU WON!")
                print("=" * 40)

                return True

            else:

                print("Incorrect word guess!")
                incorrect_guesses += 1
                continue

        # ==================================
        # SINGLE LETTER GUESSING
        # ==================================

        if guess in guessed_letters:

            print("You have already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:

            print("Correct guess!")

        else:

            print("Wrong guess!")
            incorrect_guesses += 1

        # ==================================
        # CHECK FOR VICTORY
        # ==================================

        if all(letter in guessed_letters for letter in secret_word):

            print("\n" + "=" * 40)
            print("       CONGRATULATIONS!")
            print("=" * 40)
            print("The correct word was:", secret_word.upper())
            print("YOU WON!")
            print("=" * 40)

            return True

    # ======================================
    # DEFEAT SCREEN
    # ======================================

    print(HANGMAN_STAGES[-1])

    print("\n" + "=" * 40)
    print("            GAME OVER!")
    print("=" * 40)

    print("You have used all your attempts.")
    print("The correct word was:", secret_word.upper())

    print("Better luck next time!")
    print("=" * 40)

    return False


# ==========================================
# MAIN PROGRAM AND REPLAY SYSTEM
# ==========================================

def main():

    wins = 0
    losses = 0
    rounds = 0

    print("\n************************************")
    print("       WELCOME TO HANGMAN")
    print("************************************")

    while True:

        result = play_game()

        rounds += 1

        if result:
            wins += 1
        else:
            losses += 1

        print("\n========== GAME STATISTICS ==========")
        print("Rounds played:", rounds)
        print("Games won:", wins)
        print("Games lost:", losses)
        print("=====================================")

        while True:

            replay = input("\nWould you like to play again? (yes/no): ")
            replay = replay.lower().strip()

            if replay in ["yes", "y"]:
                break

            elif replay in ["no", "n"]:

                print("\nThank you for playing Hangman!")

                print("\nFINAL STATISTICS")
                print("Total rounds:", rounds)
                print("Total wins:", wins)
                print("Total losses:", losses)

                print("\nGoodbye!")
                return

            else:
                print("Please enter yes or no.")


# ==========================================
# START THE GAME
# ==========================================

if __name__ == "__main__":
    main()
