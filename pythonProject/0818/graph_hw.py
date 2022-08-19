import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

def dfs(S, E):
    stk = []
    vstd = [0] * 100    # 방문 기록
    vstd[S] = 1         # 시작

    while True:
        for i in range(100):
            if vstd[i] == 0 and arr[S][i] == 1:     # 초행길 & 연결된 길
                if i == E:
                    return 1
                else:
                    stk.append(S)       # 왔던 길 기록
                    S = i
                    vstd[i] = 1
                    break               # 0부터 다시 탐색 시작

        else:                           # 막다른 길
            if stk:
                S = stk.pop()           # 돌아가서 출발점 변경
            else:
                return 0

T = 3
for test_case in range(1, T+1):
    _ = input()

    arr = [[0]*100 for _ in range(100)]
    points = list(map(int, input().split()))


    for i in range(0, len(points)-1, 2):    # 인덱스 기록
        arr[points[i]][points[i+1]] = 1

    S = 0       # 출발지
    E = 99      # 목적지

    print(f'#{test_case} {dfs(S, E)}')
