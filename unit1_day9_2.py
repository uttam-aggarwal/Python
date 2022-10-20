'''Brat and Pat are engaged in a covert operation. They should communicate in a way that is impossible for anyone to decode. Therefore, they decided to limit their communication to words of five letters where every pair of letters contains a ("#") them. Please assist Brat and Pat with encoding certain words.
Constraints:
length of the string = 5
string consists of upper case as well as lower case characters.
Sample test case:
crime (only line of input contains five-letter word)
c#r#i#m#e (print the encoded word with each letter separated by '#')'''
a=input()
b=""
for i in range(0,5):
    if i<4:
        print(a[i],end="#")
    else:
        print(a[i])