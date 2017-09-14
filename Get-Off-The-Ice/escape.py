"""
file: escape.py
language: python3
author: pvc8661@rit.edu by  Pallavi Chandanshive
author: pan7447@rit.edu by  Parvathi Nair
description: Implementation of graph to find an escape point from the pond
Based off of vertex.py,graph.py and searchalgs.py created and distributed by CSCI-603 faculty.
"""
from graph import Graph
from searchalgs import *


g=Graph()
escape=Graph()
def main():


    myGraph=[]
    src=[]
    dest=[]


    filename = input("Enter the filename ")
    with open (filename) as f:
        line = f.readline().rstrip("\n")
        FirstLine=(line.split(" "))
        if FirstLine[2].isdigit() and FirstLine[1].isdigit() and FirstLine[0].isdigit():
            if int(FirstLine[2])>int(FirstLine[1]) or int(FirstLine[2])>int(FirstLine[0]) or int(FirstLine[2])<0:
                print("escape point not inside the matrix")
            else:
                for line in f:
                    line = line.rstrip("\n")
                    myGraph.append(line.split(" "))
        else:
            print("invalid characters in the input file")



    for i in range(len(myGraph)):
        for j in range(len(myGraph[i])):
            src=[]
            dest=[]

            if myGraph[i][j]==".":
                src.append(i)
                src.append(j)

                #### right
                if i < int(FirstLine[0]) and i >= 0 and j < int(FirstLine[1]) and j >= 0:
                    dest=[]
                    counter=0
                    tempj=j
                    while j+1 < int(FirstLine[1]) and myGraph[i][j]!='*' and myGraph[i][j+1]!='*':
                        j=j+1
                        counter=counter+1
                    if j!=tempj:
                        if i==int(FirstLine[2]) and j==int(FirstLine[1])-1:
                            g.addEdge((str(src[0]) + ',' + str(src[1])), escape)
                        else:
                            dest.append(i)
                            dest.append(j)
                            g.addEdge((str(src[0]) + ',' + str(src[1])), (str(dest[0]) + ',' + str(dest[1])))
                    j=j-counter



                ####bottom
                if i < int(FirstLine[0]) and i >= 0 and j < int(FirstLine[1]) and j >= 0:
                    dest=[]
                    counter=0
                    tempi=i
                    while i+1 < int(FirstLine[0]) and myGraph[i][j]!='*' and myGraph[i+1][j]!='*':
                        i=i+1
                        counter=counter+1
                    if i!=tempi:
                        if i==int(FirstLine[2]) and j==int(FirstLine[1])-1:
                            g.addEdge((str(src[0]) + ',' + str(src[1])), escape)
                        else:
                            dest.append(i)
                            dest.append(j)
                            g.addEdge((str(src[0]) + ',' + str(src[1])), (str(dest[0]) + ',' + str(dest[1])))
                    i=i-counter



                ####left
                if i < int(FirstLine[0]) and i >= 0 and j < int(FirstLine[1]) and j >= 0 and j-1>=0:
                    dest=[]
                    counter=0
                    tempj = j
                    while j-1>=0 and myGraph[i][j] != '*' and myGraph[i][j-1] != '*':
                        j = j - 1
                        counter = counter + 1
                    if j != tempj:
                        if i==int(FirstLine[2]) and j==int(FirstLine[1])-1:
                            g.addEdge((str(src[0]) + ',' + str(src[1])), escape)
                        elif i==int(FirstLine[2]) and tempj==int(FirstLine[1])-1:
                            dest.append(i)
                            dest.append(j)
                            g.addEdge(escape, (str(dest[0]) + ',' + str(dest[1])))

                        else:
                            dest.append(i)
                            dest.append(j)
                            g.addEdge((str(src[0]) + ',' + str(src[1])), (str(dest[0]) + ',' + str(dest[1])))
                    j = j + counter



                ####top
                if i < int(FirstLine[0]) and i >= 0 and j < int(FirstLine[1]) and j >= 0 and i-1>=0:
                    dest=[]
                    counter=0
                    tempi = i
                    while i-1>=0 and myGraph[i][j] != '*' and myGraph[i-1][j] != '*':
                        i = i - 1
                        counter = counter + 1
                    if i != tempi:
                        if i==int(FirstLine[2]) and j==int(FirstLine[1])-1:
                            g.addEdge((str(src[0]) + ',' + str(src[1])), escape)
                        else:
                            dest.append(i)
                            dest.append(j)
                            g.addEdge((str(src[0]) + ',' + str(src[1])), (str(dest[0]) + ',' + str(dest[1])))
                    i = i + counter


    escapeList(FirstLine,escape)
"""
     prints  the list of vertices with their corresponding number of moves to reach escape point
    :param FristLine: List that contains no of rows,no of columns and the row number of escape point
    :param escape   : Vertex object of the escape point
"""
def escapeList(FirstLine,escape):
    keyList=[]
    dict=g.getVertices()
    keyList=list(dict)
    dictResult={}
    noPath=""
    noPathList=[]


    for i in range(len(keyList)):
        src=g.getVertex(keyList[i])
        dest=g.getVertex(escape)
        pathList=findShortestPath(src,dest)
        if pathList==None:
            noPathList.append(str(keyList[i]))
        else:
            l=len(pathList)-1
            if (l > 0):

                if l in dictResult:
                    dictResult[l].append(keyList[i])
                else:
                    dictResult[l]=[keyList[i]]

    for key in dictResult.keys():
        print(str(key) + ':' + str(list(dictResult[key])))\

    if noPathList != []:
        print("No Path from: " + str(noPathList))














if __name__ == '__main__':
    main()


