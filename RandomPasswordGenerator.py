#this is the basic form of the random_password_generator


import string
import random

charachters=list(string.ascii_letters + string.digits + "!@$%&*^()")

def generate_password():
    password_lenght=int(input("How long would you like your password to be? "))

    random.shuffle(charachters)

    password=[]
    for i in range(password_lenght):
        password.append(random.choice(charachters))


    random.shuffle(password)

    password="".join(password)

    print(password)


option=input("do you like to generate password  (Yes/No):  ")

if option=="Yes":
    generate_password()
elif option=="No":
    print("program ended")
    quit()
else:
    print("invalid input,please input Yes or No")
    quit()

