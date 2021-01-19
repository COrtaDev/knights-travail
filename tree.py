class Node:
    # __slots__ = [_value, _parent, _children]

    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    def add_child(self, node):
        self._children.append(node)
        if node not in self._children:
            node._parent = self

    def remove_child(self, node):
        self._children.remove(node)
        node._parent = None

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self):
        self.add_child(self)
