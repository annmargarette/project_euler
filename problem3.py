import sys

sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")

n = 600851475143
factor = []

i = 2

while(i*i < n):
    if n%i==0:
        while n%i == 0:
            factor.append(i)
            n/=i
    i+=1

if n>1:
    factor.append(n)

print(int(max(factor)))
    