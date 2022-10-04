import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def merge(l, r):
    global cnts
    idxL, idxR = 0, 0
    res = []

    while idxL < len(l) or idxR < len(r):         # 두 리스트에 원소가 남아있을 때
                                                    # (인덱스가 리스트의 마지막 인덱스보다 작을 때)
        if idxL < len(l) and idxR < len(r):
            if l[idxL] < r[idxR]:                # 크기 비교 후 더 작은 값 추가
                res.append(l[idxL])
                idxL += 1
            else:
                res.append(r[idxR])
                idxR += 1

        elif idxL < len(l):                    # 한 리스트에만 원소가 있을 때
            res.append(l[idxL])            # 남아있는 원소 다 추가
            idxL += 1

        elif idxR < len(r):
            res.append(r[idxR])
            idxR += 1

    # 마지막 값 비교 후 counting
    if l[-1] > r[-1]:
        cnts += 1


    return res

def merge_sort(lst):
    # 더이상 분할할  수 없을 때
    if len(lst) == 1:
        return lst

    m = len(lst) // 2

    # 왼쪽 오른쪽 분할
    l = merge_sort(lst[:m])
    r = merge_sort((lst[m:]))

    return merge(l, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnts = 0
    print(f'#{tc} {merge_sort(lst)[N//2]} {cnts} ')

