import sys
sys.stdin = open("../input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input()))
    ans = 0
    # 어차피 0은 영향 X, j+2까지 범위에서 index out of range 방지
    # 0 ~ 9 까지 정수, 양옆 [0] 포함
    cnts = [0] * 12
    # cnts 배열 생성
    for i in range(len(arr)):
        cnts[arr[i]] += 1
    # run or triplet 검사
    # ans == 2면 break
    j = 0
    while j < 10:
        if cnts[j] >= 3:
            ans += 1
            cnts[j] -= 3
        elif cnts[j] >= 1 and cnts[j+1] >= 1 and cnts[j+2] >= 1:
            ans += 1
            cnts[j] -= 1
            cnts[j+1] -= 1
            cnts[j+2] -= 1
        else:
            j += 1

    print(bool(ans//2)) # 몫 1이면 True, 0이면 False


