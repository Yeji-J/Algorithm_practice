import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N = int(input())
lst = []

if N == 1:
    print()
else:
    # 해당 숫자 내 소수
    for i in range(2, N+1):
        if N % i == 0:              # 나누어 떨어질 때
            lst += [i]              # 일단 추가

            for j in lst:                   # 리스트에 있는 원소에 대해
                if i != j and i % j == 0:   # 나눠 떨어진다면
                    lst.pop()               # 빼버리고 break
                    break

    # 소인수분해 결과
    for k in lst:
        while N % k == 0:
            N /= k
            print(k)