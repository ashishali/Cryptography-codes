import sympy #package for selecting random prime number
import random #package that helps in selecting a random number
import gmpy2 #package that helps in validating whether the number is prime or not

p = sympy.randprime(1000,5000)
q = sympy.randprime(1000,5000)
print("\n\nPrime numbers chosen are:", p,",",q, "\n")

n = p*q
z = (p-1)*(q-1)
print("Value of n:",n,"\nValue of z:",z,"\n")

temp_e = []
for i in range(10000,z+1):
    if z%i == 0:
        temp_e.append(i)

temp1_e = []
for j in range(10000,n):
    if j not in temp_e:
        temp1_e.append(j)

maybe_e = random.choice(temp1_e)

final_e= gmpy2.next_prime(maybe_e)
print("Value of e: ",final_e)

listt=[]
for i in range(1,100000000):
    if(((final_e*i)%z)-1)==0:
       listt.append(i)

for i in listt:
    q=i
    print("Value of d: ",i)

print("\n\nPublic Key: ",(n,int(final_e)))
print("Private Key: ",(n,q))
