num_list = [3, 4, 5, 2, 1]

def solution(num_list):
    global multiplynumber, sumnumber
    multiplynumber = 1
    sumnumber = 0
    
    for element in num_list:
        multiplynumber *= element
        sumnumber += element

        sumnumber2 = sumnumber * sumnumber

        if multiplynumber > sumnumber2:
            answer = 1
            
    
        else :
            answer = 0
        
        return answer
        
result = solution(num_list)
print(result)
