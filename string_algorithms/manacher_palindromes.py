def manacher_for_palindroms(str):
    string = '#'.join('^{}$'.format(str))#copy of string with unique chars on even position
    n = len(string)
    palindrome = [0] * n
    centr = right = 0
    for i in range(1, n - 1):
        palindrome[i] = (right > i) and min(right - i, palindrome[2 * centr - i])  # equals to  C - (i-C) ~ like mirror
        while string[i + 1 + palindrome[i]] == string[i - 1 - palindrome[i]]:
            palindrome[i] += 1
        if i + palindrome[i] > right: #if we reach right boundary unpdate the center
            centr, right = i, i + palindrome[i]

    max_lenght, centerIndex = max((n, i) for i, n in enumerate(palindrome))
    return str[(centerIndex - max_lenght) // 2: (centerIndex + max_lenght) // 2]

str = 'abacabaaaaa'
print(manacher_for_palindroms(str))