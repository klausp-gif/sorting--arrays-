def bubble_sort(array):
    sorted = False
    while not sorted:
        sorted = True
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                (array[j], array[j+1]) = (array[j+1], array[j])
                sorted = False
        print(array)
    return array

array = [-4, 11, 7, -12, 6, 1]
print(bubble_sort(array))