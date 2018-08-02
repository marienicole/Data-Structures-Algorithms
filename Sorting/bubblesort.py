small = [1, 6, 7, 23, 44, 2, 8, 15]

def bubblesort(array):
    for i in range(len(array)-1):
        for j in range(i, len(array)-1):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

bubblesort(small)
print(small)
