import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

M = int(input())
N = int(input())
lst = []

for i in range(M, N+1):             # 두 수의 범위 내 모든 수
    if i != 1:                      # 1이 아니라면
        lst += [i]                   # 리스트에 일단 추가

    for j in range(2, i):         # 2부터 해당 수 이전까지
        if i != 1 and i % j == 0:              # 나누어 떨어지면 해당 수 제거 및 break
            lst.pop()
            break

if lst:                 # lst not empty
    print(sum(lst))
    print(min(lst))
else:                   # lst empty
    print(-1)