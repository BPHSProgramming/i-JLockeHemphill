import os
os.system("cls")

equ = float(input("What equation do you want? "))
if equ==2.11:
    print(
        float(input("What is Vo: "))+
        float(input("What is a: "))*
        float(input("What is t: "))
        )
elif equ==2.15:
    print(
        float(input("What is Vo: "))*
        float(input("What is t: "))+
        0.5*
        float(input("What is a: "))*
        float(input("What is t: "))**2
        )
