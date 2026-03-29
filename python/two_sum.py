def two_sum(arr, t):
    hm = {}
    for i in range(len(arr)):
        diff = t - arr[i]
        if diff in hm:
            return [i, hm[diff]]
        hm[arr[i]] = i
    return []