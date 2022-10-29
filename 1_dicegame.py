'''Design a project where as an input student will give a static number (between 1 to 6) and then roll
the dice which randomly generate some value between 1 to 6. The winning situation arrives when the given
static/fixed number exactly same to the number came after rolling the dice.
User can play the game as many numbers of times he wants until user wants to exit, and whenever winning situation 
occur some scores must be given to the user, and these scores goes on adding if user play this game multiple number
of times.'''
import random
score=0
while True:
    number=int(input("enter the number: "))
    dice=random.randint(1,6)
    if number==dice:
        score+=1
        print("WIN score+1: ")
        print("current score =",score)
    else:
        print("Lost")
        print("current score =",score)
    repeat=input("once more?: N/Y: ")
    if repeat=="N":
        break
print(score,"is your final score")