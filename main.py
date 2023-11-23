from typing import TypeVar, List

T = TypeVar('T')


class MinHeap:

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = []

    def __len__(self) -> int:
        """
        Length override function
        :return: Length of the  heap
        """
        return len(self.data)

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def empty(self) -> bool:
        """
        Checks if the heap is empty
        :return: True if heap is empty, False otherwise
        """
        return len(self) == 0

    def top(self) -> T:
        """
        Gets the heap root value
        :return: None if heap is empty, the root value otherwise
        """
        if not self.empty():
            return self.data[0]

    def left_child_index(self, index: int) -> int:
        """
        Returns the index of the left child of the node at index
        :param index: index to find the left child index of
        """
        if 2 * index + 1 < len(self.data):
            return 2 * index + 1

    def right_child_index(self, index: int) -> int:
        """
        Returns the index of the right child of the node at index
        :param index: index to find the right child index of
        """

    if 2 * index + 2 < len(self.data):
        return 2 * index + 2

    def parent_index(self, index: int) -> int:
        """
        Returns the index of the parent of the node at index
        :param index: index to find the parent of
        """
        parent = (index - 1) // 2
        if parent >= 0:
            return parent

    def min_child_index(self, index: int) -> int:
        """
        Finds the minimum child at the specified index
        :param index: the index of the node where the minimum child needs to be found
        :return: The minimum child, or None if there are no children
        """
        left_i = self.left_child_index(index)
        right_i = self.right_child_index(index)
        if right_i is not None and left_i is not None:  # FULL  node
            if self.data[left_i] < self.data[right_i]:
                return left_i
            else:
                return right_i
        elif right_i is None and left_i is None:  # node without children
            return
        return left_i  # must be a complete tree right??? it can not have right if it does not have a left...

    def percolate_up(self, index: int) -> None:
        """
        Moves a node up the heap to its desired position
        :param index: The index of the node to be percolated up
        """
        pass

    def percolate_down(self, index: int) -> None:
        """
        Moves a node down the heap to its desired position
        :param index: The index of the node to be percolated down
        """
        pass

    def add(self, key: T) -> None:
        """
        Creates a node and adds a new element to the heap
        :param key: key of the added node
        :param val: value of the new node
        """

    self._data.append(self._Item(key, value))
    self._upheap(len(self.data) - 1)


def remove(self) -> T:
    """
    Removes the smallest element from the heap
    :return: the root of the heap
    """


if self.is_empty():
    raise Empty('Priority queue is empty.')
self._swap(0, len(self._data) - 1)
item = self._data.pop()
self._downheap(0)

return (item._key, item._value)


def build_heap(self):
    pass


def is_min_heap(self):
    pass
