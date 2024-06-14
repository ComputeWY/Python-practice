class ArrayBaseQueue:
    
    def __init__(self, max = 50):
        self.items = []
        self.front = 0
        self.rear = 0
        self.max_length = max
    
    def enqueue(self, data):
        if self.is_full():
            raise Exception('Queue FULL ERROR!')
        
        else :
            self.items.append(data)
            self.rear += 1
            
    def dequeue(self):
        if self.is_empty():
            raise Exception('QUEUE EMPTY ERROR!')
    
        else:
            del_data = self.items[self.front]
            self.front += 1
            
            return del_data
        
        
        #배열기반 선형 큐 공백 확인 함수
        
    def is_empty(self):
        return self.front == self.rear
    
    def is_full(self):
        return self.rear == self.max_length -1
    
    #배열 기반 선형 큐 출력 함수
    
    def display(self):
        for i in range(self.front, self.rear):
            if i == self.rear - 1:
                print(self.items[i])
            else:
                print(f'{self.items[i]} <-', end=' ')

if __name__ == '__main__':
    
    queue = ArrayBaseQueue()
    
    
    
    
        