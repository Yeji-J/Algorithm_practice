import sys
sys.stdin = open("input.txt", "r")

# kruskal
# 대표원소 찾기
def find_set(n):
    while R[n] != n:
        n = R[n]
    return n

# 대표원소 할당
def union(x, y):
    R[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())        # V 마지막 노드 번호 (노드수: V+1) E 간선 수

    lst = []
    for _ in range(E):
        lst.append(list(map(int, input().split())))

    lst.sort(key=lambda x:x[2])         # 가중치 오름차순 정렬
    print(lst)
    R = [i for i in range(V + 1)]  # 대표 원소 배열

    cnts = 0        # 선택한 간선 수
    total = 0       # 가중치 합

    for n1, n2, w in lst:
        if find_set(n1) != find_set(n2):          # 연결된 노드의 대표 원소가 다르면
            union(n1, n2)           # 대표원소 바꾸기
            cnts += 1               # 선택된 간선 + 1
            total += w              # 가중치 더하기

            if cnts == V:           # 노드 수와 일치하면 break
                break

    print(f'#{tc} {total}')




