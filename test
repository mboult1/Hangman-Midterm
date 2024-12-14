import random
import time
from words import word_list

# Function to select a random word
def get_word():
   word = random.choice(word_list)
   return word.upper()

# Hangman game logic
def play(word):
   word_completion = "_" * len(word)
   guessed = False
   guessed_letters = []
   guessed_words = []
   tries = 6
   print("Let's play Hangman!")
   
   # Start the timer
   start_time = time.time()
   
   print(display_hangman(tries))
   print(word_completion)
   print("\n")
   
   while not guessed and tries > 0:
       guess = input("Please guess a letter or word: ").upper()
       if len(guess) == 1 and guess.isalpha():
           if guess in guessed_letters:
               print("You already guessed the letter", guess)
           elif guess not in word:
               print(guess, "is not in the word.")
               tries -= 1
               guessed_letters.append(guess)
           else:
               print("Good job,", guess, "is in the word!")
               guessed_letters.append(guess)
               word_as_list = list(word_completion)
               indices = [i for i, letter in enumerate(word) if letter == guess]
               for index in indices:
                   word_as_list[index] = guess
               word_completion = "".join(word_as_list)
               if "_" not in word_completion:
                   guessed = True
       elif len(guess) == len(word) and guess.isalpha():
           if guess in guessed_words:
               print("You already guessed the word", guess)
           elif guess != word:
               print(guess, "is not the word.")
               tries -= 1
               guessed_words.append(guess)
           else:
               guessed = True
               word_completion = word
       else:
           print("Not a valid guess.")
       print(display_hangman(tries))
       print(word_completion)
       print("\n")
   
   # End the timer and calculate time taken
   end_time = time.time()
   time_taken = end_time - start_time

   # Check win or loss condition
   if guessed and tries > 0:
       print("Congrats, you guessed the word! You win!")
   else:
       print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
   
   # Display time taken
   print(f"Time taken: {time_taken:.2f} seconds\n")


# Hangman drawing function
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

# Test function for the game
def test_play():
   # Define test cases
   test_cases = [
       {
           "word": "PYTHON",
           "guesses": ['P', 'Y', 'Z', 'T', 'H', 'O', 'N', 'PYTHON'],
           "expected_outcome": "win",
       },
       {
           "word": "HANGMAN",
           "guesses": ['A', 'E', 'I', 'O', 'U', 'J', 'T'],
           "expected_outcome": "lose",
       },
       {
           "word": "DEBUG",
           "guesses": ['X', 'Y', 'Z', 'A', 'B', 'C', 'F'],
           "expected_outcome": "lose",
       },
   ]

   # Loop through each test case
   for i, case in enumerate(test_cases):
       print(f"Running Test Case {i + 1}")
       mock_guesses = iter(case["guesses"])

       def mock_input(prompt):
           return next(mock_guesses)

       # Patch the input function
       original_input = __builtins__.input
       __builtins__.input = mock_input

       try:
           play(case["word"])
       finally:
           __builtins__.input = original_input  # Restore original input function

       print(f"Test Case {i + 1} completed.\n")

# Run the tests
if __name__ == "__main__":
   test_play()
