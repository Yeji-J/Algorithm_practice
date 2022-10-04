import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

A, B, C, M = map(int, input().split())
# 시간 당 A : 피로도 B : 일 C : -피로도
# M : 최대 피로도


if A > M:                   # 애초에 일을 할 수 없을 때
    W = 0
else:
    P = W = 0
    for _ in range(24):         # 24시간 - 일 한 시각 - 1
        if P+A <= M:              # 이어서 일을 할 때 : 피로도가 한계 피로도보다 작거나 같다면
            P += A                  # 다시 일하고 피로 쌓이기
            W += B
        else:                   # 이어서 일을 할 때 한계 피로도를 넘어버린다면
            P -= C                  # 쉬어주기
            if P < 0:
                P = 0

print(W)