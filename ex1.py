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

def time_sort(algo, n):
    import time, random

    # n samples with replacement from [0,1,...,n-1]
    data = random.choices(range(n), k=n)

    start = time.process_time()
    algo(data)
    end = time.process_time()
    return end - start

print(time_sort(selection_sort, 8*10**3))