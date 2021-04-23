"""
Stack to queue converter.
"""

from arraystack import ArrayStack  # or from linkedstack import LinkedStack
from arrayqueue import ArrayQueue  # or from linkedqueue import LinkedQueue


def stack_to_queue(stack):
    elements = []
    while not stack.isEmpty():
        elements.append(stack.pop())
    for el in reversed(elements):
        stack.push(el)
    # for i in range(-1, -(len(elements) + 1), -1):
    #     stack.push(elements[i])
    queue = ArrayQueue(elements)
    return queue


if __name__ == "__main__":
    stack = ArrayStack()
    for i in range(10):
        stack.add(i)
    queue = stack_to_queue(stack)
    print(queue)
    print(stack)
    print(stack.pop())
    print(queue.pop())
    stack.add(11)
    queue.add(11)
    print(queue)
    print(stack)
