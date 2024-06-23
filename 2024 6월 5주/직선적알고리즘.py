def solution(a, b):

    isFalse = False

    if len(a) != len(b):
        isTure = True

    else:
        for i in range(len(a)):
            if a[i] == b[i]:
                isFalse = False
            else:
                isFalse = True

    answer = not isFalse
    print(answer) 

a = "String"
b = "String"

solution(a,b)
                
    
                
        
