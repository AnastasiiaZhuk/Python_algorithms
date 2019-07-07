def binary_add(str1, str2):
    result = ""
    c, i, j = 0, len(str1) - 1, len(str2) - 1
    zero = ord('0') #(int) unicode code point of parameter
    while i >= 0 or j >= 0 or c == 1:
        if i >= 0:
            c += ord(str1[i]) - zero
            i -= 1
        if j >= 0:
            c += ord(str2[j]) - zero
            j -= 1
        result = chr(c % 2 + zero) + result
        c //= 2
    return result


print(binary_add('11', '1'))