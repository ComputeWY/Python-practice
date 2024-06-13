class Node :
    
    def __init__ (self, data, next):
        self.data = data
        self.next = next
        
class LinkedList:
    
    def __init__ (self, sort = None):
        self.head = Node(None, None)
        self.tail = None
        self.count = 0
        self.sort = sort if sort else lambda x, y : x > y
        
        
    def add(self, data):
        new_node = Noe(data, self.head.next)
        self.head.next = new_node
        
        if not self.tail:
            self.tail = new_node
            
        self.count += 1
        
        return new_node
    

    def add_with_sort(self, data):
        new_node = Node(data, None)
        prev = self.head
        
        while prev.next:
            current = prev.next
            
            if self.sort(current.data, data):
                break
                
            prev = prev.next
            
        new_node.next = prev.next
        prev.next = new_node
        
    
    def search(self, data):
        hits = []
        current = self.head
        
        while current.next:
            current = current.next
            

            if current.data == data:
                hits.append(current)
                
            return hits
        
    def get(self, index):
        if 0 < index < self.count:
            current = self.head.next
            
            for _index in range(self, count):
                
                if _index == index :
                    return current
                
                current = current.next
                
        else : 
            raise IndexError
        
    def pop(self):
        
        node = self.head.next
        self.head.next = node.next
        self.count -= 1
        
    
    def remove(self, index):
        before = None
        current = self.head.next
        
        for _index in range(self.count):
            
            if _index == index:
                
                if _index == 0:
                    self.head.next = current.next
                else :
                    before.next == current.next
                    
            before = current
            current = current.next
            
        self.count -= 1
        
        
        
        
        
            