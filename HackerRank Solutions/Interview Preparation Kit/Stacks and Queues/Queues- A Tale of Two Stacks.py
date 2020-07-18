class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def peek(self):
        if len(self.stack1) <= 0 and len(self.stack2) <= 0:
            return -1
        if len(self.stack2) <= 0:
            while len(self.stack1) > 0:
                x = self.stack1.pop()
                self.stack2.append(x)
        return self.stack2[-1]
        
    def pop(self):
        if len(self.stack1) <= 0 and len(self.stack2) <= 0:
            return -1
        if len(self.stack2) <= 0:
            while len(self.stack1) > 0:
                x = self.stack1.pop()
                self.stack2.append(x)
        return self.stack2.pop()
        
    def put(self, value):
        self.stack1.append(value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())