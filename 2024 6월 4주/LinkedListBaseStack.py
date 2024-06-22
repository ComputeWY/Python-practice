class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedListBaseStack:
    
    def __init__(self):
        self.top = None
        
    # 연결 리스트 기반 스택 삽입 함수
    
    def push(self, data):
        new_node = Node(data)
        
        if self.top is None:
            self.top = new_node
            
        else:
            new_node.next = self.top
            self.top = new_node
            
    # 연결 리스트 기반 스택 삭제 함수
    def pop(self):
        
        if self.is_empty():
            raise Exception('STACK EMPTY ERROR')
        
        else:
            del_node = self.top
            del_data = del_node.data
            self.top = self.top.next
            del del_node
            
            return del_data
        
    #연결 리스트 기반 스택 참조 함수
    
    def peek(self):
        if self.is_empty():
            raise Exception('STACK EMPTY ERROR')
        
        else:
            temp = self.top
            
            while temp is not Node:
                print('|%3d|' % temp.data)
                
                temp = temp.next
                
                print("---------")