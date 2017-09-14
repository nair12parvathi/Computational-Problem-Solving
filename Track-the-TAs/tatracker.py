"""
file: tatracker.py
language: python3
author:zjb (Used the code uploaded in mycourses for heap implementaton.)
author: pvc8661@rit.edu by  Pallavi Chandanshive
author: pan7447@rit.edu by  Parvathi Nair
description: Implementation of a day in the lab where TAs are helping out students

"""
"""
This class used to implement linkable node
"""
class Node:
    __slots__="index","name","confusion_level","next","previous"

    def __init__(self,name=None,confusion_level=None,next=None,previous=None,index=0):
        self.index=index
        self.name=name
        self.confusion_level=confusion_level
        self.next = next
        self.previous = previous
"""
This class used to implement queue, which is the datat structure for Oliver
"""
class Queue:
    __slots__ = "front","rear"
    def __init__(self):
        self.front=None
        self.rear=None
    """
    This method does enqueue operation
    param newNode: node to be enqueued
    precondition: queue in initial condition
    postcondition: queue after new node is added
    """
    def enque(self, newNode):
        #newNode = Node(index, Nlist[0],Nlist[1])
        if self.front == None:
            self.front = newNode
        else:
            self.rear.next = newNode
            newNode.previous = self.rear
        self.rear = newNode

    """
    This method does dequeue operation
    precondition: queue in initial condition
    postcondition: queue after 1st node is deleted
    return: Node that is dequeued
    """
    def dequeue(self):
        Node=self.front
        if self.front == None:
            print("Queue is empty")
            return None
        else:
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.previous = None
            return Node

    """
    This method checks if the queue is empty
    """
    def isEmpty(self):
        return self.front==None

    """
    This method does deletion operation
    param newNode: node to be deleted
    precondition: queue in initial condition
    postcondition: queue after node is deleted
    """
    def delete(self,newNode):
        if self.front==newNode:
            self.dequeue()
        else:
            if newNode.next==None:
                self.rear=newNode.previous
                newNode.previous.next=None
            else:
                newNode.previous.next=newNode.next
                newNode.next.previous=newNode.previous



"""
This class is the implementation of heap which is the data structure for Colleen
"""
class Heap(object):
    '''
    Heap that orders by a given comparison function, default to less-than.
    '''
    __slots__ = ('data', 'size')

    def __init__(self):
        self.data = []
        self.size = 0

    """
        This method does comparison
        param x and y: Nodes to be compared
        """
    def lessfn(self,x,y):
        return x.confusion_level > y.confusion_level
    """
    Helper function to compute the parent location of an index
    param loc: Index in the heap
    return: Index of parent
    """
    def __parent(self, loc):
        return (loc - 1) // 2

    """
    Starts from the given location and moves the item at that spot
    as far up the heap as necessary
    param loc: Place to start bubbling from
    """
    def __bubbleUp(self, loc):
        while loc > 0 and \
                self.lessfn(self.data[loc], self.data[self.__parent(loc)]):
            self.data[loc], self.data[self.__parent(loc)] = \
                self.data[self.__parent(loc)], self.data[loc]
            self.data[loc].index=loc
            self.data[self.__parent(loc)].index=self.__parent(loc)
            loc = self.__parent(loc)
    """
    Starts from the given location and moves the item at that spot
    as far down the heap as necessary
    param loc: Place to start bubbling from
    """
    def __bubbleDown(self, loc):
        swapLoc = self.__smallest(loc)
        while swapLoc != loc:
            self.data[loc], self.data[swapLoc] = \
                self.data[swapLoc], self.data[loc]
            self.data[loc].index = loc
            self.data[swapLoc].index = swapLoc
            loc = swapLoc
            swapLoc = self.__smallest(loc)
    """
    Finds the "smallest" value of loc and loc's two children.
    Correctly handles end-of-heap issues.
    param loc: Index
    return: index of smallest value
    """
    def __smallest(self, loc):
        ch1 = loc * 2 + 1
        ch2 = loc * 2 + 2
        if ch1 >= self.size:
            return loc
        if ch2 >= self.size:
            if self.lessfn(self.data[loc], self.data[ch1]):
                return loc
            else:
                return ch1
        # now consider all 3
        if self.lessfn(self.data[ch1], self.data[ch2]):
            if self.lessfn(self.data[loc], self.data[ch1]):
                return loc
            else:
                return ch1
        else:
            if self.lessfn(self.data[loc], self.data[ch2]):
                return loc
            else:
                return ch2
    """
    Inserts an item into the heap.
    param item: Item to be inserted
    """
    def insert(self, newNode):
        self.data.append(newNode)
        self.size += 1
        self.__bubbleUp(self.size - 1)
    """
    Removes and returns top of the heap
    return: Item on top of the heap
    """
    def pop(self):
        if self.size == 0:
            return None
        else:
            retjob = self.data[0]
            self.size -= 1
            # if we are popping the only element, assignment will fail,
            # but bubbling is unnecessary, so:
            if self.size > 0:
                self.data[0] = self.data.pop(self.size)
                self.__bubbleDown(0)
            return retjob
    """
    Defining the "length" of a data structure also allows it to be
    used as a boolean value!
    return: size of heap
    """
    def __len__(self):
        return self.size
    """
    Deletion of the node
    """
    def delete(self, Node):
        if Node.index == 0:
            self.pop()
        elif Node.index==self.size-1:
            self.size -= 1
            self.data.pop(self.size)
        else:
            self.size -= 1
            self.data[Node.index] = self.data.pop(self.size)
            self.__bubbleDown(Node.index)

