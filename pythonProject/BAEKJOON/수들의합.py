import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N = int(input())
lst = []
bit = [0] * N
for i in range(1, N+1):         # 1 ~ N까지 숫자
    lst.append(i)

ans = []
for bit in range(2**N):         # 비트 경우의 수
    S = []
    for j in range(N):          # 비트 한 세트에 대해
        if (bit >> j) & 1:      # 값이 존재하고
            if not S:           # S가 비었다면 해당 값 추가
                S.append(lst[j])

            else:                           # S에 값이 있다면
                if S[-1] + 1 == lst[j]:     # 연속된 자연수일 때만 추가
                    S.append(lst[j])

    if sum(S) == N and S not in ans:             # 합이 N이라면 경우의 수 추가
        ans.append(S)

print(len(ans))