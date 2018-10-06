def edit_distance(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    edit_dist = 0
    if str1 == str2:
        return True
    elif len(str1) == len(str2): # same length
        for c in range(len(str1)-1):
            if str1[c] != str2[c]:
                if edit_dist == 1:
                    return False
                else:
                    edit_dist += 1
    else:
        if len(str1)-1 == len(str2): # first is one longer
            longest = str1
            shortest = str2
        elif len(str2)-1 == len(str1): # second is one longer
            longest = str2
            shortest = str1
        else: # more than 2 edits
            return False
        for c in range(len(longest)-1):
            if edit_dist == 1:
                return False
            elif longest[c] != shortest[c]:
                shortest = shortest[:c] + " " + shortest[c:]
                edit_dist += 1
    return True


print("Yes and Yet: %s" % edit_distance("yes", "yet"))
print("Cat and Cart: %s" % edit_distance("Cat", "Cart"))
print("Cat and Catty: %s" % edit_distance("Cat", "Catty"))
print("Space and Space: %s" % edit_distance(" ", ""))

edit_distance
