from time import time


def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2

        L = array[:mid]
        R = array[mid:]

        mergeSort(L)
        mergeSort(R)

        merge(array, L, R)


def merge(array, L, R):
    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        array[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        array[k] = R[j]
        j += 1
        k += 1



t = time()
tab = [1, 8, -2, 0, -6, 101, 11, -8]
print(tab)
mergeSort(tab)
print(tab)
print(time() - t)

