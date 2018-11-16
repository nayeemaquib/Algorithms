# Divide and Conquer
# Divide all the items of a list into single item sublists

def merge_sort(l):
    if len(l) > 1:
        mid = len(l)//2
        left = l[:mid]
        right = l[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i+=1
            else:
                l[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            l[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            l[k] = right[j]
            j+=1
            k+=1
    return l



print(merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))