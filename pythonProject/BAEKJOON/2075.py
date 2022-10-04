import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)