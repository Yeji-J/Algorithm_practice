import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

# N = 10
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N-2):
#             print(i, j, k)

def nCr(n, r, s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, r+1)
A = [1, 2, 3, 4,5]
n = len(A)
r = 3
comb = [0] * r
nCr(n, r, 0)