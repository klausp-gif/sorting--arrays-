def insertion_sort(array):
    i = 1
    while i < len(array):
        val = array[i]
        j = i - 1
        while j >= 0 and array[j] > val:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = val
        i += 1
    return array

a = [9, 7, 2, 11]
print(insertion_sort(a))
