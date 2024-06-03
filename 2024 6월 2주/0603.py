def heapify(li, idx, n):

    # li : 힙으로 만들고자 하는 배열
    # idx : 선택된 노드
    # n : 힙의 범위

    left = idx * 2 #자식의 왼쪽 노드
    right = idx * 2 + 1 #자식의 오른쪽 노드
    s_idx = idx

    if left <= n and li[s_idx] > li[left]:
        s_idx = left
    if right <= n and li[s_idx] > li[right]:
        s_idx = right

    if s_idx != idx:
        li[idx],li[s_idx] = li[s_idx], li[idx]

        return heapify(li, s_idx, n)
    
def heap_sort(array):

    n = len(array)

    array = [0] + array
    
    ans= []

    for i in range(n//2, 0, -1):
        heapify(array, i , n)

    
    for i in range(n, 0, -1):
        ans.append(array[i])
        array[i], array[1] = array[1], array[i]
        heapify(array, 1, i-1)

    return ans

    