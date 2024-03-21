import sys

input = lambda: sys.stdin.readline()

def preorder(tree, node):
  if node == ".":
    return
  print(node, end="")
  preorder(tree, tree[node][0])
  preorder(tree, tree[node][1])

def inorder(tree, node):
  if node == ".":
    return
  inorder(tree, tree[node][0])
  print(node, end="")
  inorder(tree, tree[node][1])

def postorder(tree, node):
  if node == ".":
    return
  postorder(tree, tree[node][0])
  postorder(tree, tree[node][1])
  print(node, end="")

N = int(input())
TREE = {}
for _ in range(N):
  PARENT, LEFT_CHILD, RIGHT_CHILD = list(input().split())
  TREE[PARENT] = [LEFT_CHILD, RIGHT_CHILD]
  
preorder(TREE, "A")
print("")  
inorder(TREE, "A")
print("")  
postorder(TREE, "A")
print("")
