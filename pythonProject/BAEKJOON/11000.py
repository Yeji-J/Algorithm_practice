import sys, heapq
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N = int(sys.stdin.readline())

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 수업 시간 정렬
lst.sort()

q = []
heapq.heappush(q, lst[0][1])        # 첫 번째 수업 종료시간 push

for i in range(1, N):               # 두 번째 수업부터 비교
    if lst[i][0] < q[0]:            # 다음 수업의 시작 시간 < 현재 수업 종료 시간 (시간 겹칠 때)
        heapq.heappush(q, lst[i][1])

    else:                           # 안 겹칠 때
        heapq.heappop(q)                # 현재 수업 pop
        heapq.heappush(q, lst[i][1])    # 다음 수업 push

print(len(q))








