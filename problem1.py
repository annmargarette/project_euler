import sys
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt", "w")

n = 1000

sum = 0
for i in range(1,n):
    if i%3 == 0 or i%5 == 0:
        sum += i
print(sum)