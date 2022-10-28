import random
s,e=int(input("starting range: ")),int(input("ending range: "))
score=0
while True:
    number=random.randint(s,e)
    for i in range(1,4):
        print("(TRY ",i,") guess the number: ",sep="",end="")
        u_input=int(input())
        if u_input>number:
            print("TRY AGAIN --- guessed higher")
        elif u_input<number:
            print("TRY AGAIN --- guessed smaller")
        else:
            print("congrats right guess")
            score+=1
            break
    print("The number was",number)
    print("current score is =",score)
    repeat=input("another round? N/Y: ")
    if repeat=="N":
        break
print("your final score is",score)