import random
#imports a random module to choose random words
import time
#imports a timer to measure the length of the game
from words import word_list
#imports a word list from an external file

def get_word():
    #selects a random word from word_list
    word = random.choice(word_list)
    return word.upper()


def play(word):
    #the gameplay starts with this function
    word_completion = "_" * len(word)
    #creates a line of underscores the length of the randomly selected word
    guessed = False
    #boolean that indicates if the word has been guessed
    guessed_letters = []
    #this implements a list to keep track of the guessed letters
    guessed_words = []
    #this implements a list to keep track of the previously guessed words
    tries = 6
    #this is the number of attempts the player is given
    print("Let's play Hangman!")
    #welcome message
    
    # Start the timer
    start_time = time.time()
    
    print(display_hangman(tries))
    #displays the current hangman state
    print(word_completion)
    #displays the word completion
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        #input from player here/ first letter or word guess
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
                #alerts player if guessed letter has already been guessed
            elif guess not in word:
                print(guess, "is not in the word.")
                #alerts player if the guessed letter is not in the word
                tries -= 1
                #tracks the number of tries used
                guessed_letters.append(guess)
                #adds guessed letter to list of guessed letters
            else:
                print("Good job,", guess, "is in the word!")
                #make known to player if their guess is a letter in the word
                guessed_letters.append(guess)
                #add their letter to the list of guessed_letters
                word_as_list = list(word_completion)
                #convert word completion to list
                indices = [i for i, letter in enumerate(word) if letter == guess]
                #finds indices of the guessed letter in the word
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                #converts the word list back to a string
                if "_" not in word_completion:
                    #sets guessed to true if there remain no more underscores
                    guessed = True
                    #states that guessed is true
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
                #makes known to the player if their guessed word was already guessed
            elif guess != word:
                print(guess, "is not the word.")
                #makes known to the player if their guessed word is not the right word
                tries -= 1
                #decreases the number of tries
                guessed_words.append(guess)
                #adds the guessed word to the list of guessed words
            else:
                guessed = True
                #if the player's guessed word is correct, guessed is true
                word_completion = word
        else:
            print("Not a valid guess.")
            #makes known to player that their guess is invalid
        print(display_hangman(tries))
        #displays the hangman
        print(word_completion)
        #displays the word completion thus far
        print("\n")
        #newline for better readability
    
    # End the timer and calculate time taken
    end_time = time.time()
    time_taken = end_time - start_time

    if guessed:
        print("Congrats, you guessed the word! You win!")
        #congratulates the player if their guess was correct
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
        #makes known to the player that they are out of tries, what the correct word was, and displays an encouraging message
    
    # Display time taken
    print(f"Time taken: {time_taken:.2f} seconds\n")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
#return the stage to the number of tries left

def main():
    #main function for restarting the game and playing again
    word = get_word()
    #selects a random word
    play(word)
    #plays the game with the random word
    while input("Play Again? (Y/N) ").upper() == "Y":
        #asks the player if they want to play again
        word = get_word()
        #gets a new random word
        play(word)
        #plays the game with the new word


if __name__ == "__main__":
    main()
    #the main funtion that starts the game again
