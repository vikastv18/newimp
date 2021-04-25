import random
words = ['hello', 'what', 'blue']

def randomword():
    word = random.choice(words)
    return word

def mainfun():
    turns = 0
    word = randomword()
    wordlist = list(word)
    print(wordlist)
    dash = "_" * len(word)
    print(dash)

    while turns<6:
        a = input("Enter the letter: ")
        guess_list = []
        if len(a)>1:
            print("Enter one letter at a time")
        elif a =="":
            print("Please enter the char")
        elif a in guess_list:
            print("letter already in the list")
            print(guess_list)
        else:
            guess_list.append(a)



