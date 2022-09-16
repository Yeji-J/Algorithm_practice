import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]

    # 초기 세팅
    arr[N//2][N//2] = arr[N//2+1][N//2+1] = 2
    arr[N//2+1][N//2] = arr[N//2][N//2+1] = 1

    # 해당 좌표에 돌 넣기
    for _ in range(M):
        si, sj, d = map(int, input().split())
        # 입력 받은 돌 넣기
        arr[si][sj] = d
        for di, dj in ((-1, 0), (-1, -1), (-1, 1), (0, -1), (1, 0), (0, 1), (1, 1), (1, -1)):

            s = []          # 뒤집을 후보 배열
            for mul in range(1, N):         # mul: 배열 끝까지 확장
                ni, nj = si + di * mul, sj + dj * mul

                # 범위 내에 있을 때
                if 1 <= ni <= N and 1 <= nj <= N:
                    # 돌이 없으면 끝
                    if arr[ni][nj] == 0:
                        break
                    # 돌과 색이 같을 때
                    elif arr[ni][nj] == arr[si][sj]:
                        # 해당 색과 같은 돌로 바꾸고 break
                        while s:
                            ti, tj = s.pop()
                            arr[ti][tj] = d
                        break
                        # 다른 돌일 때 뒤집을 후보 배열에 추가
                    else:
                        s.append((ni, nj))

                # 범위 밖이면 끝
                else:
                    break

    # 흑돌 백돌 counting
    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)

    print(f'#{tc} {bcnt} {wcnt}')
