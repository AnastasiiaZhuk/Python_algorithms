def zet_function(string):
    length = len(string)
    zet = [0]*length
    l, r, zet[0] = 0, 0, 0
    for i in  range(1, length):
        if i < r:
            if zet[i - l] < r - i:
                zet[i] = zet[i - l]
                continue
            l = i
        else:
            l = r = i
        while r < length and string[r - l] == string[r]:
            r += 1
        zet[i] = r - l
    return zet


string = 'aaaaa'
print(zet_function(string))