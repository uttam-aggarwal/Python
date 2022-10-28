import random
QA={'Q1':'ANS1','Q2':'ANS2','Q3':'ANS3','Q4':'ANS4','Q5':'ANS5'}
score=0
for i in range(0,5):
    Qs=random.choice(list(QA.keys()))
    print(Qs)
    ans=input("type the answer: ")
    ans=ans.upper()
    if QA.get(Qs)==ans:
        print("congratulation it's the right answer")
        score+=1
    else:
        print("wrong answer")
    del QA[Qs]
print("Total score =",score,"/ 5")