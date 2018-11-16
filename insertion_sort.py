# The first item is sorted since its only 1 item list as sublist
# So second from second item and compare it to the left side, if it's smaller then swap
# Keep going incrementally and build sorted sublist gradually and turn it into the whole list

def insertion_sort(l):
    count = 0
    for i in range(1, len(l)):
        j = i-1
        while j >= 0 and l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            j -= 1

    return l

print(insertion_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))


