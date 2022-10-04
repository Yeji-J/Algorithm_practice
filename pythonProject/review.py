import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

<<<<<<< HEAD:pythonProject/review.py



=======
def counting(si,sj):
    global cnts

    if not stk:
        print(cnts)
        return cnts

    else:
        for ki, kj in idx:
            hi, hj = si + ki, sj + kj
            if 0 <= hi < N and 0 <= hj < N and arr[si][sj] + 1 == arr[hi][hj]:
                stk.append([ni, nj])
                cnts += 1
            else:
                if stk:
                    si, sj = map(int, stk.pop())
                    counting(si, sj)

                else:
                    print(cnts)
                    return cnts

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    idx = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    maxCnts = 0
    maxNum = 0
    for i in range(N):
        for j in range(N):
            # 상하좌우 탐색
            stk = []
            for di, dj in idx:
                cnts = 1
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and arr[i][j] + 1 == arr[ni][nj]:
                    stk.append([i, j])      # 현재 위치 저장
                    cnts += 1
                    counting(ni, nj)
                else:
                    break

>>>>>>> d7f176263f59e12ff0945e93a117192ccbe47819:pythonProject/main.py
