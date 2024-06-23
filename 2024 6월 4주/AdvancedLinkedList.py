#DoublyLinkedList

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
        
        #이중 연결 리스트 맨앞 삽입 함수
        def add_first(self,data):
            new_node = Node(data)
            new_node_next = self.head
            
            if self.head is not None:
                self.head.prev = new_node
                
            if self.tail is None:
                self.tail = new_node
            
            self.head = new_node
            
        #이중 연결 리스트 특정 노드 삭제 함수
        def delete_node(self,data):
            if self.is_empty():
                raise Exception('LIST EMPTY ERROR')
            
            del_node = self.head
            count = 0
            
            while del_node:
                
                if del_node.data == data:
                    del_node.prev.next = del_node.next
                    del_node.next.prev = del_node.prev
                    del del_node
                    count += 1
                    del_node = self.head
                    
                del_node = del_node.next
            return count
        
        #이중연결리스트 공백 확인 함수
        def is_empty(self):
            return self.head == None and self.tail == None
        
        #이중연결 리스트 출력 함수
        def display(self, node):
            while(node is not None):
                
                if node.next == None:
                    print(str(node.data), end ="")
                    
                else:
                    print(str(node.data) + '->', end="")
                    
                last = node
                node = node.next
                
            print()
                    