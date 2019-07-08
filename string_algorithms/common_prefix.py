def common_prefix(str1, str2):
    if not str1 or not str2:
        return ""
    k = 0
    while str1[k] == str2[k]:
        k += 1
        if k >= len(str1) or k >= len(str2):
            return str1[0 : k]
    return str1[0 : k]

def common_of_all_strs(strs):
    if not strs:
        return ""
    result = strs[0]
    for i in strs:
        result = common_prefix(result, i)
    return result


strs = ['all', 'allie', 'allen']
print(common_of_all_strs(strs))