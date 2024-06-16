#ArrayBaseMaxHeap

class ArrayBaseMaxHeap:
    
    #배열 기반 최대 히프 초기화 함수
    def __init__(self, len):
        self.data = [0 for _ in range(len)]
        self.count = 0
        self.max_len = len
        
    
    #베열 기반 최대 히프 공백 검사 함수
    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.count == (self.max_len - 1)
    
    #배열 기반 최대 히프 삽입 함수
    def insert_max_heap(self, data):
        if self.is_full():
            print("HEAP FULL ERROR")
            return
        self.count += 1
        i = self.count
        
        while i != 1 and data > self.data[i //2]:
           #self.data[i // 2] -> 현재노드 i의 부모노드
            self.data[i] = self.data[i//2]
            i//2
            
        self.data[i] = data
        
        
    #배열 기반의 최대 히프 삭제 함수
    def delete_max_heap(self):
        if self.is_empty():
            print('HEAp EMPTY ERROR')
            return
    
        parent, child = 1, 2
        
        item = self.data[i]
        temp = self.data[self.count]
        self.count -= 1
        
        while child <= self.count:
            if child < self.count and self.data[child] < self.data[child + 1]:
                child += 1
                
            if temp >= self.data[child]:
                break
            
            self.data[parent] = self.data[child]
            parent,child = child, child*2
            
        self.data[parent] = temp
        
        return item
    
        #배열 기반 최대 히프 중위 순회 함수
        
    def inorder_traverssal(self, idx):
        if idx > self.count:
            return
        
        self.inorder_traverssal(2*idx)
        print(self.data[idx], end="")
        self.inorder_traverssal(2 * idx + 1)
        
    