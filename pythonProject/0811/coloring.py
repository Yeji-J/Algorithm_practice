import sys
sys.stdin = open("../input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    coloring = int(input())
    lst = []
    red = []
    blue = []
    cnts = 0
    # input 받아 이차원 배열로 저장
    for i in range(coloring):
        lst.append(list(map(int, input().split())))
        # color가 red면 모든 좌표 red 리스트에 저장
        if lst[i][-1] == 1:
            for s in range(lst[i][0], lst[i][2]+1):
                for e in range(lst[i][1], lst[i][3]+1):
                    red.append([s, e])
        # color가 blue면 모든 좌표 blue 리스트에 저장
        if lst[i][-1] == 2:
            for s in range(lst[i][0], lst[i][2] + 1):
                for e in range(lst[i][1], lst[i][3] + 1):
                    blue.append([s, e])
    # 범위가 더 큰 리스트에서 작은 리스트의 원소를 포함한다면
    # 개수 cnts + 1
    if len(blue) > len(red):
        for x in red:
            if x in blue:
                cnts += 1
    if len(red) > len(blue):
        for x in blue:
            if x in red:
                cnts += 1

    print(f'#{test_case} {cnts}')