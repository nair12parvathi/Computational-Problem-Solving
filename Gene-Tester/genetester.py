"""
file: DNALIst.py
language: python3
author: pvc8661@rit.edu by  Pallavi Chandanshive
author: pan7447@rit.edu by  Paravthi Nair
description: Implementation of LinkedList
"""

import dnalist

""" This class consiste of all the test cases
"""
class genetester:

     def init_tester(self):
         """
            Testing the  constuctor of DNA_List class
            precondition: LinkedList is created
            postcondition: hLinkedlist is crated with teh avlues passed in the constructor

         """
         DNA1 = dnalist
         print('Testing the init tester....')
         print('Testing Passing Empty String')
         t = DNA1.DNA_List("")
         print(t.__str__())
         print('Passing String')
         t = DNA1.DNA_List("ACG")
         print(t.__str__())
         print("Passing invalid characters")
         t= DNA1.DNA_List("AABT")


     def append_tester(self):
         """
            Testing the  append method of DNA_List class
            precondition:LinkedList is created
            postcondition: various dff arguments are tetested for appending char

         """
         DNA1 = dnalist
         print('Testing the append method....')
         print('Passing Empty string')
         t = DNA1.DNA_List('ACGT')
         t.append('')
         print(t.__str__())
         print('Passing IllegalArguments ')
         t.append(1)
         print('Appending When LinkedList is Null')
         t = DNA1.DNA_List('')
         t.append('A')
         print(t.__str__())
         print('Appending at the end of the list')
         t = DNA1.DNA_List('ACGTT')
         t.append('G')
         print(t.__str__())
         print('Appending more characters')
         t.append('AA')
         print('Appending invalid character')
         t.append('B')


     def join_Tester(self):
         """
             Testing the  join method of DNA_List class
             precondition: LinkedList is created
             postcondition: checks various joining condition

         """
         DNA1 = dnalist
         DNA2 = dnalist
         print('Testing the join method....')
         print('Join When LinkedList is Null')
         t = DNA1.DNA_List('')
         t1 = DNA2.DNA_List('ACGT')
         t.join(t1)
         print(t.__str__())
         print('Joining at the end of the list')
         t = DNA1.DNA_List('ACG')
         t2 = DNA2.DNA_List('TTA')
         t.join(t2)
         print(t.__str__())
         print('Join When both LinkedLists are Null')
         t = DNA1.DNA_List('')
         t1 = DNA2.DNA_List('')
         t.join(t1)
         print(t.__str__())
         print('Join When LinkedList 2 is Null')
         t = DNA1.DNA_List('ACGT')
         t1 = DNA2.DNA_List('')
         t.join(t1)
         print(t.__str__())



     def splice_Tester(self):
         """
            Testing the  splice method of DNA_List class
            precondition: LinkedList is created
            postcondition: checks various splicing condition

         """
         DNA1 = dnalist
         DNA2 = dnalist
         print('Testing the splice method....')
         print('Testing when index is not in range')
         t = DNA1.DNA_List('ACGGT')
         t2 = DNA2.DNA_List('ACGT')
         t.splice(6,t2)
         #print(t.__str__())
         print('splice at last index')
         t = DNA1.DNA_List('GACTT')
         t2 = DNA2.DNA_List('ACGT')
         t.splice(4, t2)
         print(t.__str__())
         print('splice at middle index')
         t = DNA1.DNA_List('ACGTT')
         t2 = DNA2.DNA_List('ACGT')
         t.splice(1, t2)
         print(t.__str__())
         print('Illegal passing of arguments')
         t = DNA1.DNA_List('ACGT')
         t2 = DNA2.DNA_List('GGCCT')
         t.splice('A', t2)
         print('Negative value of arguments')
         t = DNA1.DNA_List('ACGT')
         t2 = DNA2.DNA_List('GACT')
         t.splice(-1, t2)
         print('if the list on which splice is being done is empty ')
         t = DNA1.DNA_List('')
         t2 = DNA2.DNA_List('GACTT')
         t.splice(0, t2)
         print(t.__str__())
         print('if the list with which splice is being done is empty ')
         t = DNA1.DNA_List('ACCAT')
         t2 = DNA2.DNA_List('')
         t.splice(2, t2)
         print(t.__str__())
         print('if other list has invalid characters')
         t = DNA1.DNA_List('ACCAT')
         t2 = DNA2.DNA_List('BAT')
         t.splice(2, t2)

     def snip_Tester(self):
         """
            Testing the  join method of DNA_List class
            precondition: LinkedList is created
            postcondition: checks various joining condition

         """
         DNA1 = dnalist
         DNA2 = dnalist
         print('Testing the snip method....')
         print('Indices in range')
         t = DNA1.DNA_List('ACCTTG')
         t.snip(2, 3)
         print(t.__str__())
         print('Index is not in range')
         t = DNA1.DNA_List('ACCTTG')
         t.snip(8,9)
         #print(t.__str__())
         print('Snip using boundary indices')
         t = DNA1.DNA_List('GACTT')
         t.snip(0,4)
         print(t.__str__())
         print('Illegal passing of arguments')
         t = DNA1.DNA_List('ACCTTG')
         t.snip('A', 4)
         print('Negative value of arguments')
         t = DNA1.DNA_List('ACCTTG')
         t.snip(-1, 4)
         print('i1 is greater than i2 ')
         t = DNA1.DNA_List('ACCTTG')
         t.snip(4, 1)
         print('i1 equal to i2 ')
         t = DNA1.DNA_List('ACCTTG')
         t.snip(2, 2)
         print(t.__str__())
         print('i1 and i2 equals to 0')
         t = DNA1.DNA_List('ACCTTG')
         t.snip(0, 0)
         print(t.__str__())


     def replace_Tester(self):
         """
        Testing the  replace method of DNA_List class
        precondition: LinkedList is created
        postcondition: checks various replacing conditions
        """
         DNA1 = dnalist
         DNA2 = dnalist
         print('Testing the replace method....')
         print('Normal case')
         t = DNA1.DNA_List('ACCTTG')
         t2 = DNA2.DNA_List('AC')
         t.replace('CT',t2)
         print(t.__str__())
         print('Replacing the starting elements')
         t = DNA1.DNA_List('ACCTTG')
         t2 = DNA2.DNA_List('GG')
         t.replace('AC', t2)
         print(t.__str__())
         print('Replacing the ending elements')
         t = DNA1.DNA_List('ACCTTG')
         t2 = DNA2.DNA_List('TT')
         t.replace('TG', t2)
         print(t.__str__())
         print('Replacing the first element')
         t = DNA1.DNA_List('ACCTTG')
         t2 = DNA2.DNA_List('C')
         t.replace('A', t2)
         print(t.__str__())
         print('Replacing the last element')
         t = DNA1.DNA_List('ACCTTG')
         t2 = DNA2.DNA_List('T')
         t.replace('G', t2)
         print(t.__str__())
         print('List 1 is empty')
         t = DNA1.DNA_List('')
         t2 = DNA2.DNA_List('CG')
         t.replace('AC', t2)
         print('List 2 is empty')
         t = DNA1.DNA_List('ACCTTG')
         t2 = DNA2.DNA_List('')
         t.replace('CT', t2)
         print(t.__str__())
         print('String and list length not equal')
         t = DNA1.DNA_List('ACCTTG')
         t2 = DNA2.DNA_List('GGG')
         t.replace('TT', t2)
         print(t.__str__())
         print('Invalid string')
         t = DNA1.DNA_List('ACCTTG')
         t2 = DNA2.DNA_List('TTT')
         t.replace(123, t2)
         print('String not found')
         t = DNA1.DNA_List('CCGTAAT')
         t2 = DNA2.DNA_List('ACGTTT')
         print(t.replace('CT', t2))
         print('Invalid characters in the list 2')
         t = DNA1.DNA_List('ACCTTG')
         t2 = DNA2.DNA_List('PQG')
         t.replace('CC', t2)



     def copy_Tester(self):
         """
         Testing the  replace method of DNA_List class
         precondition: LinkedList is created
         postcondition: checks various copying conditions
         """
         DNA1 = dnalist
         print('Testing the copy method....')
         print('Normal Case')
         t = DNA1.DNA_List('ACCGGT')
         print(t.__str__())
         print("copy of the list is as below:")
         t.copy()
         print('Copy of empty list')
         t = DNA1.DNA_List('')
         print(t.__str__())
         print("copy of the list is as below:")
         t.copy()


     def str_Tester(self):
         """
        Testing the  replace method of DNA_List class
        precondition: LinkedList is created
        postcondition: checks various test cases
                     """
         DNA1 = dnalist
         print('Testing the str method....')
         print('Normal Case')
         t = DNA1.DNA_List('ACCGT')
         s=t.__str__()
         print(s)
         print('Testing if list is empty')
         t = DNA1.DNA_List('')
         s = t.__str__()
         print(s)




g = genetester()

g.init_tester()
g.append_tester()
g.join_Tester()
g.splice_Tester()
g.snip_Tester()
g.replace_Tester()
g.copy_Tester()
g.str_Tester()







