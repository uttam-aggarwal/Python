'''encryption-decryption password'''
password=input("enter your password(min 8 chars): ")
encrypted_password=""
for i in range(0,len(password)):
    if i%2==0:
        encrypted_password+=password[i]
    elif i==1:
        encrypted_password+='@'
        encrypted_password+=password[i]
    elif i==3:
        encrypted_password+='v'
        encrypted_password+=password[i]
    elif i==5:
        encrypted_password+='0'
        encrypted_password+=password[i]
    else:
        encrypted_password+=password[i]

print(encrypted_password)
#decryption
decrypted_password=''
for i in range(0,len(encrypted_password)):
    if i==1:
        continue
    elif i==4:
        continue
    elif i==7:
        continue
    else:
        decrypted_password+=encrypted_password[i]
print(decrypted_password)