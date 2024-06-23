def solution(a, b):
    aString = a.split("")
    bString = b.split("")
    
    isTrue = True
    
    if len(aString) != len(bString):
        isTure = False
    
    else:
        for i in range(len(aString)):
            if aString[i] == bString[i]:
                isTrue = True
            else:
                isTrue = False
    
    answer = isTrue
    return answer
                
    
                
        