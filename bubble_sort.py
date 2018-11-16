# We compare the items pairwise
# If left one is bigger then the right one, then we swap place
# Keep doing it until the list is sorted

def bubble_sort(l):
    for i in range(len(l)):
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

print(bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

