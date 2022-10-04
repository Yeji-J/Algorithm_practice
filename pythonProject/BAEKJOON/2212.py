import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

# 센서 위치 오름차순 정렬
lst.sort()

# 센서 간 거리 차
distance = []
for i in range(len(lst)-1):
    distance.append(lst[i+1] - lst[i])
distance.sort(reverse=True)

if K >= N:      # 수신국 개수가 센서의 개수보다 크거나 같을 때
    print(0)
else:
    # 가장 큰 거리를 제외 -> 남은 곳에 수신국 세우기 : K-1 ~ 끝
    print(sum(distance[K-1:]))