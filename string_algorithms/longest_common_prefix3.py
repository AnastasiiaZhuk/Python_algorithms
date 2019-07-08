def common(s1, s2):
    if not s1 or not s2:
        return ""
    k = 0
    while s1[k] == s2[k]:
        k += 1
        if k >= len(s1) or k >= len(s2):
            return s1[0:k]
    return s1[0:k]

def longest_common_pref(strs, left, right):
    if not strs:
        return ""
    return longets_pref(strs, 0, len(strs) -1 )

def longets_pref(strs, left, right):
    if left == right:
        return strs[left]
    mid = (left + right)//2
    lcp_lefr = longets_pref(strs, left, mid)
    lcp_right = longets_pref(strs, mid + 1, right)
    return common(lcp_lefr, lcp_right)

strr = ['abca', 'abcc', 'abcd']
print(longest_common_pref(strr, 0, len(strr) -1 ))