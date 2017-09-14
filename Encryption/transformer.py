"""
file: transformer.py
language:python 3
author: pan7447@cs,rit,edu Parvathi Nair
author: dck1135@cs.rit.edu Darshan Kavathe
description: To generate fractals in 3 different ways
precondition: messages and operations as strings
postcondition: messages encrypted or decrypted as per user input
"""
def encrypt_Sik(message,i,k):
    """
    This method shifts the letter at index i forward by k
    precondition: string message read from the file
    postcondition: string message after performing the shift operation

    :param message: string on which the operation has to be performed
    :param i: index of the string which is to be shifted
    :param k: number of times it has to be forwarded
    :return: encrypted message after performing shift operation
    """
    result = message[0:i]
    temp = ord(message[i:i + 1])
    if k>0:
        while(k>0):
            if temp == 90:
                temp = 64
            temp = temp + 1
            k=k-1
    elif k<0:
        k=-1*k
        while (k > 0):
            if temp == 65:
                temp = 91
            temp = temp - 1
            k = k - 1
    elif k==0:
        #print(message)
        return message
    trans_temp = chr(temp)
    result = result + trans_temp
    result = result + message[(i + 1):len(message)]
    return result

def decrypt_Sik(message,i,k):
    """
    This method shifts the letter at index i backwards by k
    precondition: string message read from the file
    postcondition: string message after performing the shift operation
    :param message:string on which the operation has to be performed
    :param i:index of the string which is to be shifted
    :param k:number of times it has to be shifted backward
    :return:decrypted message after performing shift operation
    """
    result = message[0:i]
    temp = ord(message[i:i + 1])
    if k>0:
        while(k>0):
            if temp == 65:
                temp = 91
            temp = temp - 1
            k=k-1
    elif k<0:
        k=-1*k
        while (k > 0):
            if temp == 90:
                temp = 64
            temp = temp + 1
            k = k - 1
    elif k==0:
        return message

    trans_temp = chr(temp)
    result = result + trans_temp
    result = result + message[(i + 1):len(message)]
    return result

def encrypt_Ri(message,i):
    """
    Rotates the string i times
    precondition: string message read from the file
    postcondition:string message after performing the rotate operation
    :param message:string on which the operation has to be performed
    :param i: number of times it has to be rotated
    :return: string after performing rotation
    """
    result=message
    if i>0:
        while (i > 0):
            temp = result[-1]
            result = temp + result[0:len(message) - 1]
            i = i - 1
    elif i<0:
        i=-1*i
        while (i > 0):
            temp = result[0]
            result = result[1:len(message)]+temp
            i = i - 1
    elif i==0:
        print(message)
        return
    return result

def decrypt_Ri(message,i):
    """
    This method performs reverse rotation
    precondition:string message read from the file
    postcondition:string after performing the rotation
    :param message:string on which the operation has to be performed
    :param i: number of rotaion
    :return:string after performing the operation on it
    """
    result=message
    if i>0:
        while (i > 0):
            temp = result[0]
            result = result[1:len(message)]+temp
            i = i - 1
    elif i<0:
        i=-1*i
        while (i > 0):
            temp = result[-1]
            result = temp + result[0:len(message) - 1]
            i = i - 1
    elif i==0:
        print(message)
        return
    return result

def encrypt_Dik(message, i, k):
    """
    This message duplicates the element at index i ,k time
    precondition: string read from the file
    postcondition: string has the duplicate operation performed on it
    :param message:string on which the operation has to be performed
    :param i:index of the element to be duplicated
    :param k: number of times the letter has to be duplicated
    :return: string after performing the duplication operation
    """
    result=message
    while(k>0):
        temp=result
        result=result[0:i+1]+result[i:i+1]+result[i+1:len(temp)]
        k=k-1
    return result

def decrypt_Dik(message, i, k):
    """
    This method  performs the reverse operation of duplication and removes the duplicates
    precondition:string read from the file
    postcondition:string has the operation performed on it
    :param message: string on which the operation has to be performed
    :param i:the index where the duplicates are found
    :param k: number of times the reverse of
    :return: string after removing the duplicates
    """
    result=message
    while(k>0):
        #temp=result
        result = result[0:i + 1] + result[i + 2:len(result)]
        k=k-1
    return result


