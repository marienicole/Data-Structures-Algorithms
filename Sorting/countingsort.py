# stable sorting algorithm O(n+k), n items in original array, k is range of
# items that could be in the array

array1 = [26,21,44,25,50,49,21,28,51,32,62,59,32,24,62,30,19,39,55,21,62,52,55,22,32,61,58,49,50,55,25,52,44,37,56,57,48,18,49,29,43,59,47,44,52,19,34,56]
array2 = [52,48,38,44,58,27,23,53,18,49,49,55,43,43,21,22]
array3 = [31,51,64,60,18,40,53,63,61,49,53,29,35,42,51,49,34,62,47,58,42,29,46,51,43,19,18,44,33,40,44,39]
array4 = [48,36,64,52,43,59,60,61,50,34,39,55,37,24,63,52,65,45,63,51,59,53,48,25,59,53,19,26,36,24,28,51,52,43,38,29,27,53,60,19,18,32,61,21,50,19,58,48,63,40,46,62,60,49,57,52,19,20,40,47,40,43,54,37,25,51,24,52,19,43,52,37,59,43,46,39,23,21,38,60,60,43,45,34,62,45,65,33,53,61,55,47,57,28,20,25,64,48,20,46,23,59,27,52,24,29,56,62,30,21,30,18,35,32,25,28,41,24,31,63,50,41,35,25,35,21,37,46,52,41,45,58,62,33,37,42,30,29,23,25,44,54,44,34,21,64,62,30,33,21,54,28,38,27,27,55,28,44,38,33,49,51,45,56,38,52,35,60,39,40,32,65,30,42,19,54,61,37,29,46,22,64,35,62,37,64,55,29,28,23,18,40,56,55,58,59,41,60,27,27,53,62,23,18,50,35,32,49,20,59,34,25,26,52,41,55,54,46,31,26,61,59,36,48,33,44,37,55,53,28,34,32,25,58,35,43,44,54,58,62,44,39,21,24,63,44,37,42,29,55,63,47,22,36,58,34,21,19,22,30,35,41,30,50,43,18,35,50,61,58,31,30,34,45,51,23,27,63,39,26,37,56,34,39,40,50,36,46,51,45,20,45,45,51,50,21,64,27,29,23,58,31,21,28,44,42,19,44,27,26,42,25,59,41,20,50,34,59,36,27,29,20,50,43,42,40,65,29,44,18,20,49,54,45,65,43,54,37,27,37,30,57,23,50,58,57,29,28,22,23,53,38,42,63,43,61,60,19,50,47,51,43,58,24,62,44,18,28,20,49,50,41,52,22,64,51,21,25,59,29,46,60,28,29]
def counting_sort(array, max):
    if array == [] or len(array) == 1:
        return array

    max_plus = max + 1
    sorted = [0] * max_plus

    for e in array: #O(n)
        sorted[e] += 1

    i = 0
    for j in range(max_plus):
        for k in range(sorted[j]):
            array[i] = j
            i += 1
    return array

# create empty array, one larger than the maximum value
# for each number in the array, increment that index by ONE (total occurances)
# for each number in the counts array, replace that number with whatever is next
# in the sorted array( 3 5's, 4 4's, etc)
# does not compare values against eachother!

'''
calling countingsort
'''

m1 = max(array1)
m2 = max(array2)
m3 = max(array3)
m4 = max(array4)

print("Original array: ", array1)
print("sorted array: ", counting_sort(array1, m1))
print()
print("Original array: ", array2)
print("sorted array: ", counting_sort(array2, m2))
print()
print("Original array: ", array3)
print("sorted array: ", counting_sort(array3, m3))

print()
print()
print("Original array: ", array4)
print("sorted array: ", counting_sort(array4, m4))
