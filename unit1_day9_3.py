'''Randy and Mandy are playing a game. Mandy must provide Randy with a four letter word. Randy should pronounce the word by doubling each letter.
Constraints:
length of the word = 4
Letters of the word are not case sensistive.
Sample test case:
cold (Only line of input contains the four letter word)
ccoolidd (Print the output as required)'''
a=input()
b=""
for i in a:
    b=b+i+i
print(b)

