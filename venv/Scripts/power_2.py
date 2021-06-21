import math

#user inputs
x=int(input("Enter a num for X value :"))
n=int(input("Enter a 4num for N value :"))


def power(base,exp):
    if(exp == 0):
        return 1
    else:
        return base*power(base,exp-1)
while (x!=-1 or n!=-1):
    print(power(x,n))
    x=int(input("Enter anum for X value :"))
    n=int(input("Enter anum for N value :"))
