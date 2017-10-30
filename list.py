# coding: utf-8
# @author zhenzong
# @date Sunday, 29 October 2017.


class ListNode(object):

    next = None

    data = None

    def __init__(self, **kwargs):
        if kwargs:
            self.data = dict()
            self.data.update(kwargs)

    def __getattr__(self, name):
        return self.data[name]

    def __setattr__(self, name, value):
        if name in dir(self):
            self.__dict__[name] = value
        else:
            self.data[name] = value

    def __str__(self):
        return str(self.data)

    __repr__ = __str__


class List(object):

    root = ListNode()

    def reverse(self):
        node, new_node = self.root.next, None
        while node is not None:
            temp_node = node.next
            node.next = new_node
            new_node = node
            node = temp_node
        self.root.next = new_node

    def step_reverse(self, step):
        traversal, tail = self.root.next, self.root
        while traversal is not None:
            index, new_node, new_tail = 0, None, traversal
            while index < step and traversal is not None:
                temp_node = traversal.next
                traversal.next = new_node
                new_node = traversal
                traversal = temp_node
                index += 1
            tail.next = new_node
            tail = new_tail

    def __str__(self):
        temp_node = self.root.next
        if not temp_node:
            return ''
        list_str = str(temp_node)
        temp_node = temp_node.next
        while temp_node is not None:
            list_str += ','
            list_str += str(temp_node)
            temp_node = temp_node.next
        return list_str

    __repr__ = __str__

    __invert__ = reverse


if __name__ == '__main__':
    list = List()
    node = list.root
    for i in range(10):
        node.next = ListNode(key=i)
        node = node.next
    print list
    list.step_reverse(2)
    print list
