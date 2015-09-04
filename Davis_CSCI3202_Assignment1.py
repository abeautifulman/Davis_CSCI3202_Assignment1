
#Connor Davis
#CSCI 3202 Intro to Artificial Intelligence
#Assignment 1: Data Structures in Python


import queue

#Queue
#First in, first out

class iloveqs():
    def __init__(self):
        self.myQueue = queue.Queue()

    def addItems(self):
        for i in range(10):
            print("Pushing", i)
            self.myQueue.put(i)

    def obliterateItems(self):
        for j in range(10):
            print("Removing item", j, "from queue")
            self.myQueue.get(j)


#Stack

class stack():
    def __init__(self):
        #Empty List for the stack
        self.items = []

    def push(self, value):
        print("Adding", value, "to stack")
        self.items.append(value)

    def stackPop(self):
        #for k in len(self.items):
            #print("Popping item", k)
        return self.items.pop()

    def checkSize(self):
        return len(self.items)


#Binary Tree

class treeNode():
    def __init__(self, Value):
        self.integerKey = Value
        self.leftChild = None
        self.rightChild = None
        self.parent = None

'''
in order to make an Austin node we would do this
Austin = treeNode(20)
print(Austin.integerKey)
'''

class binaryTree():

    #Initialize
    def __init__(self, rootValue):
        self.rootNode = treeNode(rootValue)

        #Keeping track of node values in a list so we can check against them
        self.nodeList = []
        self.nodeList.append(self.rootNode)

    #Printing the Root Node
    def printRoot(self): {
        print(self.rootNode.integerKey)
    }

    #Adding a Node
    def addNode(self, value, parentValue):
        #Loop through nodeList to check if parentValue is present in tree
        success = False

        for node in self.nodeList:
            if success == False:
                if node.integerKey == parentValue:
                    if node.leftChild == None:
                        node.leftChild = treeNode(value)
                        node.leftChild.parent = parentValue
                        self.nodeList.append(node.leftChild)
                        success = True
                    elif node.rightChild == None:
                        node.rightChild = treeNode(value)
                        node.rightChild.parent = parentValue
                        self.nodeList.append(node.rightChild)
                        success = True
                    else:
                        print("Parent has two children, node not added")
                        success = True

        if success == False:
            print("Parent not found")

    def deleteNode(self, value):

        #Attempt 3
        '''
        nodeExists = False

        for zoomba in self.nodeList:
            #Check if node has value we're looking for
            if zoomba.integerKey == value:
                nodeExists = True
                #Check if node has any children
                if zoomba.leftChild is not None: #or zoomba.rightChild is not None:
                    print("Node not deleted, has children")
                #Parent doesn't have children, delete it
                elif zoomba.leftChild is None:
                    print("This node has a no children - time to KILL IT")
                    print(value)
                    for parentzoomba in self.nodeList:
                        #I think it's getting hung up here because some nodes don't have a leftChild value
                        print(parentzoomba.leftChild.integerKey)
                        #if parentzoomba.leftChild.integerKey == value:
                         #   print("This node has a left child who we need to remove")


        if nodeExists == False:
            print("Node not found")
        '''


        #Attempt 2
        '''
        #Check if node exists
        nodeExists = False

        for node in self.nodeList:
            if node.integerKey == value:
                nodeExists = True

            if nodeExists == True:

            #Check if existing node has any chilren
                for node in self.nodeList:
                    if node.leftChild is None and node.rightChild is None:
                        #We want to delete this node
                        #First remove it as the child of it's parent
                        for item in self.nodeList:
                            if item.leftChild == value:
                                item.leftChild = None
                            if item.rightChild == value:
                                item.rightChild = None
                        #Now delete the node from the list
                            self.nodeList.pop()

        if nodeExists == False:
            print("Node not found")
        '''



        #Attempt 1
        '''
        #Look for nodes that have no children
        for node in self.nodeList:
            if node.leftChild == None and node.rightChild == None:

                #If a node does not have children, re-loop through the list to find
                for node in self.nodeList:
                    if node.leftChild == value:
                        node.leftChild = None
                    if node.rightChild == value:
                        node.rightChild == None
                    self.nodeList.pop()
        '''



    #PrintTree

    def printTree(self):

        for item in self.nodeList:
            self.leftValue = None
            self.rightValue = None

            if item.leftChild is not None:
                self.leftValue = item.leftChild.integerKey

            if item.rightChild is not None:
                self.rightValue = item.rightChild.integerKey

            print("Node value:", item.integerKey, "Left Child:", self.leftValue, "Right Child:", self.rightValue, "Parent:", item.parent)



#TESTING CODE


#TESTING THE QUEUE
print("Testing the queue")
vegeta = iloveqs()
vegeta.addItems()
vegeta.obliterateItems()



#TESTING THE STACK
print("Testing the stack, adding 10 integers")
gooberDust = stack()
for q in range(10):
    gooberDust.push(q)

print("Popping items off stack")
while gooberDust.checkSize() != 0:
    print(gooberDust.stackPop())

#TESTING THE TREE

print("Instantiating Binary Tree")
testTree = binaryTree(50)

print("Adding 10 nodes to the tree")
testTree.addNode(15, 50)
testTree.addNode(30, 50)
testTree.addNode(2, 15)
testTree.addNode(8, 2)
testTree.addNode(20, 15)
testTree.addNode(7, 30)
testTree.addNode(99, 30)
testTree.addNode(25, 20)
testTree.addNode(666, 99)


#Add a node that won't work because the parent value isn't there
testTree.addNode(1, 100000)

#Add a node that won't work because the parent already has two children
testTree.addNode(500, 15)
testTree.printTree()

#Unneeded print code
'''
for item in testTree.nodeList:
    print(item.integerKey)
'''

#Delete a Node

#Try deleting a node that has children
print("Trying to delete a node that has children")
testTree.deleteNode(2)

#Try deleting a node that doens't exist
print("Trying to delete a node that doesn't exist")
testTree.deleteNode(99999999999)

#Delete 2 nodes
print("Removing 2 nodes from the tree")
testTree.deleteNode(666)

print("Printing tree again")
testTree.printTree()



#print("Printing Tree")

#add 10 integers as nodes to the tree
