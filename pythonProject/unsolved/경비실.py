import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

W, H = map(int, input().split())        # 블록 가로 세로
N = int(input())
distance = []

# 절대 경로 구하기
for _ in range(N+1):        # 동근이 좌표까지
    F, D = map(int, input().split())
    if F == 2:
        idx = D
    elif F == 4:
        idx = W + H - D
    elif F == 1:
        idx = W + H + W - D
    elif F == 3:
        idx = W + H + W + D
    distance.append(idx)

sm = 0
dg = distance[-1]       # 동근이 좌표
for k in range(N):
    if abs(distance[k] - dg) < abs(2 * (H + W) - (distance[k] - dg)):
        sm += abs(distance[k] - dg)
    else:
        sm += abs(2 * (H + W) - (distance[k] - dg))


print(sm)