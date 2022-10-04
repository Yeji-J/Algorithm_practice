import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

import heapq
import sys

H = []      # heap list
N = int(sys.stdin.readline())
for _ in range(N):
    # input 대신 sys.stdin.readline()으로 받기 - 시간초과때문
    n = int(sys.stdin.readline())

    if n != 0:      # 자연수일 때
        heapq.heappush(H, (-n, n))      # (-n, n) 내림차순 정렬

    else:           # 0일 때
        if H:       # heap list not empty
            print(heapq.heappop(H)[1])      # 최댓값 꺼내기

        else:       # heap empty
            print(0)        # 0 출력