a=int(input("enter the starting number: "))
b=int(input("enter the ending number: "))

even=[]
odd=[]
for n in range(a,b):
    if n%2==0:
        even.append(n)
    else:
         odd.append(n)
print("Even numbers:",even)
print("Odd numbers:",odd)
