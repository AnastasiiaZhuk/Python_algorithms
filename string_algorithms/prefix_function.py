def prefix_function(string):
    length = len(string)
    prefix = [0]*length
    for i in range(1, length):
        j = prefix[i - 1]
        while j > 0 and string[i] is not string[j]:
            j = prefix[j - 1]
        if string[i] is string[j]:
            j += 1
        prefix[i] = j
    return prefix


string = 'abcabcd'
print(prefix_function(string))