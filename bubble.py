def bubble_sort(array):
    sorted = False
    while not sorted:
        sorted = True
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                (array[j], array[j+1]) = (array[j+1], array[j])
                sorted = False
    return array

array = [7, 9, 11, 2]
print(bubble_sort(array))