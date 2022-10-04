import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def day(si, sj):                    # day 함수
    for sj2 in range(1, W-sj):      # 리스트 하나의 길이 까지만
        if res[si][sj+sj2] == -1:   # 구름이 없다면
            res[si][sj+sj2] = sj2   # 누적된 day 초기화

        else:                       # 구름을 만난다면 함수종료
            return res

H, W = map(int, input().split())
cloud = [list(str(input())) for _ in range(H)]

res = [[-1] * W for _ in range(H)]          # default -1

# 구름 표시
for i in range(H):
    for j in range(W):
        if cloud[i][j] == 'c':
            res[i][j] = 0

# 구름이 뜨는 시간 표시
for m in range(H):
    for n in range(W):
        if res[m][n] == 0:      # 구름을 만났을 때
            day(m, n)           # day 표시하는 함수 실행

#출력
for lst in res:
    print(*lst)
