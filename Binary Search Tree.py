class Binary_Search_Tree:
    #Constructor
    
    def __init__(self, data):
        self.data = data
        self.Left_child = None
        self.Right_child = None
        
    """
    Prevention of nodes with duplicate values
    """
        
    def Add_Node(self, data):
        if data == self.data:
            return # node already exist

        """
        If the data we are inserting is Less
        than the value of the current node, then
        data will insert in Left node
        """
        
        if data < self.data:
            if self.Left_child:
                self.Left_child.Add_Node(data)
            else:
                self.Left_child = Binary_Search_Tree(data)
         
            """
            If the data we are inserting is Greater
            than the value of the current node, then
            data will insert in Right node
            """
            
        else:
            if self.Right_child:
                self.Right_child.Add_Node(data)
            else:
                self.Right_child = Binary_Search_Tree(data)


    def Find_Node(self, val):
        
        """
        If current node is equal to 
        data we are finding return true
        """
        
        if self.data == val:
            return True
        
        """
        If current node is lesser than 
        data we are finding we have search 
        in Left child node
        """

        if val < self.data:
            if self.Left_child:
                return self.Left_child.Find_Node(val)
            else:
                return False
        
        """
        If current node is Greater than 
        data we are finding we have search 
        in Right child node
        """

        if val > self.data:
            if self.Right_child:
                return self.Right_child.Find_Node(val)
            else:
                return False
            
    """
    First it will visit Left node then
    it will visit Root node and finally 
    it will visit Right and display a
    list in specific order
    """      
    

    
#List
elements= [1, 2, 4, 4, 3, 3, 3, 6, 5]
    
def Build_Tree(elements):
root = Binary_Search_Tree(elements[0])

    for i in range(1,len(elements)):
        root.Add_Node(elements[i])

    return root

def In_Order_Traversal(self):
    output = []
    if self.Left_child:
        output += self.Left_child.In_Order_Traversal()

    output.append(self.data)

    if self.Right_child:
        output += self.Right_child.In_Order_Traversal()

    return output
  
#Print
print(*output)
