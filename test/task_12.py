def binary_search(list, elem):
    min_ind = 0
    max_ind = len(list) - 1

    while min_ind < max_ind:
        i = round(min_ind + (max_ind-min_ind) / 2)
        if list[i] < elem:
            min_ind = i+1
        elif list[i] > elem:
            max_ind = i-1
        else:
            return i

    if min_ind == max_ind and list[min_ind] == elem:
        return min_ind

    return -1

# Test
list = []
print(binary_search(list, 5))

list = [5]
print(binary_search(list, 5))

list = [1,2,3,4,5,6,7,8,9]
print(binary_search(list, 5))
