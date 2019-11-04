#Guess the word
import random

def choose():
    words = ['orange','cube','beautiful','string','dream','pass','physics','tree','man','dream']
    ch = random.choice(words)
    return ch

def jumbled(word):
    jumble = "".join(random.sample(word,len(word)))
    return jumble

def thank(p1name,p2name,p1s,p2s):
    print(p1name," your score is ",p1s)
    print(p2name," your score is ",p2s)
    print("Thanks for play the game")
    print("Have a nice day")

def play():
    print("____________________GUESS THE WORD GAME_____________________")
    p1name = input('Enter the name of Player 1: ')
    p2name = input('Enter the name of player 2: ')
    pp1 = 0
    pp2 = 0
    turn = 0

    while(1):
        picked_word = choose()
        qn = jumbled(picked_word)
        print(qn)

        if turn%2 == 0:
            print(p1name," Your turn")
            ans = input("Please! Enter the word you guess: ")
            if(ans == picked_word):
                pp1 = pp1+1
                print("Hurrey! You guessed the right word")
                print("Your point is:",pp1)
            else:
                print("Better luck next time")
            c = int(input("Enter 1 to continue and 0 to end the game: "))
            if c == 0:
                thank(p1name,p2name,pp1,pp2)
                break

        else:
            print(p2name,"Your turn")
            ans = input("Please! Enter the word you guess: ")
            if(ans == picked_word):
                pp2 = pp2+1
                print("Hurrey! You guessed the right word")
                print("Your point is:",pp2)
            else:
                print("Better luck next time")
            c = int(input("Enter 1 to continue or 0 to end the game: "))
            if c == 0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn = turn+1

play()
