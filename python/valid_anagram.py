def is_anagram(str1, str2):
    
    if len(str1) != len(str2):
        return False
    
    track = {}
    for i in str1:
        if i in track:
            track[i] += 1
        else:
            track[i] = 1
    
    for i in str2:
        if i in track:
            track[i] -= 1
        else:
            return False
    
    for i in track:
        if track[i] != 0:
            return False
    
    return True