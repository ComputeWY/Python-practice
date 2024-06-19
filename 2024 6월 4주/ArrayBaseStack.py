class ArrayBaseStack:
    def __init__(self, max_length = 50):
        self.items = []
        self.top = -1
        self.max_length = max_length
        
    #배열 기반 스택 삽입 함수
    def push(self,data):
        if self.is_full:
            raise Exception('STACK FULL ERRROR')
        
        self.item.append(data)
        self.top += 1
        
        
    #배열 기반 스택 삭제함수
    def pop(self):
        if self.is_empty():
            raise Exception('STACK EMPTY ERROR!')
        
        data = self.items[self.top]
        self.top -= 1
        
        return data

    #배열기반스택참조함수
    def peek(self):
        if self.is_empty():
            raise Exception('STACK EMPTY ERROR!')
        
        return self.items[self.top]
    
    #배열기반 스택 포화 확인 함수
    def is_full(self):
        return self.top == self.max_length - 1
    
    #배열 기반 스택 출력 함수
    def display(self):
        index = self.top
        
        while index >= 0:
            print('|%3d|' % self.items[index])
            
            print('└─────┘')
        
        