def selection_sort(array):
    for i in range(len(array) - 1):
        minv = array[i]
        mini = i
        for j in range(i+1, len(array)):
            if array[j] < minv:
                minv = array[j]
                mini = j
        if mini != i:
            array[mini] = array[i]
            array[i] = minv
        print(array)

array = [-4, 11, 7, -12, 6, 1]
print(selection_sort(array))
