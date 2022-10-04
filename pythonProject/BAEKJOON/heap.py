import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

import heapq
N = int(input())
H = []

for _ in range(N):
    x = int(input())

    if not H and x == 0:        # 리스트가 비었는데 0일 때
        print(x)
    else:                       # 리스트에 값이 있을 때
        if x != 0:              # 자연수일 때
            heapq.heappush(H, (-x, x))    # 내림차순으로 추가
        else:                   # 0일 때
            print(H.pop(0)[1])