def solution(num_list):

    lista = []
    listb = []
    for numbers in num_list:
        if numbers %2 == 0:
            lista.append(numbers)
        else :
            listb.append(numbers)

    def array_to_decimal(listc):
        num_str = ''.join(map(str, listc))
        result = int(num_str)
        return result
    
    answer = array_to_decimal(lista) + array_to_decimal(listb)
    return answer

