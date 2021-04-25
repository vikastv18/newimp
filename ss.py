import random

words = ['hello', 'what', 'buddy']
word = random.choice(words)
allowerd_errors = 7
guessess =[]
done = False

while not done:
    for letter in word:
        if letter in guessess:
            print(letter)
        else:
            print("_")

    guess = input("enter the char: ")
    guessess.append(guess)
    if guess not in word:
        allowerd_errors -=1
        if allowerd_errors ==0:
            break
    done =True

    for letter in word:
        if letter not in guessess:
            done=False

if done:
    print(word)
else:
    print("Not")