#strict binary should contain only two or less the two childrens.
#this code is to show how the tree structure behaves & how all the traverse works.



class TreeNode:
    def __init__(self, d):
        self.data = d
        self.leftchild = None
        self.rightchild = None
    
    
    def preOrderTraverse(self,rootNode):
        if not rootNode:
            return
        print(rootNode.data)
        self.preOrderTraverse(rootNode.leftchild)
        self.preOrderTraverse(rootNode.rightchild)
        
    
    def inOrderTraverse(self,rootNode):
        if not rootNode:
            return
        self.inOrderTraverse(rootNode.leftchild)
        print(rootNode.data)
        self.inOrderTraverse(rootNode.rightchild)
        
    def postOrderTraverse(self,rootNode):
        if not rootNode:
            return
        self.postOrderTraverse(rootNode.leftchild)
        self.postOrderTraverse(rootNode.rightchild)
        print(rootNode.data)
        
    def levelOrderTraverse(self):
        import queue        
        q2 = queue.Queue(maxsize=20)
        q2.put(rootNode)
        while not q2.empty():
            qdata = q2.get()
            print(qdata.data)
            
            if qdata.leftchild is not None:
                q2.put(qdata.leftchild)
            if qdata.rightchild is not None:
                q2.put(qdata.rightchild)




#FALLOW THIS STEPS TO USE THE ABOVE CODE:-
#First create the objects by using the above class:-
#rootNode = TreeNode("data1")    (you can take any object name that is your choice).
#data2 = TreeNode("data2")
#data3 = TreeNode("data3")
#data4 = TreeNode("data4")
#data5 = TreeNode("data5")

#After creating the objects update the objects adress in there particular parents node:-
#rootNode.leftchild = data2
#rootNode.rightchild = data3
#data2.leftchild = data4
#data2.rightchild = data5


#After updating the address we can print the particular node deatils to see there data and what address stored in tha node at left&right child.
#print(rootNode.__dict__)
#print(data2.__dict__)
#print(data3.__dict__)
#print(data4.__dict__)
#print(data5.__dict__)

#To see the behaviour of tree and traverse fuctions use the fuctions which are available in class:-

#DFS(Depth First Search:-
#rootNode.preeOrderTraverse(rootNode)
#rootNode.inOrderTraverse(rootNode)
#rootNode.postOrderTraverse(rootNode)

#BFS(Breath First Search):-
#rootNode.levelOrderTraverse(rootNode)        
    
        
    
