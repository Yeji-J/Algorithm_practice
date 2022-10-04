import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

def check():

    # 가로 검사
    for lst in arr:
        for i in range(N-4):
            if lst[i:i+5] == ['o'] * 5:
                return "YES"

    # 세로 검사
    for lst2 in (list(map(list, zip(*arr)))):
        for j in range(N-4):
            if lst2[j:j+5] == ['o'] * 5:
                return "YES"

    # 대각선
    for i in range(N):
        for j in range(N):
            x1 = ''
            for di, dj in [[0,0], [1,1], [2,2], [3,3], [4,4]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    x1 += arr[ni][nj]
                else:
                    break

            if x1 == 'o' * 5:
                return "YES"

            x2 = ''
            for mi, mj in [[0,0], [-1,1], [-2,2], [-3,3], [-4,4]]:
                ki, kj = i + mi, j + mj
                if 0 <= ki < N and 0 <= kj < N:
                    x2 += arr[ki][kj]
                else:
                    break
            if x2 == 'o' * 5:
                return "YES"

    return "NO"


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(str(input())) for _ in range(N)]
    ans = ''

    print(f'#{test_case} {check()}')

