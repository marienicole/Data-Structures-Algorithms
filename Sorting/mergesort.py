def merge(arr, mid, left, right):
    a1_end = mid - left
    a2_begin = right - mid

    print("a1 and a2 %d %d" % (a1_end, a2_begin))

    l_arr = arr[int(left):int(a1_end + 1)]
    r_arr = arr[int(a2_begin):int(right + 1)]

    i = 0
    j = 0
    k = left

    while i < a1_end-1 and j < a2_begin-1:
        if l_arr[i] < r_arr[j]:
            print("%d %d" %(i,j))
            arr[k] = l_arr[i]
            i+=1
        else:
            arr[k] = r_arr[j]
            j+=1
        k+=1

    k = 0
    for m in range(len(l_arr) - 1):
        arr[k] = l_arr[m]
        k+=1

    for n in range(len(r_arr) - 1):
        arr[k] = r_arr[n]
        k+=1

def mergesort(arr, left, right):
    # left, right, and mid are *indicies*
    # ex l 0, r 24, m 12
    if left < right:
        mid = (left+(right-1))/2
        print("mid is %d "% mid)

        mergesort(arr, left, mid)
        mergesort(arr, mid + 1, right)
        merge(arr, mid, left, right)

arr = [1, 8, 2, 9, 3, 5, 4, 7, 4, 6, 4, 6, 8, 7, 8, 9]
mergesort(arr, 0, len(arr) - 1)
