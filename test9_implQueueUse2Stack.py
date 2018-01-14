"""
File: test9_implQueueUse2Stack.py
Author: heguilong
Email: hgleagle@gmail.com
Github: https://github.com/hgleagle
Description:用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def is_empty(self):
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    for i in range(10):
        s.push(i)
    while not s.is_empty():
        print(s.pop())
