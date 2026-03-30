def group_anagrams(strs):
    group = {}
    for x in strs:
        k = [0] * 26
        for i in x:
            k[ord(i) - ord('a')] += 1
        k = tuple(k)
        if k not in group:
            group[k] = [x]
        else:
            group[k].append(x)
        
    return group.values()