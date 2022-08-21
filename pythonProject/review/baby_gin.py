import sys
sys.stdin = open("review_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    cnts = [0]*12        # [0] + 0 ~ 9 + [0]
    nums = input()
    for num in nums:
        cnts[int(num)] += 1
    ans = 0     # ans == 2면 baby gin
    i = 0
    while i < len(cnts):
        if cnts[i] >= 3:                                            # triplet
            ans += 1
            cnts[i] -= 3
        if cnts[i-1] == 1 and cnts[i] == 1 and cnts[i+1] == 1:      # run
            ans += 1
            cnts[i-1] -= 1
            cnts[i] -= 1
            cnts[i+1] -= 1

        if ans == 2:
            break

        i += 1

    print(f'#{test_case} {ans//2}')