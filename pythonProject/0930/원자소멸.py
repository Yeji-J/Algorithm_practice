import sys
sys.stdin = open("input.txt", "r")

D = {   # 상 하 좌 우
    0:(-1,0), 1:(1,0), 2:(0,-1), 3:(0,1)
}


T = int(input())
for tc in range(1, T+1):
    N = int(input())

