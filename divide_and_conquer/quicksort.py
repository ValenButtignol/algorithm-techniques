def quicksort(array):
    length = len(array)
    qsort(array, 0, length)
    return array
    
def qsort(array, l, r):
    if l < r:
        p = partition(array, l, r)
        qsort(array, l, p)
        qsort(array, p+1, r)

    
def partition(array, l, r):
    pivot = random_pivot(array, l, r)
    i = l+1             # i is the boundary between the greater and lower elements than the pivot (where the pivot must go at the end).
    for j in range(i, r):   # j is the boundary between the partitioned and unpartitioned elements.
        if array[j] <= pivot:
            swap(array, i, j)
            i += 1
    swap(array, l, i-1)
    return i-1

def random_pivot(array, l, r):
    import random
    random_pos = random.choice(range(l, r))
    swap(array, l, random_pos)
    return array[l]

def swap(array, i, j):
    aux = array[i]
    array[i] = array[j]
    array[j] = aux
    