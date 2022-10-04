import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N = int(input())            # 학생수
num = list(map(int, input().split()))   # 뽑은 번호

line = [1]          # 초깃값 : 1번은 항상 번호 0을 뽑음

for idx in range(1, N):   # 2번 부터
    line_idx = len(line) - num[idx]         # 넣을 자리 = 현재 줄 길이 - 뽑은 번호
    line.insert(line_idx, idx+1)

print(*line)