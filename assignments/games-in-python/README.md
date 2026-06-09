
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. Students will practice control flow, string manipulation, and basic program structure.

## 📝 Tasks

### 🛠️ Implement the Hangman Game

#### Description
Create a playable Hangman game in Python that selects a secret word and lets the player guess letters until they either reveal the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept single-letter guesses from the player and update the displayed progress (e.g., _ _ a _ _ )
- Prevent or handle repeated guesses gracefully
- Track and display the number of incorrect guesses remaining
- End when the word is fully guessed or attempts are exhausted
- Display a win or lose message and reveal the secret word when the game ends

Example gameplay (simplified):

```
Secret word: panda
Progress: _ _ _ _ _
Guess: a
Progress: _ a _ _ a
Incorrect guesses left: 5
```

### 🛠️ Enhancements (Optional)

#### Description
Add one or more optional features to improve the game experience.

#### Requirements (choose any)

- Load word list from an external file (e.g., `words.txt`)
- Add difficulty levels that adjust word selection or allowed attempts
- Draw an ASCII-art hangman that progresses with each incorrect guess
- Implement a replay option and basic scoring
- Validate and sanitize user input

---

**Skills practiced:** String manipulation, loops, conditionals, random selection

**Starter file:** `starter-code.py` (provided in this folder)

Follow the project assignment guidelines in the repository when editing this file.
