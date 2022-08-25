import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())        # N: 숫자  M: 처리
    lst = list(map(int, input().split()))


    for i in range(M):              # M만큼
        lst.append(lst.pop(0))      # 앞에서 뒤로 보내기

    print(f'#{test_case} {lst[0]}')