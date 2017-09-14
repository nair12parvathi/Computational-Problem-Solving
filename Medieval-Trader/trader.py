"""
file: trader.py
language:python 3
author: pan7447@cs,rit,edu Parvathi Nair
author: dck1135@cs.rit.edu Darshan Kavathe
description: To read files and store data from it and then determine how to get the maximum profit
precondition: name of the item, quantity of the items, and price of each item saved in text file
postcondition: Total profit that can be gained and from which city to buy goods
and in what quantity to buy is displayed
"""
def readFile(filename):
    """
    This method reads the file and gets and stores the data in a dictionary
    precondition: file consiting of data
    postcondition: dicitonary that has data from the files stored in it
    :param filename: name of the file from which the data is to be read
    :return: name of the city
    """
    with open(filename) as f:
        name = f.readline().rstrip("\n")
        d={}
        for line in f:
            line = line.rstrip("\n")
            (itemName, Quantity, Price)=line.split(" ")
            d[itemName]=[int(Quantity),int(Price)]
        return name, d

def profitcal(dict1,dict2):
    """
    This method evaluates the differences between the prices of the items and appends
    it to the dictionary and returns the new dictionaries
    precondition: The dictionaries dict1 and dict2 has the item name, quantity and price
    of each item stored in them
    postcondition: The differences in the price of the items is computed and appended in
    the dictionaries dict1 and dict2
    :param dict1: Dictionary in which the data of hilltown is stored
    :param dict2: Dictionary in which the data of valleydale is stored
    :return: dict1 and dict2, which has the differences of the prices of items
    appended in it.
    """
    for i in dict1:
        dict1[i].append('x')

    for i in dict2:
        dict2[i].append('x')

    for i in dict1:
        x=(dict1[i][1]-dict2[i][1])
        dict1[i][2]=-x
        dict2[i][2] = x
    return dict1,dict2

def convertToList(dict):
    """
    This method converts the dictionary to the list
    precondition:the data from file in dicionary format received as parameter dict
    postcondition: the data from dicitionary dict is stored in a list of lists,
    that is in listOfList
    :param dict: the dictionary which is to be converted
    :return: listOfLists which is the converted data structure,
     the element which is present in either of the dictionary but not in the other
     is removed
    """
    listOfList= [[k, v] for k, v in dict.items()]
    for i in listOfList:
        if i[1][2]=='x':
            listOfList.remove(i)
    return listOfList

def _findMaxIndex(data, mark):
    """
    A helper routine for selectionSort which finds the index
    of the biggest value in data at the mark index or greater.
    precondition:a list of data and maxindex initialised to mark
    postcondition: maxindex has the highest/biggest number from the list
    :param data: a list of data
    :param mark: an index which is in range 0..len(data)-1 inclusive
    :return: An index which is in range 0..len(data)-1 inclusive
    """
    # assume the maximum value is at initial mark position
    maxIndex = mark
    # loop over the remaining positions greater than the mark
    for mark in range(mark+1, len(data)):
        # if a bigger value is found, record its index
        if data[mark][1][2] > data[maxIndex][1][2]:
            maxIndex = mark
    return maxIndex

def selectionSort(data):
    """
    Perform an in-place selection sort of data.
    precondition: unsorted list
    postcondition: sorted list in descending order, order set according to the
    3rd item in the list, that is the price difference
    :param data: The data to be sorted (a list)
    :return: the sorted list (descending order)
    """
    for mark in range(len(data)-1):
        maxIndex = _findMaxIndex(data, mark)
        # swap the element at marker with the min index
        data[mark], data[maxIndex] = data[maxIndex], data[mark]
    return data

def totalProfit(name,sortlist, max):
    """
    This method computes the maximum profit that can be gained considering the
    maximum number of items to be bought
    precondition: The name has the name of the city, sortlist has the details
    in a sorted manner according to the price
    difference, max has the maxium number of itmes that can be bought from a
    city. Result will have the final string or message to be displayed,
    tp(total profit) is initialised to 0
    postcondition: Variable result has the final message to be displayed and
    tp has the total profit calculated
    :param name: name of the city
    :param sortlist: sorted list which contains details which will help
    compute the maximum profit
    :param max: the maximum number of items that can be bought from one
    city and sold in another
    :return: result which is the message to be displayed and tp is the
    total profit computed
    """
    result= "go to "+ name+" and buy"
    tp=0
    for i in range(len(sortlist)):
        if  sortlist[i][1][2]>0 :
            if sortlist[i][1][0]<=max:
                max= max-sortlist[i][1][0]
                t=(sortlist[i][1][2] * sortlist[i][1][0])
                result= result+"\n"+str(sortlist[i][1][0])+ " "+str(sortlist[i][0])+" for profit of "+str(t)
                tp= tp+t
            else:
                t=(sortlist[i][1][2]*max)
                result = result+"\n"+ str(max)+" "+str(sortlist[i][0])+" for profit of "+str(t)
                tp=tp+t
                max=0
        if max==0:
            break
    if tp==0:
         result= result+ "\nno profit"
    return result,tp

def main():
    """
    The main method calls aprropriate functions to read the files, store
    the data in a data structure and to compute the maximum profit
    precondition: the files have the item names, quantity of items and
    price of the items, max is initialised to 10
    postcondition: Making aproprate function calls, the final result is
    computed. The resultH or resultV is displayed when the profit is gained
    by buying goods from the respective cities and selling in the other city.
    tpH and tpV has the total profit that can be made by buying goods and
    selling in the other city
    :return: None
    """
    filename1=input("Enter the first filename :")
    filename2 = input("Enter the second filename :")
    city1, hilltownDict=readFile(filename1)
    city2, valleydaleDict=readFile(filename2)
    max=int (input("Enter the maximum number of items :"))

    hilltownDict, valleydaleDict=profitcal(hilltownDict,valleydaleDict)
    hilltownList=convertToList(hilltownDict)
    valleydaleList=convertToList(valleydaleDict)

    sort_valley= selectionSort(valleydaleList)
    sort_hill = selectionSort(hilltownList)


    resultH,tpH=totalProfit(city1,sort_hill,max)
    resultV,tpV=totalProfit(city2,sort_valley,max)

    if tpH>tpV:
        print(resultH)

    elif tpV>tpH:
        print(resultV)

    else:
        print("Both city has same profit" +"\n" + resultH +"\n" + resultV)


if __name__ == '__main__':
    main()


