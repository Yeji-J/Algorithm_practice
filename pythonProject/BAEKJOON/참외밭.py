import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

cham = int(input())
cnt = [0] * 5           # 동서남북 카운트
area_len = []
for _ in range(6):
    F, L = map(int, input().split())        # F : 동서남북 L : 길이
    cnt[F] += 1     # 동서남북 개수 카운트
    area_len.append([F, L])

# 높이, 너비 인덱스 구하기
hw_idx = []             # 여기에 들어있는 인덱스 두 개가 높이, 너비
for i in range(5):
    if cnt[i] == 1:
        hw_idx.append(i)

# 큰 사각형 높이 너비
big = []
for j in range(6):
    for hw in hw_idx:
        if area_len[j][0] == hw:
            big.append(area_len[j][1])

# 들어간 부분의 길이 찾기
# 높이 너비 인덱스 양옆에 위치한 길이 제외
# 남은 애들이 들어간 부분의 길이
search = []
for idx in range(6):
    for hw in hw_idx:
        if area_len[idx][0] == hw:
            search.append(idx)

# 작은 사각형 높이 너비
small = []
for x in search:
    if x + 3 > 5:       # 인덱스가 5 (인풋의 개수)를 넘어간다면
        small.append(area_len[x-3][1])      # -3

    else:               # 아니라면
        small.append(area_len[x+3][1])      # + 3

H, W = map(int, big)
Hs, Ws = map(int, small)

# 밭에서 생산 가능한 참외 개수
print((H * W - Hs * Ws) * cham)