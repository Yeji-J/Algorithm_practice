import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    print(f'#{test_case}')
    for i in range(1, N+1):
        s = 1                   # 항상 시작은 1
        for j in range(1, i+1):
            print(s, end=' ')   # 프린트 먼저 (마지막 차례에 s가 0이 돼도 출력안됨)
            s = s * (i - j) // j    #
        print() # 다음 줄에 출력

