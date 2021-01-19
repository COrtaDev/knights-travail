class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if node not in self.children:
            self._children.append(node)
            node.parent = self

    def remove_child(self, node):
        if node in self.children:
            self.children.remove(node)
            node.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if self._parent == node:
            return
        if self._parent != None:
            self._parent.remove_child(self)
        if self._parent != None:
            self._parent.add_child(self)

    def depth_search(self, value):
        if self.value == value:
            return self
        for i in range(len(self.children)):
            child = self.children[i]
            result = child.depth_search(value)
            if result != None:
                return result


node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
node3.parent = node2

print(node1.children)
print(node2.children)
