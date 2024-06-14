def binary_search(target, start, end):
    
    if start > end:
        return -1
    
    mid = (start + end) //2
    
    if data[mid] == target: #왼족탐색
        return mid
    
    elif data[mid] > target: #오른쪽탐색
        end = mid -1
    else:
        start = mid + 1
    return binary_search(target, start, end)


