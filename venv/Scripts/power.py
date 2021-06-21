
x=int(input("Enter anum for X value :"))
n=int(input("Enter anum for N value :"))

def power(x,n):
     if n<=0:
        return n
     else:
        return x*power(x,n-1)

print(power(x,n))
