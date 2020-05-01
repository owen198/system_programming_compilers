# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:21:32 2020
@author: yeshw
"""
import time
#required list initializations
lst = []#the whole program is converted to a 2d list [->lines[->words]]
#lstOp[[Op entry]]
lstOp = []#for out
#the card is stored in card.txt
with open('card.txt') as f:#the file will be read and copied to a list
    for line in f:#the words from the lines are appended by splitting spaces
        lst.append(line.split())
#extracting card info
cardType = int(lst[0][0])
cardLength = int(lst[1][0])
cardAddr = int(lst[2][0][:4])
#printing input file
print('[absLoader input]')
for items in lst:print(items)
#starting actual absolute loadr here!
for i in range(3,len(lst)):
    if lst[i][1] == 'L' or lst[i][1] == 'A' or lst[i][1] == 'ST':
        tempAddr = int(lst[i][0]) + cardAddr
        tempLc = int(lst[i][2]) + cardAddr
        lstOp.append([tempAddr,lst[i][1],tempLc])
    elif lst[i][1].isnumeric():
        tempAddr = int(lst[i][0]) + cardAddr
        lstOp.append([tempAddr,lst[i][1]])
#printing the output card
print('-----------------')
print('[absLoader output]')
print(f'cardType: {cardType}\ncardLength: {cardLength}\ncardAddr: {cardAddr}')
for items in lstOp:print(items)
with open('output.txt','w')as f:
    for line in lstOp:
        for words in line:
            f.write(f'{words}')
            f.write(' ')
        f.write('\n')   