"""
Displays message
"""
def displayhelp(showList):
    result= "" + showList[0] + " is looking for help !"
    print(result)
"""
Displays message
"""
def displayHelping(showList,Node):
    result="" + showList[0] + " helping " + Node.name
    print(result)
"""
Displays message
"""
def displayLeft(q):
    current=q.front
    if current==None:
        print("Students left unhelped:\n 0")
    else:
        result="Students left unhelped: \n"
        while current != None:
            result += ""+current.name+"\n"
            current=current.next

        print(result)

def main():
    q=Queue()
    h=Heap()
    mylist=[]
    filename = input("Enter the filename ")
    with open(filename) as f:
        for line in f:
            line = line.rstrip("\n")
            mylist=(line.split(" "))
            if mylist[1].isdigit()==True:
                displayhelp(mylist)
                newNode=Node(mylist[0],int(mylist[1]))
                q.enque(newNode)
                h.insert(newNode)
            else:

                if mylist[0]=="Colleen":
                    newNode=h.pop()
                    if newNode != None:
                        q.delete(newNode)
                        displayHelping(mylist, newNode)
                    else:
                        print(""+mylist[0]+" waiting")

                else:
                    newNode=q.dequeue()
                    if newNode != None:
                        h.delete(newNode)
                        displayHelping(mylist, newNode)
                    else:
                        print("" + mylist[0] + " waiting")


    displayLeft(q)

if __name__ == '__main__':
    main()


"""
Text file:

Bob 3
Dan 6
Melissa 4
Oliver ready
Colleen ready
Nate 1
Gertrude 3
Colleen ready
Oliver ready

#################################################################################################################################

Test Cases:

1. If last element in heap is to be popped. (Melissa 4 is the first line in the text file)
2. If any of the TA becomes ready again. (Example: put Oliver ready as the last line in the text file)
3. If any of the TA is ready before any student is looking for help (Example: put Oliver ready as the first line in the text file)
4. If any of the student looking for help has name same as the name of any TAs.(Example: put Oliver 4 as the first line)
5. If only one of the TAs is helping students(Example: Replace Colleen with Oliver in the text file)

###################################################################################################################################

Expected outcome:

1.
Enter the filename tatracker.txt
Melissa is looking for help !
Bob is looking for help !
Dan is looking for help !
Oliver helping Melissa
Colleen helping Dan
Nate is looking for help !
Gertrude is looking for help !
Colleen helping Bob
Oliver helping Nate
Students left unhelped:
Gertrude

2.
Enter the filename tatracker.txt
Melissa is looking for help !
Bob is looking for help !
Dan is looking for help !
Oliver helping Melissa
Colleen helping Dan
Nate is looking for help !
Gertrude is looking for help !
Colleen helping Bob
Oliver helping Nate
Oliver helping Gertrude
Students left unhelped:
 0

3.
Enter the filename tatracker.txt
Queue is empty
Oliver waiting
Melissa is looking for help !
Bob is looking for help !
Dan is looking for help !
Oliver helping Melissa
Colleen helping Dan
Nate is looking for help !
Gertrude is looking for help !
Colleen helping Bob
Oliver helping Nate
Students left unhelped:
Gertrude

4.
Enter the filename tatracker.txt
Oliver is looking for help !
Bob is looking for help !
Dan is looking for help !
Oliver helping Oliver
Colleen helping Dan
Nate is looking for help !
Gertrude is looking for help !
Colleen helping Bob
Oliver helping Nate
Students left unhelped:
Gertrude

5.
Enter the filename tatracker.txt
Melissa is looking for help !
Bob is looking for help !
Dan is looking for help !
Oliver helping Melissa
Oliver helping Bob
Nate is looking for help !
Gertrude is looking for help !
Oliver helping Dan
Oliver helping Nate
Students left unhelped:
Gertrude

"""