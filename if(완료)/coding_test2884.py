# 2884 45분전 알람맞추기

H,M = map(int,input().split())

TIME_Temp = (H*60) + M
TIME_Temp = TIME_Temp - 45

if TIME_Temp < 0:
    TIME_Temp = 1440 + TIME_Temp
H = int(TIME_Temp / 60)
M = TIME_Temp % 60

print(H,M)