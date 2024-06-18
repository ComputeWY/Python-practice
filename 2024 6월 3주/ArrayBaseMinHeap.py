class ArrayBaseMinHeap:
#배열기반최소히프클래스
    #배열기반최소히프초기화함수
    def __init__(self, len):
        self.data = [0 for _ in range(len)]
        self.count = 0
        self.max_len = len
        
        
    #배열기반최소히프공백검사함수
    def is_empty(self):
        return self.count == 0
    
    #배열기반최소히프포화검사함수
    def is_full(self):
        return self.count == (self.max_len - 1)
    
    #배열기반최소히프삽입함수
    def insert_min_heap (self,data):
        if self.is_full():
            print("HEAP FULL ERROR")
            return
        
        self.count += 1
        i = self.count
        
        while i != 1 and data < self.data[i // 2] :
            self.data[i] = self.data[ i // 2]
            i //= 2
            
        self.data[i] = data
        
    #배열기반최소히프삭제함수
    def delete_min_heap(self):
        if self.is_empty():
            print("HEAP EMPTY ERROR")
            return
        
        parent, child = 1, 2
        
        item = self.data[i]
        temp = self.data[self.count]
        self.count -= 1
        
        while child <= self.count:
            if child < self.count and self.data[child] > self.data[child + 1]:
                child += 1
                
            if temp <= self.data[child]:
                break
            
            self.data[parent] = self.data[child]
            parent, child = child, child * 2
            
        self.data[parent] = temp
        
        return item
    
    #배열기반최소히프중위순회함수
    def inorder_traversal(self, idx):
        if idx > self.count:
            return
        
        self.inorder_traversal (2 * idx)
        print (self.data[idx], edn ="")
        self.inorder_traversal ( 2* idx + 1)