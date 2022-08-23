import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def rsp(s, e):
    # 종료 조건
    if s == e:
        return s

    # 하부호출, 최소단위작업 : 2등분 > 각 그룹 승자 > 최종 승자
    else:
        a = rsp(s, (s+e)//2)
        b = rsp((s+e)//2+1, e)

        if lst[a]%3 + 1 == lst[b]:     # b win
            return b
        return a        # 비기거나 이겨도 a win

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    ans = rsp(1, N)     # 1 ~ N 최종 승리자 index return

    print(f'#{test_case} {ans}')