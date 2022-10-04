import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

# 시작시간과 끝시간이 같은 경우 때문에
# 끝시간 오름차순 -> 시작시간 오름차순으로 두 번 정렬
lst.sort(key=lambda x:(x[1], x[0]))

room = []
room.append(lst[0])
for i in range(1, len(lst)):
    if room[-1][1] <= lst[i][0]:
        room.append(lst[i])


print(len(room))