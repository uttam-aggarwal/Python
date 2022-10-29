'''You need to write a python script that generates an acronym word from a given sentence.
•	Take multiple strings as input in the form of list.
•	Add the first letter of each string to output.
•	Iterate over the complete string and add every next letter to space to output.
•	Change the output to uppercase (required acronym).
•	You have to generate acronyms for all given strings.'''
while True:
    a=input("enter sentence: ")
    print(a[0].upper(),end='')
    for i in range(0,len(a)):
        if a[i]==' ':
            print(a[i+1].upper(),end='')
    repeat=input("\nwant to enter another one? N/Y: ")
    if repeat=="N":
        break