import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def hPartition(l, r):
    pivot = lst[l]          # 피봇 값
    i, j = l, r             # 인덱스

    while i <= j:                           # 두 인덱스가 만날 때까지

        while i <= j and lst[i] <= pivot:   # 왼쪽 원소 피봇보다 작으면 index 증가
            i += 1
        while i <= j and lst[j] >= pivot:   # 오른쪽 원소 피봇보다 크면 index 감소
            j -= 1

        if i < j:                           # i와 j가 만나지 않은 경우
            lst[i], lst[j] = lst[j], lst[i]

    # pivot 자기 자리 찾아가기 : pivot <-> j
    lst[l], lst[j] = lst[j], lst[l]

    # 기준이 되는 값 return
    return j


def qsort(l, r):
    if l < r:                       # index 오른쪽 왼쪽 구분
        s = hPartition(l, r)   # 기준 index
        qsort(l, s-1)
        qsort(s+1, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    qsort(0, N-1)         # 왼쪽 끝, 오른쪽 끝 index
    print(f'#{tc} {lst[N//2]}')