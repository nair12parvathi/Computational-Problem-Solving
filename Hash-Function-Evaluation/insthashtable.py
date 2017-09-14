
"""
file: inhastable.py
language: python3
author: pvc8661@rit.edu by  Pallavi Chandanshive
author: pan7447@rit.edu by  Parvathi Nair
"""

'''
To calculate the hash function for the file
Based Off of hash.py created and distributed by CSCI-603 faculty.
'''


import re
import math
from  hash import  *

def hash_func(key):
    '''
    Not using Python's built in hash function here since we want to
    have repeatable testing...
    However it is terrible.
    Assumes keys have a len() though...
    :param key: Key to store
    :return: Hash value for that key
    '''
    # if we want to switch to Python's hash function, uncomment this:
    return hash(key)


def hf1(key):
    '''
    calculates the hash function for the key
    :param key: Key of new entry
    '''
    h = 0
    for i in range(len(key)):
        h += ord(key[i]) * (73**i)
    return h

def hf2(key):
    '''
    calculates the hash function for the key
    :param key: Key of new entry
    '''
    h = 0
    for i in range(len(key)):
        h += ((2*ord(key[i])* 97) + 17 )**101
    return h


def max_key(map):
    '''
    computes the max count of  word
    '''

    maxKey = ''
    maxvalue = 0
    for i in map.table:
        if i != None and i != DELETED:
            if i.value > maxvalue:
                maxKey = i.key
                maxvalue = i. value
    print('Word that occurred Maximum times : '+ str(maxKey))
    print('Maximum Value: ' + str(maxvalue)+'\n')

def main():
    h1=Hashmap(hf1, 5)
    h2=Hashmap(hf2, 5)
    h3=Hashmap(hash_func , 5)
    filename = input("Enter a filename (without .txt extension):")
    with open(filename+'.txt') as file:
        mylist =[]
        for line in file:
            line = line.rstrip("\n")
            mylist =re.split('\W+',line)

            for i in range(len(mylist)):

                    x = mylist[i].lower()
                    if x != '':
                        h1.put(x)
                        h2.put(x)
                        h3.put(x)
        printMap(h3)
        max_key(h3)
        printMap(h2)
        max_key(h2)
        printMap(h1)
        max_key(h1)

if __name__ == '__main__':
    main()