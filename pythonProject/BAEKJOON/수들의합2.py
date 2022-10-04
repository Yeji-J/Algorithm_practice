import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N = int(input())
lst = []
for i in range(1, N+1):         # 1 ~ N까지 숫자
    lst.append(i)

i = 1
while i <= 15:
    for j in range(1, N-i+1):
        for k in range():            # 더할 숫자 개수
