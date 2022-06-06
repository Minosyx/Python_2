import asyncio
from time import time

async def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2

        L = array[:mid]
        R = array[mid:]

        task1 = mergeSort(L)
        task2 = mergeSort(R)

        grupa = asyncio.gather(task1, task2)

        await grupa

        await merge(array, L, R)
        

        
 
async def merge(array, L, R):
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

async def main():
    t = time()
    tab = [1, 8, -2, 0, -6, 101, 11, -8]
    print(tab)
    await mergeSort(tab)
    print(tab)
    print(time() - t)


asyncio.run(main(), debug=True)
