
def recursive(n): # O(n^2)
    if n == 0:
        return n
    elif n == 1:
        return 1
    else:
        return (recursive(n-1) + recursive(n-2))

def iterative(n): # O(n)
    one = 1
    two = 0
    for i in range(1, n): # start  at one becasue we've computed two indicies
        cur = one + two
        two = one
        one = cur
        i += 1

    return cur

n = int(input("Please enter the value to compute > "))
print(recursive(n))
print(iterative(n))
