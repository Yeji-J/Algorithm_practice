import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    num = int(input())
    cnts = [0] * 5
    k = 0
    for i in [2, 3, 5, 7, 11]:
        while True:
            if num % i == 0:
                cnts[k] += 1
                num /= i
            else:
                k += 1
                break

    print(f'#{test_case}', *cnts)

