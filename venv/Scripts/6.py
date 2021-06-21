#It19976136
#Paper Number 	06
n = int(input("Enter value for n: "))
#implement the above recursive algorithm.
def sum(n):
    if n <=0:
        return n+100
    else:
        if n %3==0:
            return (n*(sum(n-2)))
        else:
            return (n*(sum(n-3)))
#termination of the process
while n!= -1:
    print(sum(n))
    #keboard inputs
    n= int(input("Enter value for n: "))