def encrypt_Tgij(message,g, i, j):
    """
    this method performs swap operation
    precondition:string read from the file
    postcondition:string has the operation performed on it
    :param message:string on which the operation has to be performed
    :param i: index of element which is to be swapped with element at j
    :param g: number of equal partitions
    :param j:index of element which is to be swapped with element at i
    :return: string after performing operation
    """
    result=[]
    #groups=g
    start=0
    inc=len(message)//g
    end=inc
    while end <= len(message):
        result.append(message[start:end])
        start = end
        end = end + inc
    #print(result)
    temp = []
    temp.append(result[i])
    result[i] = result[j]
    result[j] = temp[0]
    answer=("".join(result))
    return answer


def decrypt_Tgij(message,g, i, j):
    """
     this method performs swap operation(decryption)
    precondition:string read from the file
    postcondition:string has the operation performed on it

    :param message:string on which the operation has to be performed
    :param i: index of element which is to be swapped with element at j
    :param j:index of element which is to be swapped with element at i
    :param g: number of equal partitions
    :return: string after performing operation
    """
    result=[]
    #groups=g
    start=0
    inc=len(message)//g
    end=inc
    while end <= len(message):
        result.append(message[start:end])
        start = end
        end = end + inc
    #print(result)
    temp = []
    temp.append(result[i])
    result[i] = result[j]
    result[j] = temp[0]
    answer=("".join(result))
    return(answer)

def encrypt_A(message):
    """
    this method is the secret operation which converts the first letter to the respective  element from backwards, that is A is converted to z, B is converted to Y
    precondition:string read from the file
    postcondition:string has the operation performed on it
    :param message:string on which the operation has to be performed
    :return:encrypted message
    """
    temp=message[1:]
    result=chr(ord('Z')-ord(message[0])+ord('A'))+temp
    return result

def decrypt_A(message):
    """
    this method performs the reverse operation of A
     precondition:string read from the file
    postcondition:string has the operation performed on it
    :param message:message read from the file
    :return:decrypted message
    """
    temp = message[1:]
    result = chr(ord('Z') - ord(message[0]) + ord('A'))+temp
    return result




def decide(line, op, perform):
    """
    precondition: takes input
    postcondition: decides what operation to be performed
    :param line: string which is to be encrypted or decrypted
    :param op: operations
    :param perform: e for encryption and d for decryption
    :return: encrypted or decrypted string
    """
    if op[0]=="S":
        i=int(op[1])
        k=1
        if len(op)>2:
            k=int(op[3])
        if perform=="e":
            return encrypt_Sik(line, i, k)
        else:
            return decrypt_Sik(line, i, k)

    if op[0]=="R":
        i=1
        if len(op)>1:
            i=int(op[1])
        if perform=="e":
            return encrypt_Ri(line, i)
        else:
            return decrypt_Ri(line, i)

    if op[0]=="D":
        i=int(op[1])
        k=1
        if len(op)>2:
            k=int(op[3])
        if perform=="e":
            return encrypt_Dik(line, i, k)
        else:
            return decrypt_Dik(line, i, k)

    if op[0]=="T":
        if len(op) > 4:
            g=int(op[2])
            i=int(op[4])
            j=int(op[6])
            if perform == "e":
                return encrypt_Tgij(line, g, i, j)
            else:
                return decrypt_Tgij(line, g, i, j)
        else:
            i=int(op[1])
            j=int(op[3])
            g=len(line)
            if perform == "e":
                return encrypt_Tgij(line, g, i, j)
            else:
                return decrypt_Tgij(line, g, i, j)

    if op[0] == "A":

        if perform == "e":
            return encrypt_A(line)
        else:
            return decrypt_A(line)

def main():
    """
    precondition: string to be encrypted or decrypted
    postcondition: string after encryption or decryption
    :return: None
    """
    file=input("Which file do you want to read")
    operation = input("which file has your operations")
    o=open (operation)
    with open (file) as f:
        perform = input("Enter e for encryption and d for decryption")
        for line in f:

            op=o.readline().strip("\n").split(";")

            if perform=="e" :
                for i in op:
                    line=decide(line.strip("\n"), i, perform)
            else:
                for i in range(len(op)):
                    line = decide(line.strip("\n"), op[len(op)-1-i], perform)

            print(line)
    o.close()


if __name__ == '__main__':
    main()