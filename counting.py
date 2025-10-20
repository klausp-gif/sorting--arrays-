def counting_sort(array):
    # find largest and smallest elements
    lb = array[0]
    ub = lb
    for i in range(1, len(array)):
        elem = array[i]
        if elem < lb: lb = elem
        if elem > ub: ub = elem

    # initialize and find counts
    counts = [0 for _ in range(ub - lb + 1)]
    for i in range(len(array)):
        counts[array[i] - lb] += 1

    # counts to elements in array
    j = 0 # index into array
    for i in range(len(counts)):
        while counts[i] > 0:
            array[j] = i + lb
            counts[i] -= 1
            j += 1

def time_sort(algo, n):
    import time, random

    # n samples with replacement from [0,1,...,n-1]
    data = random.choices(range(n), k=n)

    start = time.process_time()
    algo(data)
    end = time.process_time()
    return end - start

print(time_sort(counting_sort, 10**6))

array = [2, 11, 4, 15, 34, 0]
counting_sort(array)
print(array)