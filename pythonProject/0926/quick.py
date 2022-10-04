def partition(l, r):
    pivot = A[l]
    i, j = l, r
    while i <= j:       # i, j 교차되기 전까지
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:       # i, j 떨어져있는 경우
            A[i], A[j] = A[j], A[i]
    # while 종료 후 pivot 값을 자기 자리로
    A[l], A[j] = A[j], A[l]
    return j

def qsort(l, r):
    if l < r:
        s = partition(l, r)
        qsort(l, s-1)
        qsort(s+1, r)

A = [7, 2, 5, 3, 4, 5]
N = len(A)
qsort(0, N-1)       # r-1까지
print(A)