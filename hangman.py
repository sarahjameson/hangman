import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

guessed = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()


    guessed += guess
    if guessed.count(guess) > 1:
      print(f"You've already guessed {guess}")


    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} is not a correct guess. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            break

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

  
    print(hangman_art.stages[lives])