# MergeSort algorithm
def mergesort(lst, n):
    if n <= 1:
        return lst
    else:
        nleft = n // 2
        nright = n - nleft
        left = lst[0:nleft]
        right = lst[nleft:n]
        left = mergesort(left, nleft)
        right = mergesort(right, nright)
        lst = merge(lst, left, nleft, right, nright)
        return lst


def merge(lst, left, nleft, right, nright):
    i = j = k = 0
    while i < nleft and j < nright:
        if left[i] < right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    while i < nleft:
        lst[k] = left[i]
        i += 1
        k += 1

    while j < nright:
        lst[k] = right[j]
        j += 1
        k += 1

    return lst
