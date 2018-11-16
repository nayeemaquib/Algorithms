def quick_sort(l):
    less = []
    equal =[]
    more = []

    if len(l) > 1:
        pivot = l[0]
        for i in l:
            if i < pivot:
                less.append(i)
            if i == pivot:
                equal.append(i)
            if i > pivot:
                more.append(i)
        return quick_sort(less)+quick_sort(equal)+quick_sort(more)

    else:
        return l

def quicksort(l):
    return quicksorthelper(l, 0, len(l)-1)

def quicksorthelper(l, low, high):
    if low < high:
        p = parition(l, low, high)
        quicksorthelper(l, low, p-1)
        quicksorthelper(l, p+1, high)
        return l

def get_pivot(l, low, high):
    mid = (low+high)//2
    pivot = high
    if l[low] < l[mid]:
        if l[mid] < l[high]:
            pivot = mid
    elif l[low] < l[high]:
        pivot = low

    return pivot

def parition(l, low, high):
    pivot_index = get_pivot(l, low, high)
    pivot_value = l[pivot_index]
    l[pivot_index], l[low] = l[low], l[pivot_index]
    border = low

    for i in range(low, high+1):
        if l[i] < pivot_value:
            border += 1
            l[i], l[border] = l[border], l[i]

    l[border], l[low] = l[low], l[border]
    return border

print(quick_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
print(quicksort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))