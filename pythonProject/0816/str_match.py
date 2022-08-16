import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = int(input())
for test_case in range(1, T+1):
    N = input()
    M = input()
    ans = 0
    for i in range(len(M)-len(N)+1):
        word = ''
        for j in range(i, i+len(N)):
            word += M[j]
        if word == N:
            ans = 1
            break
    print(f'#{test_case} {ans}')