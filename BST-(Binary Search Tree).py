#conditions for BST: leftchild data <= rootNode data & rightchild data > rootNode data.
#when we use inordertraversal on BST it will give the sorted data.

class BST:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        
        
    def insert(self,rootNode,value):
        if rootNode.data == None:
            rootNode.data = value
        elif value <= rootNode.data:
            if rootNode.leftchild == None:
                rootNode.leftchild = BST(value)
            else:
                self.insert(rootNode.leftchild, value)
        else:
            if rootNode.rightchild == None:
                rootNode.rightchild = BST(value)
            else:
                self.insert(rootNode.rightchild, value)
            
    def sortdata(self,rootNode):
        if not rootNode:
            return
        self.sortdata(rootNode.leftchild)
        print(rootNode.data)
        self.sortdata(rootNode.rightchild)
        
  

   #time : o(h) == o(Log n)
   #space : stack memory: o(h) == o(log n)
    
    
   
    def searchBst(self, rootNode, searchItem):
            
        SearchItem = searchItem
                    
            if rootNode.data == searchItem:
                print("data found at root Node:- {}: best case O(1)".format(SearchItem))
                
                
                

            elif searchItem <= rootNode.data:
                if rootNode.leftchild == None:
                        return print("sorry searchItem not availabe in the Data Base")
  
                if rootNode.leftchild.data == searchItem:
                    print("found data at left:- {}".format(SearchItem))
                else:
                    self.searchBst( rootNode.leftchild, searchItem )
                    

            elif searchItem > rootNode.data:
                
                if rootNode.rightchild == None:
                    return print("sorry searchIteam not availabe in the Data Base")

                elif rootNode.rightchild.data == searchItem:
                    print("found data at right:- {}". format(SearchItem))
                else:
                    self.searchBst( rootNode.rightchild, searchItem )
                    
                    
                    
                
                
                
#FALLOW THIS STEPS TO USE THE ABOVE CODE:-

#First create the object by using the above class:-
#mytree = BST(None)   (object name can be your choice&create an empty object by passing None keyword in python).

#After creating the object insert the data by using <insert() function> which is avaolable in class.
#mytree.insert(mytree,10)
#mytree.insert(mytree,15)
#mytree.insert(mytree,20)


#After inserting the data if you want to search particular data use the <searchBst() function> which is available in class.
#mytree.searchBst(mytree,15)

#if you want to see the data in sorted use the <sortdata() function>
#mytree.sortdata(mytree)
