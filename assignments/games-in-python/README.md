

# 📘 Assignment: Games in Python

## 🎯 Objective

Build a simple Hangman-style word guessing game in Python. This assignment helps you practice string manipulation, loops, conditionals, user input, and working with a predefined list of words.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Create the basic structure of a Hangman game. Your program should choose a word from a predefined list and prepare the values needed to track the player's progress.

#### Requirements
Completed program should:

- Store several possible words in a predefined list.
- Randomly choose one word for the player to guess.
- Display the hidden word using underscores such as `_ _ _ _`.
- Keep track of the number of incorrect guesses remaining.

### 🛠️ Build the Guessing Loop

#### Description
Implement the main game loop so the player can guess letters until they either solve the word or run out of attempts.

#### Requirements
Completed program should:

- Ask the player to enter one letter at a time.
- Reveal correctly guessed letters in the word display.
- Reduce the number of remaining attempts for incorrect guesses.
- Continue looping until the full word is guessed or no attempts remain.
- Display a win message if the player guesses the word.
- Display a lose message if the player runs out of attempts.

Example game flow:

```text
Word: _ _ _ _
Guess a letter: a
Word: _ a _ _
Attempts remaining: 5
```
