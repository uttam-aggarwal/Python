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