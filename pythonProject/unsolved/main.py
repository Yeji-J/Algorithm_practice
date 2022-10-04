import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')
for test_case in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt1 = cnt2 = max = 1
    for i in range(1, N):
        if lst[i] < lst[i-1]:
            cnt1 += 1
            if cnt2 > N-i:
                break
            else:
                cnt2 = 1
        elif lst[i] > lst[i-1]:
            cnt2 += 1
            if cnt1 > N-i:
                break
            else:
                cnt1 = 1
        else:
            cnt1 += 1
            cnt2 += 1
        if max < cnt1:
            max = cnt1
        if max < cnt2:
            max = cnt2
    print(max)