class Node:
 def __init__(self, data):
  self.data = data
  self.right = None
  self.left = None
  self.parent = None

class BinarySearchTree:
 def __init__(self):
  self.root = None

 def minimum(self, x):
  while x.left != None:
    x = x.left
  return x

 def insert(self, n):                                              #Insertion
  y = None
  temp = self.root
  while temp != None:
    y = temp
    if n.data < temp.data:
      temp = temp.left
    else:
      temp = temp.right

  n.parent = y

  if y == None: #newly added node is root
    self.root = n
  elif n.data < y.data:
    y.left = n
  else:
    y.right = n

 def transplant(self, u, v):                                        #Transplant- Used in Deletion to prevent Disconnection of a branch if the node in between branch is deleted
  if u.parent == None:
    self.root = v
  elif u == u.parent.left:
    u.parent.left = v
  else:
    u.parent.right = v

  if v != None:
    v.parent = u.parent

 def delete(self, z):                                               #Deletion
  if z.left == None:
    self.transplant(z, z.right)

  elif z.right == None:
    self.transplant(z, z.left)

  else:
    y = self.minimum(z.right) #minimum element in right subtree
    if y.parent != z:
      self.transplant(y, y.right)
      y.right = z.right
      y.right.parent = y

    self.transplant(z, y)
    y.left = z.left
    y.left.parent = y

 def inorder(self, n):
  if n != None:
    self.inorder(n.left)
    print(n.data)
    self.inorder(n.right)

if __name__ == '__main__':
 t = BinarySearchTree()

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(100)
e = Node(90)
f = Node(40)
g = Node(50)
h = Node(60)
i = Node(70)
j = Node(80)
k = Node(150)
l = Node(110)
m = Node(120)

t.insert(a)
t.insert(b)
t.insert(c)
t.insert(d)
t.insert(e)
t.insert(f)
t.insert(g)
t.insert(h)
t.insert(i)
t.insert(j)
t.insert(k)
t.insert(l)
t.insert(m)

t.delete(a)
t.delete(m)

t.inorder(t.root)

#   Output
#   20
#   30
#   40
#   50
#   60
#   70
#   80
#   90
#   100
#   110
#   150
