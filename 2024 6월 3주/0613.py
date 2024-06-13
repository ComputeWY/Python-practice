class ArrayBaseList :
    def __init__(self):
        self.list = []
        self.count = 0
        
    def add(self,data):
        self.list.append(data)
        self.count += 1
        
    def search(self, data):
        return [index for index, stored in enumerate(self, list) if stored == data]
    
    def get(self, index):
        if 0 <= index < self.count:
            return self.list[index]
        else:
            raise IndexError
    
    def pop(self):
        val = self.list[self.count -1]
        self.remove(self.count - 1)
        
        return val
    
    def remove(self, index):
        for index in range(index, self.count -1):
            self.list[index] = self.list[index + 1]
            
    
    def display(self):
        for index in range(self.count):
            print(str(self.list[index]) + '', end = "")
            
    
    if __name__ == '__main' :
        
        list = ArrayBaseList()
        
        list.add(10), list.add(20)
        list.add(30), list.add(40)
        list.add(50), list.add(60)
        
        
        print('Add Data')
        list.display()
        print()
        
        print('pop :' + str(list.pop())) # pop : 60
        
    
            