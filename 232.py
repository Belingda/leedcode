class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stacklst1=[]
        self.stacklst2=[]
    

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stacklst1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stacklst2)>0:
            popnum=self.stacklst2.pop()
            return popnum
        self.changestacklst2()
        try:
            return self.stacklst2.pop()
        except :
            return None  
        
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """

        if len(self.stacklst2)==0:
            if len(self.stacklst1)==0:
                return None
            else:
                self.changestacklst2()
                return self.stacklst2[-1]
        else:
            return self.stacklst2[-1]
        
     

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stacklst1)==0 and len(self.stacklst2)==0

    def changestacklst2(self):
        for i in range(len(self.stacklst1)):
            try:
                v=self.stacklst1.pop()
                self.stacklst2.append(v)
            except:
                pass
           


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
print(param_3)
obj.push(3)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)