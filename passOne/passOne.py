# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:22:16 2020
@author: yeshw
"""
import time
#required list initializations
lst = []#the whole program is converted to a 2d list [->lines[->words]]
lc  = 0 #locationCounter
#lstSt[[symbol,value,length]]
lstSt = []#for symbol table
#baseAddress eg for USING *,15
baseAddr = 0 # starts from 15 if none
#lstLt[[literal,value,length]]
lstLt = []#for literal table
#the ALP is stored in program.txt
with open('program.txt') as f:#the file will be read and copied to a list
    for line in f:#the words from the lines are appended by splitting spaces
        lst.append(line.split())
        #printing the raw program code
print('----[PASS1 ASSEMBLER]----') 
with open('program.txt') as f:
    for line in f: 
        time.sleep(0.25) 
        print(line.split())
#actual PASS1 begins here!
for i in range(len(lst)):
    for j in range(len(lst[0])):
        if lst[i][j] != '-' : 
            #initial program label eg PG3
            if lst[i][j] == 'START':
                tmpLbl = lst[i][j-1]
                tmpVal = lc
                tmpLen = 1
                tmpSt  = [tmpLbl,tmpVal,tmpLen]
                lstSt.append(tmpSt)
                lc += 0                
            #fetching base address if any    
            if lst[i][j] == 'USING':
                tmp = lst[i][j+1].split(',')
                if tmp[1].isnumeric():
                    baseAddr = tmp[1]
                lc += 0                
            # processing instructions and literals (RX,RR)    
            if lst[i][j] == 'L' or lst[i][j] == 'A' or lst[i][j] == 'ST':
                tmp = lst[i][j+1].split(',')
                if tmp[1].isnumeric():
                    lc += 2
                elif tmp[1][0] == '=':
                    if tmp[1][1] == 'F':
                        tmpLt = [tmp[1][1:],'-',4]
                        lstLt.append(tmpLt)
                        lc += 4
                else:
                    lc += 4                
            #checking labels and processing DC    
            if lst[i][j] == 'DC':
                tmpLbl = lst[i][j-1]
                tmpVal = lc
                tmpLen = lst[i][j+1]
                if tmpLen[0] == 'F':
                    lc += 4    
                    symlen = 4
                tmpSt  = [tmpLbl,tmpVal,symlen]
                lstSt.append(tmpSt)     
            #checking labels and processing DS         
            if lst[i][j] == 'DS':
                tmpLbl = lst[i][j-1]
                tmpVal = lc
                tmpLen = lst[i][j+1]
                tmpSt  = [tmpLbl,tmpVal,int(tmpLen[0])*4]
                lstSt.append(tmpSt)
                if tmpLen[2] == 'F':
                    lc += int(tmpLen[0]) * 4                     
            #checking labels and processing EQU         
            if lst[i][j] == 'EQU':
                tmpLbl = lst[i][j-1]
                tmpVal = lst[i][j+1]
                tmpLen = 1
                baseAddr = int(tmpVal)
                tmpSt  = [tmpLbl,int(tmpVal),tmpLen]
                lstSt.append(tmpSt)
                lc += 0
            #final program label END
            if lst[i][j] == 'END':
                lc += 0  
                for i in range(len(lstLt)):#processing and storing literals
                    lstLt[i][1] = lc
                    lc += lstLt[i][2]        
                 
print('-----[SYMBOL TABLE]-----')
print('[symbol,value,length]')     
for items in lstSt:
    time.sleep(0.25)
    print(items)
with open('symboltable.txt','w')as f:
    for line in lstSt:
        for words in line:
            f.write(f'{words}')
            f.write(' ')
        f.write('\n')
print('-----[LITERAL TABLE]-----')
print('[literal,value,length]')  
for items in lstLt:
    time.sleep(0.25)
    print(items)   
with open('literaltable.txt','w')as f:
    for line in lstLt:
        for words in line:
            f.write(f'{words}')
            f.write(' ')
        f.write('\n')
print('________________________')