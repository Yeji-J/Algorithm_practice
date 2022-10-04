import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

#  반배정 함수
def ABC(T1, T2):
    cnts = [0] * 3      # A, B, C로 분반

    for test in scores:         # T1, T2 점수 기준에 따라 분반
        if test < T1:
            cnts[0] += 1
        elif T1 <= test < T2:
            cnts[1] += 1
        else:
            cnts[2] += 1

    for ppl in cnts:
        # 분반 인원이 최소 배정인원보다 적거나, 최대 배정인원보다 많을 때
        if ppl < min_N or max_N < ppl:
            return                    # 함수 종료

    # 분반 인원이 범위 내에 있을 때
    sm_min.append(max(cnts) - min(cnts))
    return


T = int(input())
for tc in range(1, T+1):
    N, min_N, max_N = map(int, input().split())     # N : 사원 수
    scores = list(map(int, input().split()))
    scores.sort()               # 점수 정렬

    # 분반 기준 점수
    std = []
    for score in scores:
        if score not in std:
            std.append(score)

    # T1, T2 가능한 모든 경우 수
    sm_min = []                 # 인원배정 조건을 만족한 경우 넣을 최대최소 차
    for t1 in range(len(std)):
        for t2 in range(t1+1, len(std)):
            T1, T2 = std[t1], std[t2]
            ABC(T1, T2)                 # 점수 기준으로 반 배정

    if sm_min:              # 최대최소 차에 저장된 값이 있을 때
        ans = min(sm_min)
    else:                   # 저장된 값이 없을 때 == 인원 배정 기준을 만족하는 경우가 없을 때
        ans = -1

    print(f'#{tc} {ans}')