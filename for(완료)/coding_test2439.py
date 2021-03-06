# 별 찍기 - 2

N = int(input())

for i in range(0, N):
    for j in range(0, N-i-1):
        print(" ", end = "")
    for k in range(0, i+1):
        print("*", end="")
    print("")