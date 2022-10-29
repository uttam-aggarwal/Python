'''Your task is create a converter which converts given roman numeral to an integer'''
a=input("enter the roman number: ")
integer=0
dict={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
for i in range(0,len(a)):
    if len(a)-1==i:
        integer+=dict[a[i]]
        break
    else:
        if dict[a[i]]>=dict[a[i+1]]:
            integer+=dict[a[i]]
        elif dict[a[i]]<dict[a[i+1]]:
            integer-=dict[a[i]]
    
print(integer)


