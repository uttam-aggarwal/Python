'''You have to create a repository of your classmates name and mobile numbers. And whenever you want to search the 
mobile/contact number of some of your classmate, you can easily search it out from the repository you maintained.
Searching single contact is one of the functionalities, some other functionalities your app must cover are:
1.	Your app must be capable of displaying all the contacts with your classmate names present in the repository.
2.	Your app must be capable of extracting contact numbers of your multiple classmates when required.'''
repository={"A":"6787678767","B":"9876567898","C":"9876543212","D":"9876567453","E":"7657865456"}
print("enter 1 to search for the data of someone \nenter 2 to see the full repository")
a=input("ENTER THE NUMBER: ")
if a=="1":
    while True:
        name=input("ENTER THE NAME OF THE PERSON IN CAPITALS: ")
        if name in repository.keys():
            print("Mobile number of ",name,"is",repository[name])
            again=input("another one? Y/N: ")
            if again=="N":
                break
        else:
            print("data missing .... try again")
elif a=="2":
    for i in range(len(repository)):
        print("Mobile number of",list(repository)[i],"is",list(repository.values())[i])
else:
    print("INVALID INPUT")
        
