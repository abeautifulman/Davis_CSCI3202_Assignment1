
#Connor Davis
#CSCI 3202 Intro to Artificial Intelligence
#Assignment 1: Data Structures in Python


import queue
import random

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

        nodeExists = True
        hasChildren = False

        #Create a copy of the list before we mess it up
        for node in self.nodeList[:]:
            if node.integerKey == value:

            #Check if existing node has any chilren
                if node.leftChild is None and node.rightChild is None:

                #First remove it as the child of it's parent
                    for item in self.nodeList:
                        #Check left child
                        if item.leftChild is not None:
                            if item.leftChild.integerKey == value:
                                item.leftChild = None
                        #Check right child
                        if item.rightChild is not None:
                            if item.rightChild.integerKey == value:
                                item.rightChild = None
                    #Now delete the node from the list
                    self.nodeList.remove(node)
                    nodeExists = True
                else:
                    nodeExists = True
                    hasChildren = True
                    print("Node not deleted, has children")

            else:
                nodeExists = False

        if nodeExists == False and hasChildren == False:
            print("Node not found")


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

#Graph

class testGraph():

    def __init__(self):
        #Create dictionary to store key value pairs
        self.graph = {}

    def addVertex(self, value):
        #Try to add a new node to the graph
        #Check if value already exists in graph
        if value in self.graph:
            print("Vertex already exists")
        #Add value to graph
        #Each value has a list of adjacent nodes
        else:
            self.graph.update({value: []})

    def addEdge(self, value1, value2):
        #Adds an edge between values 1 and 2 unless one of them doesn't exist
        if value1 and value2 in self.graph:
            self.graph[value1].append(value2)
            self.graph[value2].append(value1)
        #If value1 or value2 is not found
        else:
            print("One or more vertices not found")

    def findVertex(self, value):
        #Searches for node with 'value' in graph, then prints adjacent node list if it finds it
        #Check if value exists
        if value in self.graph:
            #Loop through keys
            for boogers in self.graph.keys():
                #If we find a key (node) that we're looking for
                if boogers == value:
                    #Print it, and then all of it's buddies
                    print("Found vertex, displaying adjecent nodes")
                    print(boogers, self.graph[boogers])
        else:
            print("Could not locate vertex of that value")



################
# TESTING CODE #
################

#TESTING THE QUEUE

#Make a new queue
print("Testing the queue")
vegeta = iloveqs()

#push()
print("Adding 10 integers to the queue")
vegeta.addItems()

#pop()
print("Removing 10 integers from the queue")
vegeta.obliterateItems()


#TESTING THE STACK

#Make a new stack
print("Testing the stack")
gooberDust = stack()

#push()
print("Adding 10 integers to the stack")
for q in range(10):
    gooberDust.push(q)

#pop()
print("Popping items off stack")
while gooberDust.checkSize() != 0:
    print(gooberDust.stackPop())


#TESTING THE BINARY TREE

#Make a new binary tree
print("Testing the Binary Tree")
testTree = binaryTree(50)

#TEST ADDING NODES

#Add nodes to the tree
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
print("Try adding a node to a parent value that doesn't exist (100000)")
testTree.addNode(1, 100000)

#Add a node that won't work because the parent already has two children
print("Try adding a node to a parent that already has two children")
testTree.addNode(500, 15)
testTree.printTree()

#TEST DELETING NODES

#Try deleting a node that has children
print("Trying to delete a node that has children (2)")
testTree.deleteNode(2)

#Try deleting a node that doens't exist
print("Trying to delete a node that doesn't exist (99999999999)")
testTree.deleteNode(99999999999)

#Delete 2 nodes
print("Removing 2 nodes from the tree (666, 25)")
testTree.deleteNode(666)
testTree.deleteNode(25)

#Print tree once more now that nodes have been deleted
print("Printing tree again after node removal")
testTree.printTree()

#TESTING THE GRAPH

#Make a new graph
excelsior = testGraph()
intList = []

#Add 10 integers as vertices to the graph
print("Add 10 vertexes to the graph")
for pig in range(10):
    print ("Adding", pig, "vertex to graph")
    intList.append(pig)
    excelsior.addVertex(pig)

#Add a bunch of edges
print("Adding 20 random edges to graph")
for chicken in range(20):
    nodeOne = random.choice(intList)
    nodeTwo = random.choice(intList)
    excelsior.addEdge(nodeOne, nodeTwo)
    print(excelsior.graph)

#Find some vertices
print("Finding 5 vertices")
for cow in range(5):
    nodes = random.choice(intList)
    #print("Looking for node", nodes, "in graph and displaying adjacent nodes")
    excelsior.findVertex(nodes)