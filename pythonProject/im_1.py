import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def roll(a):
    b = list(map(list, (zip(*a))))      # zip 해서
    for i in range(N):
        b[i] = b[i][::-1]               # 반대로 집어 넣기
    return b

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr1 = [list(input().split()) for _ in range(N)]

    # 90도 회전
    arr2 = roll(arr1)

    # 180도 회전
    arr3 = roll(arr2)

    # 270도 회전
    arr4 = roll(arr3)

    print(f'#{test_case}')

    res = ""
    for i in range(N):
        res = "".join(arr2[i]) + " " + "".join(arr3[i]) + " " + "".join(arr4[i])
        print(res)

        res = ""

