# 윤년

INPUT_YEAR = int(input())
if INPUT_YEAR % 4 == 0 and INPUT_YEAR % 100 != 0:
    print(1)
elif INPUT_YEAR % 400 == 0:
    print(1)
else:
    print(0)