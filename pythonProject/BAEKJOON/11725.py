import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def scan(idx):
    for n in tree[idx]:         # 해당 인덱스에 속하는 각 노드에 대해
        if not v[n]:            # 방문한 적 없는 노드면 (부모가 아직 없는 노드면)
            treeP[n] = idx      # 해당 자리에 인덱스(부모) 값 할당
            v[n] = 1            # 방문 표시
            scan(n)             # 해당 노드와 연결된 다음 노드 스캔

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    n1, n2 = map(int, sys.stdin.readline().split())
    # 연결된 노드 표시
    tree[n1].append(n2)
    tree[n2].append(n1)


treeP = [0] * (N+1)         # 부모 노드
v = [0] * (N+1)             # 방문 표시

v[1] = 1    # root 방문 표시
scan(1)     # 탐색 시작

# 출력
for i in range(2, N+1):
    print(treeP[i])