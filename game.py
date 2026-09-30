import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    MAX_GUESSES = 6
    SUPPORTED_LENGTHS = (4, 5, 6)

    def __init__(self, length=5):
        self.length = length
        self.history = []

        if length not in self.SUPPORTED_LENGTHS:
            self.target = None
            return

        candidates = [word for word in WORDS if len(word) == length]
        self.target = random.choice(candidates) if candidates else None

    def display_history(self):
        print("Guess history:")
        if not self.history:
            print("  No accepted guesses.")
            return

        for guess, feedback in self.history:
            print(f"  {guess}: {' '.join(feedback)}")

    def display_summary(self, outcome):
        guess_count = len(self.history)

        if outcome == "won":
            print(f"You won in {guess_count} accepted guess(es)!")
        elif outcome == "lost":
            print(
                f"You lost after {guess_count} accepted guesses. "
                f"The word was: {self.target}"
            )
        elif outcome == "quit":
            print(f"Game quit after {guess_count} accepted guess(es).")

    def run(self):
        if self.target is None:
            print(f"No {self.length}-letter words are available.")
            return

        print(f"Wordle — {self.length} letters, {self.MAX_GUESSES} guesses.")
        accepted_guesses = 0

        while accepted_guesses < self.MAX_GUESSES:
            guess = input("> ").strip().lower()

            if guess == "q":
                self.display_summary("quit")
                return

            if len(guess) != self.length or not guess.isalpha():
                print("Enter a valid word of the required length.")
                continue

            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))
            accepted_guesses += 1

            self.display_history()

            if guess == self.target:
                self.display_summary("won")
                return

        self.display_summary("lost")