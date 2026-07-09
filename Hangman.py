import random
words = ["apple", "banana", "orange", "grapes", "watermelon"]
word = random.choice(words)
print("Guess the word! You only have 6 lives!")
display = []
guessed = []
lives = 6
for letter in word:
    display.append("_")
while lives > 0 and "_" in display:
    print(" ".join(display))
    guess = input("Guess a letter:").lower()
    if len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed:
        print("You've already guessed this letter")
        continue
    guessed.append(guess)


    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
                print("Correct!")



    if guess not in word:
        lives -= 1
        print("Nope!")
        print("You only have {} lives!".format(lives))

    if lives == 0:
        print("You lose!")
        print("The word was", word)
        break

    if "_" not in display:
        print("You win!")
        break