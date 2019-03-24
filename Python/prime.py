a=int(input("enter the starting number: "))
b=int(input("enter the ending number: "))

prime=[]
non_prime=[]
for n in range(a,b):
    if n/1==0 & n/n==0:
        prime.append(n)
    else:
         non_prime.append(n)

print("Prime numbers:",prime)
print("Not prime numbers:",non_prime)
