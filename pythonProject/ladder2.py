import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = 10
for test_case in range(1, T+1):
    _ = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    end = []
    min_lst = [10000, 0]

    for e in range(100):
        if arr[9][e] == 1:
            end.append([99, e])

    for i, j in end:
        sm = 0
        while i > 0:                # 갈 수 있는 길에 한해서

            if j > 0 and arr[i][j-1] == 1:       # 좌측 이동 가능
                arr[i][j] = 0               # 이동지점 초기화
                j -= 1                      # 좌측으로 계속 이동
                sm += 1

            elif j < 99 and arr[i][j+1] == 1:     # 우측 이동 가능

                arr[i][j] = 0               # 이동 지점 초기화
                j += 1                      # 우측으로 계속 이동
                sm += 1

            else:                           # 아니면 계속 직진
                i -= 1
                sm += 1

        print(min_lst[0])
        if sm < min_lst[0]:
            min_lst[0] = sm
            min_lst[1] = j

    print(min_lst)

