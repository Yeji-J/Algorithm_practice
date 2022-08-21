import sys
sys.stdin = open("review_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(N):
        for j in range(i+1, N):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    print(f'#{test_case} {nums[0]-nums[-1]}')