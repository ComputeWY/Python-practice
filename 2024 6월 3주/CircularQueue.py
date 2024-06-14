class CircularQueue:
    
    def __init__(self, max = 50):
        self.items = [0 for i in range(max)]
        self.front = 0
        self.rear = 0
        self.max_length = max
        
    
    def enqueue(self, data):
        if self.is_full():
            raise Exception('QUEUE FULL ERROR')
        
        else:
            self.rear = (self.rear + 1) % self.max_length
            self.items[self.rear] = data
            
    def dequeue(self):
        if self.is_empty():
            raise Exception('QUEUE EMPTY ERROR!')
    
        else:
            self.front = (self.front + 1) % self.max_length
            del_data = self.items[self.front]
            
        
    def peek(self):
        return self.items[(self.front + 1) % self.max_length]
    
    def is_empth(self):
        return self.front == self.rear
    
    def is_full(self):
        return self.front == ((self.rear + 1) % self.max_length)
    
    def display(self):
        if self.is_empty():
            raise Exception('QUEUE EMPTY QRROR')
        
        else :
            
            for i in range(self.front + 1, self.rear + 1):
                
                if i == self.rear :
                    print ( '%3d' % self.items[i])
                    
                else:
                    print ('%3d -<' % self.items[i], end = "")
    
    