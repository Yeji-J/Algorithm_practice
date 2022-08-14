import sys
sys.stdin = open("../input.txt", "r")

for test_case in range(1, 11):
    dump = int(input())
    lst = list(map(int, input().split()))
    k = 0
    while k < dump: # dump 횟수만큼
        min_i = 0 # 최솟값 인덱스
        max_i = 0 # 최댓값 인덱스
        for i in range(100):
            if lst[i] < lst[min_i]:
                min_i = i
            if lst[i] > lst[max_i]:
                max_i = i

        # 차이가 1 초과일 때 min, max 인덱스 값에 +1, -1씩
        if lst[max_i] - lst[min_i] > 1:
            lst[min_i] += 1
            lst[max_i] -= 1
            k += 1
        # 아니면 종료
        else:
            break
    # 이건......하....
    for i in range(1, 100):
        if lst[i] < lst[min_i]:
            min_i = i
        if lst[i] > lst[max_i]:
            max_i = i
    # 결과값이 2씩 차이가 나서 마지막에 max_i, min_i 찾는 걸 한 번 더 돌렸는데..
    # 코드가 매우매우매우 더러워졌어요
    # 이유 아시는 분.. 커피 사드릴게요...

    print(f'#{test_case} {lst[max_i] - lst[min_i]}')