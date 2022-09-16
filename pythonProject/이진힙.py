import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    lst = [0] * (N + 1)

    for i in range(1, N+1):
        lst[i] = nums[i-1]                                  # 나온 번호 노드 리스트에 추가
        if lst[i//2] > lst[i]:                              # 조상 노드가 더 크다면
            j = i
            while lst[j//2] > lst[j]:
                lst[j//2], lst[j] = lst[j], lst[j//2]        # 조상 < 자식 조건 만족할 때까지 위치 바꾸기
                # 노드 index 변경
                j = j//2

    ans = 0
    while N != 1:       # root 번호 도달까지
        N = N//2        # 조상 노드 값 누적
        ans += lst[N]
    print(lst)
    print(f'#{tc} {ans}')


