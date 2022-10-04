import sys
sys.stdin = open("../input.txt", "r")

T = 3 # 테스트 케이스 3개
for test_case in range(1, T+1):
    N = 100 # 크기 100 * 100
    _ = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    i, j = N-1, 0 # 출발점 초기화
    # 값이 2인 곳 ==> 출발지점
    for tj in range(N):
        if arr[i][tj] == 2:
            j = tj
            break

    # 갈 수 있는 길에 한해서 (i == 1)
    while i > 0:
        if j > 0 and arr[i][j-1] == 1:  # 왼쪽으로 이동 가능하다면
            arr[i][j] = 0     # 이동한 지점은 중복을 피하도록 0으로 값 초기화
            j -= 1              # 값이 0일 때까지 이동
        elif j < 99 and arr[i][j+1] == 1: # 오른쪽으로 이동 가능하다면
            arr[i][j] = 0
            j += 1
        else: # 직진만 가능시 직진 & 이동한 자리 0으로 초기화
            i -= 1

    print(f'#{test_case} {j}')
