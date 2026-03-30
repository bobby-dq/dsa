from heapq import heappush, heappop

def top_k_frequent(arr, k):
    # we can use min-heaps to keep track which ones are the most
    # keep track of frequency first
    freq = {}
    for x in arr:
        # freq[x] = 1 + freq.get(x, 0)
        if x not in freq:
            freq[x] = 1
        else:
            freq[x] += 1
    
    heap = []
    for x in freq.keys():
        heappush(heap, (freq[x], x))
        if (len(heap) > k):
            heappop(heap)
            
    res = []
    for x in range(k):
        res.append(heappop(heap)[1])
    
    
    return res