import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

W, H = map(int, input().split())        # 가로, 세로
N = int(input())            # 자르는 횟수

lstW = [0, 1] * (W - 1) + [0]         # 가로 길이 리스트
lstH = [0, 1] * (H - 1) + [0]         # 세로 길이 리스트

for _ in range(N):
    D, idx = map(int, input().split())
    if D == 1:              # 세로로 자를 때 가로 길이 slice
        lstW[2 * idx - 1] = 2
    else:                   # 가로로 자를 때 세로 길이 slice
        lstH[2 * idx - 1] = 2

# 최대 길이 0 count
max_w = 1
w = 0
for i in range(W * 2 - 1):
    if lstW[i] == 0:    # 0을 만나면 + 1
        w += 1
    if lstW[i] == 2 or i == W * 2 - 2:      # 2(cut) or 마지막 인덱스일 때
        if w > max_w:                   #  max값 갱신
            max_w = w
        w = 0

max_h = 1
h = 0
for j in range(H * 2 - 1):
    if lstH[j] == 0:
        h += 1
    if lstH[j] == 2 or j == H * 2 - 2:
        if h > max_h:
            max_h = h
        h = 0


ans = max_w * max_h
print(ans)