import sys
sys.stdin = open("../input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    _ = input()
    eng1 = list(map(str, input().split()))
    nums = dict()
    for num in eng1:
        if num in nums:
            nums[num] += 1
        else:
            nums[num] = 1
    eng2 = [['ZRO'] * nums['ZRO'], ['ONE'] * nums['ONE'], ['TWO'] * nums['TWO'], ['THR'] * nums['THR'],
            ['FOR'] * nums['FOR'], ['FIV'] * nums['FIV'], ['SIX'] * nums['SIX'], ['SVN'] * nums['SVN'], ['EGT'] * nums['EGT'],
           ['NIN'] * nums['NIN']]
    ans = list()
    for i in range(len(eng2)):
        ans += eng2[i]
    print(f'#{test_case}')
    print(*ans)
