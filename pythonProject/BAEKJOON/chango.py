import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

# 최대 높이
H = 0
for i in range(len(lst)):
    if lst[i][1] > H:
        H = lst[i][1]

# 최소 최대 너비 인덱스
W_min, W_max = 1001, 0
for j in range(len(lst)):
    if lst[j][0] < W_min:
        W_min = lst[j][0]
    if lst[j][0] > W_max:
        W_max = lst[j][0]

# 총 배열 생성
arr = [[0] * (W_max+1) for _ in range(H+1)]

# 배열에 값 넣기
for w, h in lst:
    for k in range(h):
        arr[k][w] = 1

ans = 0                     # 총 넓이
for m in range(len(arr)):
    floor = 0                   # 한 층마다 넓이
    zero = 0                    # 0 개수

    for n in range(len(arr[0])):
        if arr[m][n] == 0:          # 0 개수 세기
            zero += 1
        else:
            if floor == 0:     # 처음 만난 1
                zero = 0        # 지금까지 셌던 0 초기화
                floor += 1      # 자기 자신 넓이

            elif floor > 0:     # 두 번째 이후의 1
                floor += (zero + 1)         # 지금까지 센 0과 자기 자신
                zero = 0

    ans += floor

print(ans)