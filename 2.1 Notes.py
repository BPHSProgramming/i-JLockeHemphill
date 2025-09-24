import os
os.system("cls")
# this is a comment

print("Hello World")
# this is completely outside of class fun time cause he talks FOREVER
runnum = 0
#quad formula for funsies
while runnum<=5:
    astr = input("A: ")
    a = int(astr)
    bstr = input("B: ")
    b = int(bstr)
    cstr = input("C: ")
    c = int(cstr)
    x1 = 0
    x2 = 0
    x1 = format((-b + (b**2 - 4*a*c)**0.5)/2*a, '.2')
    x2 = format((-b - (b**2 - 4*a*c)**0.5)/2*a, '.2')
    print("X1 = ",x1)
    print("X2 = ",x2)
    runnum+=1