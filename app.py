import random

from phrase import Phrase
import sys

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase('My dog ate my homework'),
            Phrase('I love sushi'),
            Phrase('Coding is hard'),
            Phrase('Carell Baskin killed her husband'),
            Phrase('No pain no gain')
            ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]


    def start(self):
        self.welcome()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            lives = 5 - self.missed
            print("\nYou missed ", self.missed, " letters. You have ", lives, " lives remaining.")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            print(self.active_phrase.display(self.guesses))
            self.active_phrase.check_letter(user_guess)
            if not self.active_phrase.check_letter(user_guess):
                self.missed += 1
        self.game_over()

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print("\n####################################")
        print("Welcome to the phrase guessing game!")
        print("####################################\n")
    
    def get_guess(self):
        while True:
            try:
                print(self.active_phrase.display(self.guesses))
                guess = input('\nGuess a letter: ')
                # .isalpha returns True if all input characters are part of the alphabet
                if not guess.isalpha():
                    raise ValueError("\nMake sure you only input letters")
                elif len(guess) > 1:
                    raise ValueError("\nPlease enter only one letter!")
                elif guess in self.guesses:
                    raise ValueError("\nYou already tried this letter!")            
            except ValueError as err:
                print(err)
                print("Sorry, this ain't it, chief! Try again!")              
            else: 
                return guess

    def game_over(self):
        if self.missed == 5:
            print("\nYou've had ", self.missed, " incorrect guesses.")
            print("\nThe correct phrase was: {}".format(self.active_phrase.phrase.capitalize()))
            print("\nCome back to play again!")
        else:
            print("\n{}!".format(self.active_phrase.phrase.capitalize()))
            print("\nYeah, you won! You guesses the phrase correclty and beat me!")
            sys.exit()
            
if __name__ == "__main__":

    game = Game()
    game.start()    
            
