import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    x1, y1, r1 = lst[0], lst[1], lst[2]
    x2, y2, r2 = lst[3], lst[4], lst[5]

    D = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5       # 두 원의 중심 사이의 거리 (피타고라스 정의 이용)

    if D == 0:              # 원의 중심이 같을 때

        if r1 == r2:        # 반지름이 같으면
            print(-1)       # 무한대

        else:               # 반지름이 같지 않으면
            print(0)        # 겹치는 점 없음

    else:                   # 원의 중심이 다를 때
        if abs(r1-r2) < D < r1 + r2:                # 겹치는 점 두 개
            print(2)

        elif D == r1 + r2 or D == abs(r1 - r2):        # 외접 & 내접
            print(1)

        else:     # 겹치는 점 없음
            print(0)