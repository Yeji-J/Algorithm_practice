import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = int(input())
for tc in range(1, T+1):
    # N: 셀 개수 M: 격리시간 K: 군집 수
    N, M, K = map(int, input().split())
    arr = [[0] * N for _ in range(N)]

    # 군집
    group = []
    for _ in range(K):
        # 좌표1, 좌표2, 미생물 수, 이동방향
        lst = list(map(int, input().split()))
        group.append(lst)
        arr[lst[0]][lst[1]] = lst[2]        # 미생물 배치

    # 상 1 하 2 좌 3 우 4
    # 이동
    pos = {
        1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)
    }

    for _ in range(M):          # M시간 동안
        # 방문표시
        V = [[0] * N for _ in range(N)]
        for one in group:       # 각 미생물들에 대해
            di, dj = one[0], one[1]                                         # 현재 위치

            # 이동 & 위치 업데이트
            arr[di][dj] = 0
            one[0], one[1] = di + pos[one[-1]][0], dj + pos[one[-1]][1]
            ci, cj = one[0], one[1]     # 업데이트 된 위치
            arr[ci][cj] = one[2]        # 해당 칸에 미생물 수 넣기
            V[ci][cj] += 1               # 방문 표시

            # 약품처리 구역에 있는 경우 미생물 //2 감소
            if ci == 0 or cj == 0 or ci == N - 1 or cj == N - 1:
                one[2] //= 2            # 미생물 수 업데이트
                arr[ci][cj] = one[2]    # 업데이트된 수 할당

                # 이동방향 변경
                if one[-1] == 1:
                    one[-1] = 2
                elif one[-1] == 2:
                    one[-1] = 1
                elif one[-1] == 3:
                    one[-1] = 4
                else:
                    one[-1] = 3

        # 1시간 동안 이동 + 약품구역에서 걸러짐 + 현재 군집 위치
        # 겹치는 위치 미생물 합치기 + 군집 제거
        mer_idx = []
        for m in range(N):
            for n in range(N):
                if V[m][n] > 1:             # 군집이 2이상인 곳
                    mer_idx.append([m,n])

        # 미생물수 최대인 군집으로 흡수
        for mi, mj in mer_idx:
            mer = []
            for G in range(len(group)):
                if group[G][0] == mi and group[G][1] == mj:
                    mer.append(group[G]+[G])                    # 인덱스와 함께 저장
            # 최댓값 인덱스, 값, 총합
            gIdx, gM, gSum = 0, 0, 0
            for x in mer:
                gSum += x[2]
                if x[2] > gM:
                    gM, gIdx = x[2], x[-1]

            group[gIdx][2], arr[x[0]][x[1]] = gSum, gSum

            for r in mer:
                if r[-1] != gIdx:
                    group[r[-1]][2] = 0

            # 미생물 수 0인 그룹 제거
            for _ in range(len(group)):
                G = group.pop(0)
                if G[2] != 0:
                    group.append(G)

    ans = 0
    for a in group:
        ans += a[2]

    print(f'#{tc} {ans}')





