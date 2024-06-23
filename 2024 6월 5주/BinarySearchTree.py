#BinarySearchTree

class Node:
    
    def __init__(self, data):
        self.rnode = None
        self.lnode = None
        self.data = data
        
    
class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        
        #이진 탐색 트리 삽입 함수
        def insert(self,data):
            self.root = self._insert_value(self.root, data)
            
            return self.root is None
        
        def _insert_value(self, node, data):
            if node is None:
                node = Node(data)
                
            else:
                if data <= node.data:
                    node.lnode = self._insert_value(node.lnode, data)
                else:
                    node.rnode = self._insert_value(node.rnode, data)
                    
        def find(self,key):
            return self._find_value(self.root, key)
        
        def _find_value(self,root,key):
            if root is None or root.data == key:
                return root is not None
        
            elif key < root.data:
                return self._find_value(root.lnode, key)
            
        #이진 탐색 트리 삭제함수
        class BST:
            def __init__(self):
                self.root = None
            
            def delete(self, key):
                self.root, deleted = self._delete_value(self.root, key)
                return deleted

            def _delete_value(self, , nodekey):
                if node is None:
                    return node, False
                
                deleted = False
                
                if key == node.data:
                    deleted = True
                    
                    if node.lnode and node.rnode:
                        parent, child = node, node.rnode
                        
                        while child.lnode is not None:
                            parent, child = child, child.lnode
                            
                        child.lnode = node.lnode
                        
                        if parent != node:
                            parent.lnode = child.rnode
                            child.rnode = node.rnode
                            
                        node = child
                        
                    elif node.lnode or node.rnode:
                        node = node.lnode or node.rnode
                        
                    else:
                        node = None
                elif key < node.data:
                    node.lnode, deleted = self._delete_value(node.lnode, key)
                else:
                    node.rnode, deleted = self._delete_value(node.rnode, key)
                    
                return node, deleted
        
            '''
    트리 순회 알고리즘

    - 깊이 우선 순회(Depth First Traversal)
        1. 전위 순회(Pre-order traversal)
        2. 중위 순회(In-order traversal)
        3. 후위 순회(Post-order traversal)

    - 너비 우선 순회(Breadth First Traversal)
        1. 레벨 순회(Level-order traversal)
    '''
    
    # 이진 탐색 트리 전위 순회 함수
    def pre_order_traversal(self) :
        def _pre_order_traversal(root) :
            if root is None :
                pass

            else :
                print(root.data, end = ' ')
                _pre_order_traversal(root.lnode)
                _pre_order_traversal(root.rnode)

        _pre_order_traversal(self.root)
        print()
        
        
    # 이진 탐색 트리 중위 순회 함수
    def pre_order_traversal(self) :
        def _pre_order_traversal(root) :
            if root is None :
                pass

            else :
                
                _pre_order_traversal(root.lnode)
                print(root.data, end = ' ')
                _pre_order_traversal(root.rnode)

        _pre_order_traversal(self.root)
        print()
        
    # 이진 탐색 트리 후위 순회 함수
    def pre_order_traversal(self) :
        def _pre_order_traversal(root) :
            if root is None :
                pass

            else :
                
                _pre_order_traversal(root.lnode)
                _pre_order_traversal(root.rnode)
                print(root.data, end = ' ')

        _pre_order_traversal(self.root)
        print()
        
    def level_order_traversal(self):
        def _lever_order_traversal(root):
            queue = [root]
            
            while queue:
                root = queue.pop(0)
                
                if root is not None:
                    print(root.data, end='')
                    
                    if root.lnode:
                        queue.append(root.lnode)
                    if root.rnode:
                        queue.append(root.rnode)
                        
            _lever_order_traversal(self.root)
            print()
                        
                
            
        
                    
                    
                