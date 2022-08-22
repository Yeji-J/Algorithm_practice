import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

def palin(arr1, arr2):
    for i in range(N, 1, -1):
        for lst in arr1:
            for j in range(N-i+1):
                if lst[j:j+i] == lst[j:j+i][:-1]:
                    return i
        for lst in arr2:
            for k in range(N-i+1):
                if lst[k:k+i] == lst[k:k+i][::-1]:
                    return i
    return i

T = 1
for test_case in range(1, T+1):
    _ = input()
    N = 100
    arr1 = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr1))
    arr3=list(map(list, zip(*arr1)))

    # ans = palin(arr1, arr2)
    #
    # print(ans)

    print(arr2)
    print(arr3)





    
























    # length = 1
    # # 가로
    # M = 3
    # N = 100
    # for i in arr:
    #     j = 0
    #     print(i)
    #     while j < N-M+1:
    #         lst = i[j:j+M]
    #         if lst == lst[::-1]:
    #             length = M
    #             M += 1
    #             break
    #         else:
    #             j += 1
    #
    # print(length)