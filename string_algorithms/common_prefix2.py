def common_prefix(strs):
    if not strs:
        return ""
    for i in range(len(strs[0])):
        for string in strs[1:]:
            if i == len(string) or string[i] != strs[0][i]:
                return strs[0][0:i]
    return strs[0]


strs = ['all', 'allie', 'allen']
print(common_prefix(strs))