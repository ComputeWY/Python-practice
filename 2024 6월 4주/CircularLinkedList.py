class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
    #원형 연결 리스트 클래스
    
    class CircularLinkedList :
        
        def __init__(self):
            self.head = None
            self.tail = None
            
        #원형 연결 리스트 맨 앞 삽입 함수
    
        def add_first(self,data):
            new_node = Node(data)
            
            if self.head is None:
                self.head = self.tail = new_node
                
            else :
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
                
        # 원형 연결 리스트 맨 뒤 삭제 함수
        def delete_last(self):
            if self.is_empty():
                raise Exception('LIST EMPTY ERROR!')
            
            del_node = self.tail
            p_node = self.head
            
            while p_node.next is not self.tail:
                p_node = p_node.next
                
            p_node.next = del_node.next
            self.tail = p_node
            
            del del_node
            
            
            
        #원형 연결 리스트 공백 확인 함수
        def is_empty(self):
            return self.head == None and self.tail == None
        
        
        #원형 연결 리스트 출력 함수
        def display(self, node):
            
            temp = node
            
            while True :
                
                if temp.next is node:
                    print(temp.data, end="")
                    
                else:
                    print(str(temp.data) + '->', end ="")
                    
                temp = temp.next
                if temp is node:
                    break
                
                print()
        
        
            