def Shellsort(arr):
    n = len(arr)
    h = 1
    # Calculate the initial gap value using Knuth's sequence
    while h < n // 3:
        h = 3 * h + 1

    # Perform sorting with decreasing gap values
    while h > 0:
        for i in range(h, n):
            key = arr[i]
            j = i
            # Perform insertion sort with the current gap
            while j >= h and arr[j - h] > key:
                arr[j] = arr[j - h]
                j -= h
            arr[j] = key
        h //= 3

    return arr

# Example usage
arr = [23, 12, 1, 8, 34, 54, 2, 3, 7, 4]
print("Original array:", arr)
Shellsort(arr)
print("Sorted array:", arr)
