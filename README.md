# Techdegree_Unit3_Project
Using Python, I created two Python classes with specific attributes and methods. I created a Game class for managing the game, and a Phrase class to help with storing attributes of a phrase with specific methods to help determine how to display the phrase in the game.
My code chooses a random phrase and use some logic I implemented to display each letter of the phrase as underscore character placeholders, _.
Each time the player guesses a letter, the program compares the letter the player has chosen with the random phrase. If the letter is in the phrase, the phrase object is updated so that it displays the chosen letters on the screen.
A player continues to select letters until they guess the phrase (and win), or make five incorrect guesses (and lose).
If the player completes the phrase before they run out of guesses, a winning screen appears. If the player guesses incorrectly five times, a losing screen appears.
