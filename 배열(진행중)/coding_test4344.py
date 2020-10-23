# 평균을 넘겠지

C = int(input())
score_list = []
for i in range(C):
    N = int(input())
    for j in range(N):
        score = map(int,input().split())
        score_list.append(score)
    average = sum(score_list,0)/len(score_list)
    for l in range(N):
        temp = 0
        if score_list[l] > average:
            temp += 1
    answer = temp / len(score_list) * 100
    print("%.3f"%answer)