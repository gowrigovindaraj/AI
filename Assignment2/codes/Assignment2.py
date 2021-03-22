import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  
n=int(input(print("Enter N:")))
if n<=2:
  print("Question in constraint n>2")
  exit()
print("a={a1,a2,.....,an}")
print()
print("x={x1,x2,....,xn}")
print("where all elements are 0,1.")
print()
sum=0
#considering the sum of 
for i in range(1,n+1,2):
     sum+=ncr(n,i)
     
    
sum=sum/(2**n)
print("The probability is")
print(sum)
