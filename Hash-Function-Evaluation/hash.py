__author__ = 'zjb'
from collections import namedtuple

Entry = namedtuple('Entry', ('key', 'value'))

'''
To make sure that the DELETED sentinel does not match
anything we actually want to have in the table, make it
a unique (content-free!) object.
'''
import math

class _delobj: pass


DELETED = Entry(_delobj(), None)


class Hashmap:
    """
       A hashtable has been implemented.

       :slot: (table): A table
       :slot (hash_func): computing  hash function
       :slot (numkeys):
       :slot (cap): capacity for
       :slot (noOfCollisions): total number of collisions
       :slot (noOfProbes): total number of probes
    """
    __slots__ = 'table','hash_func',  'numkeys', 'cap', 'maxload','noOfCollisions','noOfProbes'

    def __init__(self, hash_func, initsz=100, maxload=0.95):
        '''
        Creates an open-addressed hash map of given size and maximum load factor
        :param initsz: Initial size (default 100)
        :param maxload: Max load factor (default 0.7)
        '''
        self.cap = initsz
        self.table = [None for _ in range(self.cap)]
        self.numkeys = 0
        self.maxload = maxload
        self.hash_func = hash_func
        self.noOfProbes=0
        self.noOfCollisions=0


    def put(self, key, value = 1):
        '''
        Adds the given (key,value) to the map, replacing entry with same key if present.
        :param key: Key of new entry
        :param value: Value of new entry
        '''
        if self.numkeys / self.cap > self.maxload:
            # rehashing
            oldtable = self.table
            # refresh the table
            self.cap *= 2
            self.table = [None for _ in range(self.cap)]
            self.numkeys = 0
            # put items in new table
            for entry in oldtable:
                if entry is not None:
                    self.put(entry[0], entry[1])

        index = self.hash_func(key)% self.cap

        # increment the value
        if self.table[index] is not None and \
           self.table[index] != DELETED and self.table[index].key == key:
            value = self.get(key) + 1
            self.noOfProbes += 1
        # increment the collision
        if self.table[index] is not None and \
           self.table[index] != DELETED and self.table[index].key != key:
            self.noOfCollisions +=1

        while self.table[index] is not None and \
                        self.table[index] != DELETED and \
                        self.table[index].key != key:
            self.noOfProbes += 1
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is None:
            self.noOfProbes +=1
            self.numkeys += 1
        self.table[index] = Entry(key, value)
        # rehash


    def remove(self, key):
        '''
        Remove an item from the table
        :param key: Key of item to remove
        :return: Value of given key
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            self.table[index] = DELETED

    def get(self, key):
        '''
        Return the value associated with the given key
        :param key: Key to look up
        :return: Value (or KeyError if key not present)
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            self.noOfProbes +=1
            if index == self.cap:
                index = 0
        if self.table[index] is not None:
            return self.table[index].value
        else:
            raise KeyError('Key ' + str(key) + ' not present')

    def __contains__(self, key):
        '''
        Returns True/False whether key is present in map
        :param key: Key to look up
        :return: Whether key is present (boolean)
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            self.noOfProbes +=1
            if index == self.cap:
                index = 0
        return self.table[index] is not None




def printMap(map):
    #for i in range(map.cap):
     #   print(str(i) + ": " + str(map.table[i]))
    print('Collisions: ' + str(map.noOfCollisions))
    print('Probes: ' + str(map.noOfProbes))






if __name__ == '__main__':
    testMap()
