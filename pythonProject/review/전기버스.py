import sys
sys.stdin = open("review_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    K, N, M =  map(int, input().split())
    stn = [0] + list(map(int, input().split())) + [N]   # 출발지 0과 도착지 N

    s = ans = 0
    for i in range(1, len(stn) ):
        if stn[i] - stn[i-1] > K:       # 처음부터 도착 불가능일 때
            ans = 0
            break
        elif stn[i] - stn[s] > K:       # 갈 수 있는 범위를 넘었을 때
            s = i - 1                   # 충전지를 출발지로
            ans += 1                    # 충전 + 1

    print(f'#{test_case} {ans}')







