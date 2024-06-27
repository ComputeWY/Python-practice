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
        