# 코딩테스트 덩치 (7568번)

N = int(input("사람의 수를 입력하세요 : "))
ListOfN = []
for i in range(N):
    X,Y = (input("몸무게와 키를 입력하세요. : ").split())
    ListOfN.append([X,Y])

Rank = []
for j in range(0, len(ListOfN)):
    a = 0
    for k in range(0, len(ListOfN)+1):
        try:
            if (ListOfN[j][0] > ListOfN[k+1][0]) and (ListOfN[j][1] > ListOfN[k+1][1]):
                a = a + 1
        except:
            print("ERROR")
    Rank.append(a)
print(Rank)