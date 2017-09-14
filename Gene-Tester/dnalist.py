"""
file: DNALIst.py
language: python3
author: pvc8661@rit.edu by  Pallavi Chandanshive
author: pan7447@rit.edu by  Paravthi Nair
description: Implementation of LinkedList
"""


"""
This class is an implementation of node
"""
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
""" This class provides Linkedlist implementation using DNA concept
"""
class DNA_List:
    """
        This constuctor sets the value of head and tail to None
        precondition: head and tail =Null
        postcondition: head and tail values are set to null
        :param head: represents the head of LinkList
        :param tail: represents the end of LinkList
    """
    def __init__(self,Gene=''):

        if Gene == '':
            self.head = None
            self.tail = None
        else:
            self.head = None
            self.tail = None
            for i in range(len(Gene)):
                if self.head == None:
                    if Gene[i] != 'A' and Gene[i] != 'C' and Gene[i] != 'G' and Gene[i] != 'T':
                       print("invalid characters.List can't be created")
                       return
                    else:
                       self.head = Node(Gene[i], None)
                       self.tail = self.head
                else:
                    current = self.tail
                    if (current.next == None):
                        if Gene[i] != 'A' and Gene[i] != 'C' and Gene[i] != 'G' and Gene[i] != 'T':
                            print("invalid characters.List can't be created")
                            return
                        current.next = Node(Gene[i], None)
                        self.tail = current.next
    """
        This methods appends the linkedlist with the char paased to  the method at the end of the list
        precondition:   LinkedList is created
        postcondition:  char gets append to the list
        :param head:    represents the head of LinkList
        :param tail:    represents the end of LinkList
        :param current: points to the current value of the linkedlist
    """

    def append(self,char):
        if (isinstance(char, int)):
            print("Error")
        elif (isinstance(char, float)):
            print("Error")
        elif (char==''):
            return
        elif (char!='A' and char!='C' and char!='G' and char!='T'):
            print("invalid character")
        else:
            if len(char)==1:
                if self.head==None:
                    self.head=Node(char,None)
                    self.tail =self.head
                else:
                    current=self.tail
                    current.next=Node(char,None)
                    self.tail=current.next
            else:
                print("Error")

    """
        This methods joins the linkedlist with the other linkedlist paased to  the method
        precondition:   LinkedList is created and the other linkedlist is passed to the method
        postcondition:  linkedlist gets joined to the previous list
        :param head:    represents the head of LinkList
        :param tail:    represents the end of LinkList
        :param current: points to the current value of the linkedlist
    """

    def join(self,other):
        if self.head==None:
            self.head=other.head
            self.tail =other.tail
        else:
            self.tail.next=other.head

    """
            This methods adds the next list at the index specified
            precondition:   LinkedList is created
            postcondition:  Other linked list is added to the the current list at the specified position
            :param head:    represents the head of LinkList
            :param tail:    represents the end of LinkList
            :param current: points to the current value of the linkedlist
        """
    def splice(self,ind,other):
        if other.head==None and other.tail==None:
            print("Second list is empty. So nothing changes in first list")
            return
        else:
            if (isinstance(ind, str)):
                print("Error: Index of String type")
            elif (isinstance(ind, float)):
                print("Error: Index of float type")
            else:
                length=self.lengthOfList()
                #print (length)
                if length==0 and self.head==None:
                    self.head=other.head
                elif ind>length-1 or ind<0:
                    print("Index out of range")
                else:
                    current=self.head
                    count=0
                    while(count!=ind):
                        current=current.next
                        count +=1
                        if current.next==None and ind!=count:
                            print('Invalid Index')
                            return
                    other.tail.next=current.next
                    current.next=other.head

    """
        This methods counts the element of linkedlist
        precondition:   LinkedList is created
        postcondition:  counts the total elemnet in the list
        :param head:    represents the head of LinkList
        :param current: points to the current value of the linkedlist
        :param  count : count of elements present in the list
        :
    """

    def lengthOfList(self):
        current=self.head
        count=0
        while(current!=None):
            count += 1
            current = current.next
        return count

    """
        This methods removes the element of linkedlist present at i1 til i2
        precondition:   LinkedList is created
        postcondition:   Elemnet of th elist are removed from  the specified i1 till i2
        :param head:    represents the head of LinkList
        :param tail:    represents the end of LinkList
        :param current: points to the current value of the linkedlist
        :param  i1    : Index position from where the elements have to remove
        :param  i2    : Index position till where the elements have to remove
    """

    def snip(self,i1,i2):

        if (isinstance(i1, str)):
            print("Error: Index of String type")
        elif (isinstance(i1, float)):
            print("Error: Index of float type")
        elif (isinstance(i2, str)):
            print("Error: Index of String type")
        elif (isinstance(i2, float)):
            print("Error: Index of float type")
        elif i1 < 0 or i2 < 0:
            print("Invalid index: negative value")
        else:
            current1=self.head
            current2=self.head
            count=0
            if i1>i2:
                print('Invalid Index')
                return
            while (count!=i2):

                if count==i1 and count==0:
                    current1 = None
                elif count+ 1==i1:
                    current1=current2
                current2 = current2.next
                count += 1

                if current2.next==None and i1!=i2:
                    if i2==count:
                        #current2=current2.next
                        current1 = current2
                        self.head=current1
                        return
                    elif i2!=count or i1!=count:
                        print('Invalid Index')
                        return
            if i1==i2==0:
                return
            if current1 ==None:
                current1=current2
                self.head=current2
            elif current1.next==current2:
                return
                 #current1.next=current2.next
            else:
                 current1.next=current2

    """
        This methods replaces the elemnet of  linkedlist with the string paased to  the method
        precondition:   LinkedList is created
        postcondition:  linkedlist gets relaced with the string spcified
        :param head:    represents the head of LinkList
        :param tail:    represents the end of LinkList
        :param current: points to the current value of the current linkedlist
        :param other:   points to the current value of the other linkedlist
        :param temp1:   traverse through LinkedList
        :param temp2:   traverse through LinkedList
        :param startpointer:   traverse through LinkedList
        :param endpointer:   traverse through LinkedList
        :param repstr:         string which is to be replaced
    """

    def replace(self,repstr,other):
        if (isinstance(repstr, int)):
            print("Error: expected string")
        elif(isinstance(repstr, float)):
            print("Error: expected string")
        else:
            if other.head==None and other.tail==None:
                return
            elif self.head==None and self.tail==None:
                print("List is empty so string cant be found to replace")
            else:
                temp1 = self.head
                temp2 = self.head

                startpointer = self.head
                endpointer = self.head
                while (temp1 != None):
                    if temp2.data == repstr[0]:
                        result = ""
                        for i in range(len(repstr)):
                            result = result + temp2.data
                            endpointer = temp2
                            temp2 = temp2.next

                        if repstr == result:
                            if temp1 == self.head:
                                self.head = other.head
                                other.tail.next = endpointer.next

                            else:
                                startpointer.next = other.head
                                other.tail.next = endpointer.next

                    startpointer = temp1
                    temp1 = temp1.next
                    temp2 = temp1
                return ("No string found.Can't replace")

    """
        This methods copy 's the linkedlist
        precondition:   LinkedList is created
        postcondition:  Copy of the created LinkedList
        :param current: points to the current value of the current linkedlist
        param DNAcopy:  copy of the LinkedList
    """

    def copy(self):
        DNAcopy=DNA_List('')
        current=self.head
        while(current!=None):
            DNAcopy.append(current.data)
            current=current.next
        print(DNAcopy.__str__())

    """
        This methods converts the elments of LinkedList into a String
        precondition:   LinkedList is created
        postcondition:  Elements are conversted into single string
        :param current: points to the current value of the current linkedlist
        :param s:       represents elemnets of LinkList
    """
    def __str__(self):

        current = self.head
        if current==None:
            print("list is empty")
        else:
            s=""
            while (current != None):
                s=s+current.data
                current=current.next
            return(s)


