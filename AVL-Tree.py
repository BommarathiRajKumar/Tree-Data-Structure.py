""" :-AVL tree is extension of BST tree,  adding some more rules for BST to balance the tree to overome the challenge of
        skewed tree after adding more rules to BST then this tree is known as AVL Tree.
    :-Note:- we have some challenges in BST tree after overcome this challenges by using certain algorithms then only tree can 
        balenced automitically."""
#   CHALLENGES                  ALGORITHM
#------------------------------------------------------
#  RR(Right Right)   _      Right Rotation Algo
#  RL(Right Left)    _      Left Rotation Algo
#  RL(Right Left)    _      Right & Left Rotation Algo
#  LR(Left Right)    _      Left  & Right Rotation Algo



#        Time complexity in big O notation
#-------------------------------------------------------
# Algorith          Average          Worst case
#  Space              O(n)              O(n)
#  Search             O(log n)          O(log n)
#  Insert             O(log n)          O(log n)
#  Delete             O(log n)          O(log n)



#  AVL-Tree(insert function & all cases LL,RR,RL& LR) Code:-
#-----------------------------------------------------------



class AVLTreeNode:
    def __init__(self , data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1
    
    
    
    def getHeight(self , rootNode):
        if not rootNode:
            return 0
        return rootNode.height
    
    
    
    #if getBalance gives -1,0,1 then tree is balanced.
    #if getBalance < -1 & getBalance >1 then tree is inbalenced.
    def getBalance(self , rootNode):
        if not rootNode:
            return 0
        return self.getHeight(rootNode.leftchild) - self.getHeight(rootNode.rightchild)
    
    
    
    def preOrderTraverse(self , rootNode):
        if not rootNode:
            return
        print(rootNode.data)
        self.preOrderTraverse(rootNode.leftchild)
        self.preOrderTraverse(rootNode.rightchild)
        
        
        
    #This function will solve the challenge of RR case:-
    def leftRotation(self , disbalanceNode):
        newRoot = disbalanceNode.rightchild
        disbalanceNode.rightchild = disbalanceNode.rightchild.leftchild
        newRoot.leftchild = disbalanceNode
        disbalanceNode.height = 1+max (self.getHeight(disbalanceNode.leftchild) , self.getHeight(disbalanceNode.rightchild))
        newRoot.height = 1+max (self.getHeight(newRoot.leftchild) , self.getHeight(newRoot.rightchild))
        return newRoot
    
    
    
    #This function will solve the challenge of LL Case:-
    def rightRotation(self , disbalanceNode):
        newRoot = disbalanceNode.leftchild
        disbalanceNode.leftchild = disbalanceNode.leftchild.rightchild
        newRoot.rightchild = disbalanceNode
        disbalanceNode.height =  1+max (self.getHeight(disbalanceNode.leftchild) , self.getHeight(disbalanceNode.rightchild))
        newRoot.height = 1+max (self.getHeight(newRoot.leftchild) , self.getHeight(newRoot.rightchild))
        return newRoot 
    
    
    
    #function for inserting the data:-
    #function for inserting the data:-
    def insertNode(self , rootNode , nodeValue):
        #BST Logic:-
        if not rootNode:
            return AVLTreeNode(nodeValue)
        elif nodeValue < rootNode.data:
            rootNode.leftchild = self.insertNode(rootNode.leftchild,nodeValue)
        else:
            rootNode.rightchild = self.insertNode(rootNode.rightchild, nodeValue)
        
        # property of AVL
        rootNode.height =  1+max (self.getHeight(rootNode.leftchild) , self.getHeight(rootNode.rightchild))
        balance = self.getBalance(rootNode)
        
        
        #if tree is not balance > 1
        
        #LL Case
        if balance > 1 and nodeValue < rootNode.leftchild.data:
            return self.rightRotation(rootNode)
        
        #RR case
        if balance < -1 and nodeValue > rootNode.rightchild.data:
            return self.leftRotation(rootNode)
        
        #LR case
        if balance > 1 and nodeValue > rootNode.leftchild.data:
            rootNode.leftchild = selfleftRotation(rootNode.leftchild)
            return self.rightRotation(rootNode)
        
        #RL case
        if balance < -1 and nodeValue < rootNode.rightchild.data:
            rootNode.rightchild = self.rightRoataion(rootNode.rightchild)
            return self.leftchild(rootNode)
        return rootNode

    
    
#FALLOW THIS STEPS TO USE THE ABOVE CODE:-
#First create the objects by using the above class:-
#rootNode = AVLTreeNode("data1")    (you can take any object name that is your choice).



#After creating the object using that object you can insert the data in to the tree by using the "inserNode()" function in class:-
#rootNode.insertNode(rootNode , "data2")    **Here you have to pass rootNode name and data.
#rootNode.insertNode(rootNode , "data3")



#After inserting the data by using the "preOrderTraverse()" you can print the data to see how the data is arranged in the tree.
#preOrderTraverse(rootNode)     **Here you habe to pass the rootNode name to see the data at that particular rootNode.
