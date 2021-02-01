class Stack:
    def __init__(self):
        self.__stackList = []

    def getlist(self):
    	return self.__stackList

    def push(self, val):
        self.__stackList.append(val)
        return self.__stackList

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def getSum(self):
        Stack.getlist(self)
        return self.__sum, Stack.getlist(self) 

    def push(self, val):
        self.__sum += val
        return Stack.push(self, val)
         

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

obj=Stack()
stackObject = AddingStack()

for i in range(5):
    
    print(stackObject.push(i))
print(stackObject.getSum())


for i in range(5):
    print(stackObject.pop())
print(stackObject.getSum())