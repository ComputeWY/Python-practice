def computeLPS(pat):
    lps = [0] * len(pat)
    length = 0
    i = 1
    
    while i < len(pat):
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i +=1
        else:
            if length != 0:
                length = lps[length -1]
            else :
                lps[i] = 0
                i += 1
                
        return lps
    
def computeKmp(all_string, pattern):
    result = []
    i = 0
    for j in range(len(all_string)):
        while i > 0 and pattern[i] != all_string[j]:
            i = table[i-1]
        if pattern[i] == all_string[j]:
            i += 1
            if i == len(pattern):
                result.append(j - i + 1)
                i = table[i-1]
                
    return result