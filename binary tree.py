#binary search tree
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BT:
    def __init__(self, e):
        self.root = e        
