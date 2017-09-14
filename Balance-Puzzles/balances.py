"""
file: DNALIst.py
language: python3
author: pvc8661@rit.edu by  Pallavi Chandanshive
author: pan7447@rit.edu by  Parvathi Nair
description: Implementation of balance puzzle
"""
import turtle
import math
SCALING_FACTOR_VERTICAL=20 #Global variable defined for the turtle to draw vertical lines
"""
    This class is used to store the value of the weight at each distance. This value can be of type beam or int
"""
class Weight:
    __slots__='type','value'

    """
        This constuctor sets the value of type and value
        :param type: represents the Beam
        :param value: represents the weight
    """
    def __init__(self,type,value):
        self.type=type
        self.value=value

    """
        This methods sets the value of the weight when the weight is missing
        precondition:  value of weight passed from th efindweight function
        postcondition: instance variable value is set to th evale passed by local variable
        :param value:  represents the weights
    """
    def setWeight(self,value):
        self.value = value

    """
        This methods sets the value of the type and value
        precondition:  value of weight -1
        postcondition: value of weight is set to the computed value of missing weight
        :param value:  represents the weights
    """
    def __str__(self):
        return  self.type + " "+ str(self.value)

class Beam:
    """
        This class is used to store the pair of distnace and value
    """
    __slots__='dictBeam','totalDistance','minL','maxR'

    def __init__(self):
        self.dictBeam={}
        self.minL=0
        self.maxR=100

    """
        This methods checks whether beam is balanced or not
        precondition:  beam is passed to check if it is balanced or imbalanced
        postcondition: balanced is set to False when the beam is imbalanced
    """
    def balanceBeam(self):
        total = 0
        var = 0
        for k in self.dictBeam.keys():
            if isinstance(self.dictBeam.get(k).value,Beam):
                total = total + k * self.dictBeam.get(k).value.getAllTotal()
            else:
                if self.dictBeam.get(k).value < 0:
                    var = k
                else:
                    total = total + k * self.dictBeam.get(k).value
        if total != 0:
            print("imbalanced")
            balanced = False
            return balanced
        else:
            return True

            #self.dictBeam[k] = Weight("int", total/k)

            #if total > 0:
             #   self.dictBeam[1] = Weight("int",total)
            #else:
               # self.dictBeam[-1] = Weight("int",-1*total)

    """
        This methods finds the total distance
        precondition:  total is intially set  0
        postcondition: total distance is computed and set in total
    """
    def getAllTotal(self):
        total = 0;
        print(self.dictBeam)
        for k in self.dictBeam.keys():
            if isinstance(self.dictBeam.get(k).value,Beam):
                total += self.dictBeam.get(k).value.getAllTotal()
            else:
                total += self.dictBeam.get(k).value
        return total

    """
        This methods checks whether there is any missing weight present in the beam
        precondition:  Intially weight is -1
        postcondition: Weight is set to the value computed in this function
    """
    def findWeight(self):
        leftTorque = rightTorque = 0
        for k in self.dictBeam.keys():
            if k<0:
                if self.dictBeam.get(k).value == -1:
                    missingWeight = self.dictBeam.get(k)
                    distance = k
                else:
                    leftTorque += self.dictBeam.get(k).value
            else:
                if self.dictBeam.get(k).value == -1:
                    missingWeight = self.dictBeam.get(k)
                    distance = k
                else:
                    rightTorque += self.dictBeam.get(k).value
        if distance<0:
            weight = (rightTorque - leftTorque)/-1*distance
        else:
            weight = (leftTorque - rightTorque) /distance

        missingWeight.setWeight(weight)
        return (weight)

    """
        This methods calculates the distance from left to right of the beam
        precondition:  totalDistance is initially 0
        postcondition: totalDistance is set to the difference between maxR and minL
    """
    def calculateTotal(self):
        for k in self.dictBeam.keys():
            if k < self.minL:
                self.minL=k
            elif k>self.maxR:
                self.maxR=k
        self.totalDistance=self.maxR-self.minL

    """
        This method overrides the default string method and returns the dictionary dictBeam
    """
    def __str__(self):
        return  self.dictBeam


"""
    This methods reads the text file and calls appropriate fnctions and then draws the final output using turtle
"""

def main():
    min = 1000
    max = 0

    filename = input("Enter the filename ")
    with open(filename) as f:
        dictMainBeam={}
        for line in f:
            balanced = True
            line = line.rstrip("\n")
            missingWeight = False
            for i in line:
                element=line.split(" ")
                tempB=0
                if len(element[0])==1:
                    dictMainBeam[0]=Beam()

                else:
                    dictMainBeam[int(element[0][1])]=Beam()
                    tempB=int(element[0][1])
                index=1
                while index<len(element):
                    value = ''
                    type = ''
                    if element[index+1][0] == 'B':
                        value=dictMainBeam[int(element[index+1][1])]
                        type="beams"
                    else:
                        value=int(element[index+1])
                        if value== -1:
                            missingWeight = True
                        type = "int"
                    dictMainBeam.get(tempB).dictBeam[int(element[index])]= Weight(type,value)
                    if int(element[index])>max:
                       max=int(element[index])
                    if int(element[index])<min:
                       min=int(element[index])
                    index+=2
            if missingWeight:
                weight = dictMainBeam.get(tempB).findWeight()
                print("Missing wt=",weight)
            balanced = dictMainBeam.get(tempB).balanceBeam()
            dictMainBeam.get(tempB).calculateTotal()
    print (dictMainBeam)
    if balanced == True:
        draw(dictMainBeam,dictMainBeam.get(0))
        turtle.mainloop()


"""
    This method draws the beam
    precondition: Turtle is at coordinates(0,0),facing east, pendown
    postcondition: Turtle is at coordinates(0,0),facing east, pendown
"""

def draw(dictMainBeam,currentBeam):
    turtle.right(90)
    turtle.forward(SCALING_FACTOR_VERTICAL)
    turtle.left(90)
    print(currentBeam.dictBeam)
    tD = 50;
    for k in currentBeam.dictBeam.keys():
        v = currentBeam.dictBeam.get(k)
        if isinstance(v.value,Beam):
            tD = tD + v.value.totalDistance + 20
    print(tD)
    tD = tD / 2
    for k in currentBeam.dictBeam.keys():
        print (k)
        v=currentBeam.dictBeam.get(k)
        turtle.forward(k*tD)
        if isinstance(v.value,Beam):
            draw(dictMainBeam,v.value)
        else:
            turtle.write(v.value)
        turtle.backward(k*tD)
    turtle.left(90)
    turtle.forward(SCALING_FACTOR_VERTICAL)
    turtle.right(90)
if __name__ == '__main__':
    main()
