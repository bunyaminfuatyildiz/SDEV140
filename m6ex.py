# Write your code here
import random
from breezypythongui import EasyFrame


class GuessingGame(EasyFrame):
    """Plays a guessing game with the user where the computer guesses and user provides hints."""

    def __init__(self):
        """Sets up the window, widgets, and data."""
        EasyFrame.__init__(self, title="Guessing Game")

        self.lower_bound = 1
        self.upper_bound = 100
        self.computer_guess = random.randint(self.lower_bound, self.upper_bound)
        self.count = 0

        # Label to display computer's guess
        self.guess_label = self.addLabel(text=f"Is the number {self.computer_guess}?", row=0, column=0, sticky="NSEW", columnspan=4)

        # Buttons for user hints
        self.too_small = self.addButton(text="Too small", row=1, column=0, command=self.go_large)
        self.too_large = self.addButton(text="Too large", row=1, column=1, command=self.go_small)
        self.correct = self.addButton(text="Correct", row=1, column=2, command=self.go_correct)

        # Button to start a new game
        self.new_game = self.addButton(text="New Game", row=2, column=0, command=self.start_new_game, state="disabled")

    def go_large(self):
        """Updates lower bound based on user hint and displays new guess."""
        self.lower_bound = self.computer_guess + 1
        self.computer_guess = random.randint(self.lower_bound, self.upper_bound)
        self.update_guess_label()

    def go_small(self):
        """Updates upper bound based on user hint and displays new guess."""
        self.upper_bound = self.computer_guess - 1
        self.computer_guess = random.randint(self.lower_bound, self.upper_bound)
        self.update_guess_label()

    def go_correct(self):
        """Disables hint buttons and enables new game button."""
        self.too_small.disable()
        self.too_large.disable()
        self.correct.disable()
        self.new_game.enable()
        self.guess_label.set_text(f"You got it in {self.count} tries!")

    def start_new_game(self):
        """Resets game variables and re-enables hint buttons."""
        self.lower_bound = 1
        self.upper_bound = 100
        self.computer_guess = random.randint(self.lower_bound, self.upper_bound)
        self.count = 0

        self.too_small.enable()
        self.too_large.enable()
        self.correct.enable()
        self.new_game.disable()
        self.update_guess_label()

    def update_guess_label(self):
        """Updates the label to display the computer's new guess."""
        self.count += 1
        self.guess_label.set_text(f"Is the number {self.computer_guess} (Try {self.count})?")


if __name__ == "__main__":
    GuessingGame().mainloop()
