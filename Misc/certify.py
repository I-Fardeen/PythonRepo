#for Python Certification
#Q1 Pune:Delhi:937776767,Belgium:Brussels:9837437272 -> Puhi371,Bels302
# We are required to take ticket values separated by comas, generate genTicketId
# by taking first two letters of source and dest and appending the sum of even
# positioned digits of the mobile number followed by a sequence char 1 to n...
# example-> Pune:Delhi:937776767 should be 'Pu'+'hi'+'37'+'1'
from collections import defaultdict
import re
import math as mt
def genTicketId():
    inputstring = input()
    tickets = re.split(",",inputstring)
    #print(tickets)
    n = len(tickets)
    for i in range(0,n):
        ticket = re.split(":",tickets[i])
        #print(ticket) #ticket is a list ['Pune','Delhi,'937776767']
        str1 = ticket[0][0:2]
        str2 = ticket[1][-2:]
        sum = 0
        for c in ticket[2][0::2]:
            sum = sum + int(c)
        print(str1 + str2 + str(sum) + str(i+1)+",")

#Q2 is people are in a queue, [2,3,4,2,5,3,3] get the average of this
# list and then the floor of the same, if that number is in the list
# calculate the max distance of it from another of its occurence.
# return -1 if not present, return max distance of the number that's our
# winner.
def luckyWinner():
    inputstring = input()
    n = len(inputstring) #SUPER WRONG! IT PRINTS 13 INCLUDING THE ,
    print(n)#WRONG!
    inputlist = re.split(",",inputstring)
    print(inputlist)
    newint = []
    for i in inputlist:
        newint.append(int(i))
    print(newint)
    nn = len(newint) #THIS IS RIGHT!
    avg = sum(newint)/nn
    print(avg)
    flv = mt.floor(avg)
    print(flv)
    if flv in newint:
        temp = defaultdict(list)
        ele = flv
        for idx,ele in enumerate(newint):
            temp[ele].append(idx)
        res = max(temp[ele][-1]-temp[ele][0] for ele in temp)
        if(res in newint):
            print(res)
        else:
            print(-1)
