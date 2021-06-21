#this is an Array =[] or list
A = []

for i in range(10):
    # this is key board inputs
    n = int(input(f"enter a number {i+1}:"))
    #The append() method appends(එකතු කරයි) an element to the end of the list.
    A.append(n)
print(max(A))
print(A)
max = A[0]
for j in range(len(A)):
    if max < A[j]:
        max=A[j]

print(max)
print(A)

