import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

a, b = map(int, input().split())

if a > b:
    B, S = a, b
else:
    B, S = b, a

# 최대공약수
cmnM = 0
for i in range(S, 0, -1):       # 더 작은 값 1씩 감소
    if S % i == 0 and B % i == 0:           # 나누어 떨어지면
        cmnM = i
        break
print(cmnM)

# 최소공배수
cmnS = cmnM * (a // cmnM) * (b // cmnM)
print(cmnS)