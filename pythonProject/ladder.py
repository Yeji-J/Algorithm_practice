import sys
sys.stdin = open("input.txt", "r")

test_case = int(input())
arr = [list(map(int, input().split())) for _ in range(100)]
j = 99
ans = 0
i = 99
for i in range(99, -1, -1):
    if j == 99:
        if arr[i][j-1]:
            while True:
                if arr[i][j]:
                    j -= 1
                else:
                    break
    elif j == 0:
        if arr[i][j+1]:
            while True:
                if arr[i][j]:
                    j += 1
                else:
                    break
    else:
        if arr[i][j-1]:
            while True:
                if arr[i][j]:
                    j -= 1
                else:
                    break
        if arr[i][j+1]:
            while True:
                if arr[i][j]:
                    j += 1
                else:
                    break
    print(i, j)

print(f'#{test_case} {j}')