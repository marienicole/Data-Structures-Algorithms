def compression(string):
    i = 0
    letters = {i:""}
    for c in string:
        if c in letters[i]:
            letters[i][c] += 1
        else:
            i += 1
            letters[i] = { c : 1 }

    str2 = ""
    del letters[0]
    for j in letters:
        letter, number = letters[j].popitem()
        str2 += letter
        str2 += str(number)

    if len(str2) > len(string):
        return string
    else:
        return str2

print("aabbccaa compresses to: %s" % compression("aabbccaa"))
print("adfdsdddbbee compresses to: %s" % compression("adfdsdddbbee"))
print("aaaaaaaaaaavvccccc compresses to: %s" % compression("aaaaaaaaaaavvccccc"))
print("aardvark compresses to: %s" % compression("aardvark"))
print("yraasfdafhertewrwe compresses to: %s" % compression("yraasfdafhertewrwe"))
print("dfsgsdhtttttttttt compresses to: %s" % compression("dfsgsdhtttttttttt"))
