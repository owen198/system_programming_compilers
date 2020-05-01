# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 21:26:07 2020
@author: yeshw
"""
import time
#required list initializations
lst = []#the whole program is converted to a 2d list [->lines[->words]]
lstOp = []
#lstSt[[symbol,value,length]]
lstSt = []#for symbol table
#lstLt[[literal,value,length]]
lstLt = []#for literal table
#baseAddress eg for USING *,15
baseAddr = 0 # starts from 15 if none
#the ALP is stored in program.txt
with open('program.txt') as f:#the file will be read and copied to a list
    for line in f:#the words from the lines are appended by splitting spaces
        lst.append(line.split())
#the symbol table is stored in symboltable.txt
with open('symboltable.txt') as f:
    for line in f:#copying and converting to a list
        lstSt.append(line.split())
#the literal table is stored in literaltable.txt        
with open('literaltable.txt') as f:
    for line in f:#copying and converting to a list
        lstLt.append(line.split())        
print('----[PASS2 ASSEMBLER]----') 
#opening and storing the initial files
with open('program.txt') as f:
    for line in f: 
        time.sleep(0.25) 
        print(line.split())
print('-----[SYMBOL TABLE]-----')
print('[symbol,value,length]')     
for items in lstSt:
    time.sleep(0.25)
    print(items)
print('-----[LITERAL TABLE]-----')
print('[literal,value,length]')  
for items in lstLt:
    time.sleep(0.25)
    print(items)     
#actual PASS2 begins here!
for i in range(len(lst)):
    for j in range(len(lst[0])):
        if lst[i][j] != '-':
            #initial program
            if lst[i][j] == 'START':
                if lst[i][j+1] == '-':
                    index = 0
                    templst = lst[i]
                lstOp.append(templst)
            #fetching base address if any
            if lst[i][j] == 'USING':
                tmp = lst[i][j+1].split(',')
                if tmp[1].isnumeric():
                    baseAddr = tmp[1]
                    templst = lst[i]
                else:
                    for m in range(len(lstSt)):
                        for n in range(len(lstSt[0])):
                            if tmp[1] == lstSt[m][n]:
                                baseAddr = lstSt[m][n+1]
                    templst = ['-', 'USING', f'*,{baseAddr}']
                lstOp.append(templst)
            # processing instructions and literals (RX,RR)     
            if lst[i][j] == 'L' or lst[i][j] == 'A' or lst[i][j] == 'ST':
                tmp = lst[i][j+1].split(',')
                if tmp[1].isnumeric():
                    templst = lst[i]
                    lstOp.append(templst)  
                elif tmp[1][0] == '=':
                        for m in range(len(lstLt)):
                            for n in range(len(lstLt[0])):
                                if tmp[1][1:] == lstLt[m][n]:
                                    offset = lstLt[m][n+1]
                                    templst = lst[i]
                                    tempAdd = f'{offset}({index},{baseAddr})'
                                    tmp[1] = tempAdd
                                    templst[2] = tmp
                        lstOp.append(templst)  
                else:
                     for m in range(len(lstSt)):
                        for n in range(len(lstSt[0])):
                            if tmp[1] == lstSt[m][n]:
                                offset = lstSt[m][n+1]
                                templst = lst[i]
                                tempAdd = f'{offset}({index},{baseAddr})'
                                tmp[1] = tempAdd
                                templst[2] = tmp
                     lstOp.append(templst) 
            #checking labels and processing DC          
            if lst[i][j] == 'DC':
                tmpLbl = lst[i][j-1]
                tmpVal = bin(int(lst[i][j+1][2])).replace('0b','0')
                templst  = [tmpLbl,tmpVal,'-']
                lstOp.append(templst) 
            #checking labels and processing DS     
            if lst[i][j] == 'DS':
                tmpLbl = lst[i][j-1]
                tmpVal = '-'
                templst  = [tmpLbl,tmpVal,'-']
                lstOp.append(templst)       
            #checking labels and processing EQU     
            if lst[i][j] == 'EQU':
                tmpLbl = lst[i][j-1]
                tmpLen = '-'
                templst  = [tmpLbl,tmpLen,'-']
                lstOp.append(templst)
            #final program label END
            if lst[i][j] == 'END':
                for i in range(len(lstLt)):#processing literals
                    tmpVal = bin(int(lstLt[i][0][2])).replace('0b','0')
                    tmpLbl = '-'
                    templst  = [tmpLbl,tmpVal,'-']
                    lstOp.append(templst)
                templst  = ['-','END','-']
                lstOp.append(templst)
print('-----[PASS2 OUTPUT]-----')
for items in lstOp:print(items)
print('________________________')