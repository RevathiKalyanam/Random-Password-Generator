#importing libraries
import string
import random

#To get password Length
length=int(input("Enter required length for password"))
print("Choose the following password sets for password :\n1.Letters\n2.Digits\n3.Special characters\n4.EXIT")
characterList=""

#To get character set for password
while (True):
    choice=int(input("Pick a number"))
    if(choice==1):
        #Adding letters
        characterList+=string.ascii_letters
    elif(choice==2):
        #Adding digits
        characterList+=string.digits
    elif(choice==3):
        #Adding special characters
        characterList+=string.punctuation
    elif(choice==4):
        break
    else:
        print("Pick a valid Number!")
password=[]
for i in range(length):
    #Picking a random character from our character list
    randomchar= random.choice(characterList)

    #Appending a random character to password
    password.append(randomchar)

#Printing password as a string
print("The random password is "+ "".join(password))