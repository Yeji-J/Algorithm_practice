import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N = int(input())            # 색종이 수
paper = []
idx_i = []
idx_j = []

# 색종이 인덱스, 표시할 숫자 k도 함께 저장
for k in range(1, N+1):
    i, j, n1, n2 = map(int, input().split())
    ni, nj = i + n1, j + n2
    paper.append([[i, j], [ni, nj], k])
    idx_i += [i, ni]
    idx_j += [j, nj]

# board 생성
# i, j 인덱스 최댓값 찾아 + 1
board = [[0] * (max(idx_j)) for _ in range(max(idx_i)+1)]

# board에 색종이 놓기
for idx in paper:
    si, sj = map(int, idx[0])
    ei, ej = map(int, idx[1])
    for pi in range(si, ei):
        for pj in range(sj, ej):
            board[pi][pj] = idx[2]

# 해당하는 숫자 세서 출력
for H in range(1, N+1):
    cnts = 0
    for bi in range(max(idx_i)+1):
        for bj in range(max(idx_j)):
            if board[bi][bj] == H:
                cnts += 1
    print(cnts)


