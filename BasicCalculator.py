#this is a basic python calculator project for beginners
#enjoy




def add(a, b):
    answer= a + b
    print(str(a) + "+" + str(b)+ "=" + str(answer) + "\n")

def sub(a, b):
    answer= a - b 
    print(str(a)+ "-" + str(b)+ "=" + str(answer)+ "\n")

def div(a, b):
    answer=a / b
    print(str(a)+ "/" + str(b) + "=" + str(answer)+ "\n")


def mul(a, b):
    answer=a * b
    print( str(a)+ "*" +str(b)+ "=" + str(answer)+ "\n")



while True:

 print("A. add")
 print("S.sub")
 print("D.divide")
 print("M.multiplie")

 choice=input("please choose a function: ")
 if choice == "A" or choice=="a":
    print("addition")
    a=int(input("enter your number: "))
    b=int(input("enter your number: "))
    add(a,b)

 elif choice== "s" or choice=="S":
    print("subtraction")
    a=int(input("input your first number: "))
    b=int(input("enter your second number: "))
    sub(a,b)

 elif choice=="d" or choice=="D":
    print("Deviding")
    a=int(input("please enter your number: "))
    b=int(input("please add your second number: "))
    div(a,b)


 elif choice=="m" or choice== "M":
    print("multiplying")
    a=int(input("please give me a number: "))
    b=int(input("please give another number to multiple: "))
    mul(a,b)

 elif choice =="e" or choice=="E":
    print("the end")
    quit()









