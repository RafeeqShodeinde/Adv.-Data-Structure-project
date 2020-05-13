from cs1graphics import *
import math

################################ CODE START #####################################


class Heap:    
    
    paper = Canvas(500,500,'white','Fibonacci Heaps u digggg' )
    heap_rootlist=[]
    start = Point(0,50)
    displayMinPoint = Point(0,0)
    org_minVal=None
    mini = Text('Min')
    paper.add(mini)

    
    
    def drawNode(self,key):

        nextPosition = self.start + Point(60,0)
        node_rep = Circle(20, nextPosition)

        self.heap_rootlist.append(key)
        nodeValueString = str(key)
        number = Text(nodeValueString)
        number.moveTo(nextPosition.getX(), nextPosition.getY())

        connector = Path(Point(nextPosition.getX()+20, nextPosition.getY()), Point(nextPosition.getX()+40, nextPosition.getY()))

        self.paper.add(node_rep)
        self.paper.add(number)
        self.paper.add(connector)

        self.start = nextPosition

        if (self.org_minVal == None):
            self.displayMinPoint = nextPosition
            self.org_minVal = key
            
        elif (self.org_minVal!=None and key < self.org_minVal):
            self.displayMinPoint = nextPosition
            self.org_minVal = key
            
        elif (self.org_minVal!=None and key == self.org_minVal):
            pass

    def drawChild(self,key):

        nextPosition = self.start + Point(0,60)
        child_rep = Circle(20, nextPosition)

        nodeValueString = str(key)
        number = Text(nodeValueString)
        number.moveTo(nextPosition.getX(), nextPosition.getY())

        connector = Path(Point(nextPosition.getX(), nextPosition.getY()+20), Point(nextPosition.getX(), nextPosition.getY()+40))

        self.paper.add(child_rep)
        self.paper.add(number)
        self.paper.add(connector)


    # pointer to the head and minimum node in the root list
    root_list, min_node = None, None

    def find_min(self):
        self.mini.moveTo(self.displayMinPoint.getX(),self.displayMinPoint.getY()-30)
        return self.min_node

    # maintain total node count in full fibonacci heap
    total_nodes = 0

    # represent a single unit of a F-heap; holds pointer to p[x], child[x], then left and right sibling cus double linked list

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.parent = self.child = self.left = self.right = None
            self.degree = 0
            self.mark = False


    # insert new node into the unordered root list in O(1) time
    # returns the node so that it can be used for decrease_key later

    def insert(self, key, value=None):

        self.drawNode(key)
        
        n = self.Node(key, value)
        n.left = n.right = n
        
        self.merge_with_root_list(n)
        
        if self.min_node is None or n.key < self.min_node.key:
            self.min_node = n
        self.total_nodes += 1
        
        return n

    # merge a node with the doubly linked root list
    def merge_with_root_list(self, node):
        if self.root_list is None:
            self.root_list = node
        else:
            node.right = self.root_list.right
            node.left = self.root_list
            self.root_list.right.left = node
            self.root_list.right = node


    def extract_min(self):
        z = self.min_node
        if z is not None:
            
            self.paper.clear()
            self.heap_rootlist.remove(min(self.heap_rootlist))
            temp=[]
            temp=self.heap_rootlist
            self.heap_rootlist=[]
            self.org_minVal=None
            self.start=Point(0,50)
            self.paper.add(self.mini)

            for x in temp:
                self.drawNode(x)############
                
            
            if z.child is not None:
                # attach child nodes to root list
                children = [x for x in self.iterate(z.child)]
                for i in range(0, len(children)):
                    self.merge_with_root_list(children[i])
                    children[i].parent = None
            self.remove_from_root_list(z)
            # set new min node in heap
            if z == z.right:
                self.min_node = self.root_list = None
            else:
                self.min_node = z.right
                self.consolidate()
            self.total_nodes -= 1
        return z

    # combine root nodes of equal degree to consolidate the heap
    # by creating a list of unordered binomial trees
    def consolidate(self):
        A = [None] * int(math.log(self.total_nodes) * 2)
        nodes = [w for w in self.iterate(self.root_list)]
        for w in range(0, len(nodes)):
            x = nodes[w]
            d = x.degree
            while A[d] != None:
                y = A[d]
                if x.key > y.key:
                    temp = x
                    x, y = y, temp
                self.heap_link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        # find new min node - no need to reconstruct new root list below
        # because root list was iteratively changing as we were moving
        # nodes around in the above loop
        for i in range(0, len(A)):
            if A[i] is not None:
                if A[i].key < self.min_node.key:
                    self.min_node = A[i]


    def remove_from_root_list(self, node):
        if node == self.root_list:
            self.root_list = node.right
        node.left.right = node.right
        node.right.left = node.left


    def iterate(self, head):
        node = stop = head
        flag = False
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right


    def heap_link(self, y, x):
        self.remove_from_root_list(y)
        y.left = y.right = y
        self.merge_with_child_list(x, y)
        x.degree += 1
        y.parent = x
        y.mark = False


    def merge_with_child_list(self, parent, node):
        if parent.child is None:
            parent.child = node
        else:
            node.right = parent.child.right
            node.left = parent.child
            parent.child.right.left = node
            parent.child.right = node


    def remove_from_root_list(self, node):
        if node == self.root_list:
            self.root_list = node.right
        node.left.right = node.right
        node.right.left = node.left


    def remove_from_child_list(self, parent, node):
        if parent.child == parent.child.right:
            parent.child = None
        elif parent.child == node:
            parent.child = node.right
            node.right.parent = parent
        node.left.right = node.right
        node.right.left = node.left
