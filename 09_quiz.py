'''You have to build a dictionary (Or any other container of your choice) which contains multiple
 True/false type quiz questions.
Every participant/user will attempt 5 rounds and in each round random quiz questions will be displayed
 to the user/participant.
If the participant answers the quiz question correct, then congratulate him and add the scores.
At the end display the details and score of the participant.'''
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