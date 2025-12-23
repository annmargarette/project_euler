import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

mxpal = -1
for i in range(900,1000):
    for j in range(i, 1000):
        s = str(i*j)
        copy = s[::-1]
        if(s==copy):
            mxpal = max(int(s),mxpal)

print(mxpal)