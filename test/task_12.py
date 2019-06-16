list = [-1,20,30]

def binary_search(list, elem):
    min_ind = 0
    max_ind = len(list) - 1

    while (min_ind < max_ind):
        i = round((max_ind-min_ind) / 2)
        if list[i] < elem:
            min_ind = i+1
        elif list[i] > elem:
            max_ind = i-1
        else:
            return i

    if min_ind == max_ind and list[min_ind] == elem:
        return min_ind

    return -1


print(binary_search(list, 31))
