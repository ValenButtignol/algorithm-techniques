# Count inversions of an array
def sort_and_count_inversions(lst, n):
    if n <= 1:
        return 0
    else:
        left = lst[0 : n // 2]
        right = lst[n // 2 : n]
        left_inv = sort_and_count_inversions(left, n // 2)
        right_inv = sort_and_count_inversions(right, n - n // 2)
        split_inv = merge_and_count(lst, n, left, n // 2, right, n - n // 2)
        return left_inv + right_inv + split_inv


def merge_and_count(lst, n, left, nleft, right, nright):
    i = j = k = inversions = 0
    while i < nleft and j < nright:
        if left[i] < right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
            inversions += nleft - i
            # Both halves are sorted, so we add the remaining elements from the left array
            # Particular case example: left = [4,5] right = [1,2,3]
        k += 1

    while i < nleft:
        lst[k] = left[i]
        i += 1
        k += 1

    while j < nright:
        lst[k] = right[j]
        j += 1
        k += 1

    return inversions

