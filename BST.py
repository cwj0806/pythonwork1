class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None
    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
    def find(self, key):
        return self._find_value(self.root, key)
    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted
    def _delete_value(self, node, key):
        if node is None:
            return node, False
        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                # replace the node to the leftmost of node.right
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                    child.left = node.left
                    if parent != node:
                        parent.left = child.right
                        child.right = node.right
                        node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted



class Course:    # 수업 
    def __init__(self):
        a=1 

    def register(self, stno, rest):        # 수강 신청
        studic[stno]=rest
    
    def Modify(self,stno,rest):
        stidic[stno]=rest
        
    def withdraw(self,stno):      # 수강 취소        
        del studic[stno]
        
    def Printone(self,stno):   #입력받은 학번을 가진 학생 정보 출력
        print(stno, studic[stno])
    def Printall(self):  #지금까지 입력받은 학생들 학번 오름차순으로 출력
        a=1
studic={}
C=Course()

N=Node(0)

BST=BinarySearchTree()

while True:
    u=input().split()

    if u[0]=="N":
        if BST.find(int(u[1]))==False:
            C.register(int(u[1]),u[2:])
            N=Node(int(u[1]))
            BST.insert(N)
        else:
            print("error1")
    elif u[0]=="G":
        if BST.find==False:
            C.Modify(int(u[1]),u[2:])
        else:
            print("error2")
    elif u[0]=="C":
        if BST.find==False:
            C.withdraw(int(u[1]))
            BST.delete(int(u[1]))
        else:
            print("error2")
    elif u[0]=="R":
        if BST.find==False:
            C.Printone(int(u[1]))
    elif u[0]=="D":
        a=1
    elif u[0]=="P":
        a=2
    elif u[0]=="Q":
        break
            
            
        

        
        
        

    
