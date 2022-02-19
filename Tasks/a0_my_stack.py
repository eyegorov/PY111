"""
My little Stack
"""
from typing import Any


class Stack:
    def __init__(self):
        self.__my_stack = []  # todo для стека можно использовать python list

    def push(self, elem: Any) -> None:
        """
        Operation that add element to stack

        :param elem: element to be pushed
        :return: Nothing
        """
        self.__my_stack.append(elem)  # 0(1)
        return None

    def pop(self) -> Any:
        """
        Pop element from the top of the stack. If not elements - should return None.

        :return: popped element
        """
        if not len(self.__my_stack):
            return None

        return self.__my_stack.pop()  # O(1)

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the stack without popping it.

        :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
        :return: peeked element or None if no element in this place
        """
        if ind >= len(self.__my_stack):
            return None
        return self.__my_stack[-(ind + 1)]  # O(1)

    def clear(self) -> None:
        """
        Clear my stack

        :return: None
        """
        self.__my_stack.clear() # O(1)
        return None
