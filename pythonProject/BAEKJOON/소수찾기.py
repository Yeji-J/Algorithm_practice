import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N = int(input())
lst = list(map(int, input().split()))

cnts = 0
for num in lst:
    tmp = []
    if num != 1:                    # 1이 아닐 때만
        for j in range(2, num + 1):
            if num % j == 0:  # 나누어 떨어질 때
                tmp += [num]  # 일단 추가

                for k in tmp:  # 리스트에 있는 원소에 대해
                    if j != k and j % k == 0:  # 나눠 떨어진다면
                        lst.pop()  # 빼버리고 break
                        break

    if len(tmp) == 1:
        cnts += 1

print(cnts)