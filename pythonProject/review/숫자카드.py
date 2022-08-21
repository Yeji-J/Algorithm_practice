import sys
sys.stdin = open("review_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = input()
    cnts = [0] * 10     # 0 ~ 9
    for num in nums:
        cnts[int(num)] += 1

    ans = [0, 0]
    for i in range(10):
        if cnts[i] >= ans[1] and i > ans[0]:    # 카드 갯수 동일, 더 큰 숫자 저장
            ans[1] = cnts[i]
            ans[0] = i

    print(f'#{test_case}', *ans)