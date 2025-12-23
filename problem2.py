import sys
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt", "w")

#fibonacci sequence with values up to 4000000
fib = [1,2]
while(fib[-1]<4000000):
    fib.append(fib[-1]+fib[-2])

#calculating the sum of even terms in the fibonacci sequence
sum = 0
for f in fib:
    if not f&1:
        sum += f

print(sum)