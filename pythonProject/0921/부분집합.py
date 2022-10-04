import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def dfs(n, sm, cnt):        # sm 합 cnt 함께 넘겨주기
    global ans

    # 가지치기는 가장 위쪽에서
    # if로 계속 비교해야 하기 때문에 무조건 좋은건 아님
    if sm > K:
        return

    if n == N:                      # 종료조건
        if sm == K and cnt == CNT:      # 합, cnt 조건 부합
            ans += 1
        return
    else:
        dfs(n+1, sm + lst[n], cnt+1)        # 포함했을 때
        dfs(n+1, sm, cnt)                   # 포함하지 않았을 때

# def f(i, k):
#     if i == k:
#         for j in range(k):
#             if bit[j]:
#                 print(arr[j])
#         print()
#     else:
#         bit[i] = 0
#         f(i+1, k)
#         bit[i] = 1
#         f(i+1, k)
#
T = int(input())
for tc in range(1, T+1):
    CNT, K = map(int, input().split())
    N = 12

    lst = [i for i in range(1, 13)]
    ans = 0

    dfs(0, 0, 0)
#     arr = [1, 3, 4]
#     n = len(arr)
#
#     bit = [0] * n
#     f(0, n)
    print(f'#{tc} {ans}')