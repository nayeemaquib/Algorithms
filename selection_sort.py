# The first one is min_index
# Then compare it with other indices incrementally and change the min_index accordingly
# Swap the min_index value with the left most value(initial min_index) if it is not already
# Repeat this process for n times until the list is sorted

def selection_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i+1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        if min_index != i:
            l[i], l[min_index] = l[min_index], l[i]
    return l

print(selection_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))


