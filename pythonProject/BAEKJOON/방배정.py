import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N, K = map(int, input().split())        # N : 참가 인원 K : 배정 최대

cntS = [[0, 0] for _ in range(7)] # 학년별 성별 카운트

for _ in range(N):
    S, G = map(int, input().split())
    cntS[G][S] += 1

# 방배정
room = 0
for i in range(1, 7):               # 학년, 성별 수만큼
    for j in range(2):
        std = cntS[i][j]            # 해당 학년, 해당 성별 학생수

        if std != 0:                # 학생이 있고
            if std <= K:            # 최대 배정 수보다 같거나 작다면
                room += 1
            else:                   # 최대 배정 수보다 크다면

                if std % K:                # 나머지가 있을 때
                    room += (std // K + 1)      # 방하나 더 추가
                else:
                    room += std // K

print(room)