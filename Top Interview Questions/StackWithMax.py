class StackWithMax:
    def __init__(self):
        self.mainStack = []
        self.trackStack = [] # max element 를 추적하기 위한 stack 공간

    def push(self, x):
        self.mainStack.append(x) # 일반 스택에는 그냥 위로 쌓기만 하면 됨

        if (len(self.mainStack) == 1): # 최초의 원소인 경우 무조건 max 값이 됨.
            self.trackStack.append(x)
            return
        if (x > self.trackStack[-1]): # 현재 원소와 max 값을 비교하여 더 큰 값을 top 에 두기, 그것이 아니라면 append 하지 않음
            self.trackStack.append(x)
        else:
            self.trackStack.append(self.trackStack[-1])

    def getMax(self):
        return self.trackStack[-1]

    def pop(self):
        self.mainStack.pop()
        self.trackStack.pop()

if __name__ == '__main__':
    stack =StackWithMax()
    stack.push(20)
    stack.push(10)
    print(stack.getMax())
    s.push(50)
    print(stack.getMax())

'''
Reference 

https://www.geeksforgeeks.org/tracking-current-maximum-element-in-a-stack/
'''