import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def bfs(s):
    # 초기화 작업
    vstd = [0] * 101
    q = []
    ans = s

    # 시작
    q.append(s)
    vstd[s] = 1

    while q:
        c = q.pop(0)            # 데이터 꺼내기 from q

        # 더 늦게 방문 or 같은 거리지만 더 큰 번호
        if vstd[ans] < vstd[c] or vstd[ans] == vstd[c] and ans < c:
            ans = c
        for e in arr[c]:        # 인접 리스트에서 꺼내기
            if not vstd[e]:
                q.append(e)
                # 시작점으로부터 거리 넣기
                vstd[e] = vstd[c] + 1

    return ans


T = 10
for tc in range(1, T+1):
    # input 받기
    N, R = map(int, input().split())
    lst = list(map(int, input().split()))
    
    # 연결관계 인접리스트에 저장
    arr = [[] for _ in range(101)]      #  최대 100개

    for i in range(0, len(lst), 2):
        arr[lst[i]].append(lst[i+1])

    ans = bfs(R)
    print(f'#{tc} {ans}')






