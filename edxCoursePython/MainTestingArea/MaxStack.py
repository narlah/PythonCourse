class Stack:
    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items: return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items: return None
        return self.items[len(self.items) - 1]

    def printItems(self):
        print self.items


class MaxStack:
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def print_items(self):
        self.stack.printItems()

    def get_max(self):
        return self.max_stack.peek()

    def push(self, int_to_push):
        if int_to_push > self.max_stack.peek():
            self.max_stack.push(int_to_push)
        self.stack.push(int_to_push)

    def pop(self):
        val = self.stack.pop()
        if self.max_stack.peek() == val:
            self.max_stack.pop()
        return val


a = MaxStack();
a.push(1)
a.push(2)
a.push(3)
a.push(100)
a.push(5)
a.push(12)
a.print_items()
print a.get_max()
print a.pop()
print a.get_max()
print a.pop()
print a.get_max()
print a.pop()
print a.get_max()
a.print_items()