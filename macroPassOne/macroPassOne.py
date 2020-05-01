# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:30:25 2020
@author: yeshw
"""
#required list initializations
lst = []#the whole program is converted to a 2d list [->lines[->words]]
#lstMDT[[MDT entry]]
lstMDT = []#for MDT 
#lstMNT[[MNT entry]]
lstMNT = []#for MNT 
#lstALA[[ALA entry]]
lstALA = []
#pointers for MNTC and MDTC
MNTC,MDTC = 1,1

#the MACRO is stored in program.txt
with open('macro.txt') as f:#the file will be read and copied to a list
    for line in f:#the words from the lines are appended by splitting spaces
        lst.append(line.split())
        #printing the raw program code
print('----[MACROPASS1 ASSEMBLER]----') 
with open('macro.txt') as f:
    for line in f: 
        print(line.split())
#actual macro processing starts here
for i in range(len(lst)):
    for j in range(len(lst[0])):
        if lst[i][j] != '-' : 
            #initial MACRO label denotes start of macro
            if lst[i][j] == 'MACRO':
                i += 1
                macroName = lst[i][j]
                templst = [MNTC,macroName,MDTC]
                lstMNT.append(templst)
                MNTC += 1
                templst = [MDTC,lst[i]]
                lstMDT.append(templst)
                MDTC += 1
                templst = lst[i][1:]
                for m in range(len(templst)):
                    arg = templst[m]
                    index = m
                    tempTemplst = [index,arg]
                    lstALA.append(tempTemplst)
                i += 1 
                while lst[i][j] == 'A':
                    templst = lst[i]
                    argName = templst[2]
                    for m in range(len(lstALA)):
                        if argName == lstALA[m][1]:
                            index = lstALA[m][0]
                    templst[2] = index
                    tempTemplst = [MDTC,templst]
                    lstMDT.append(tempTemplst)
                    MDTC += 1
                    i += 1
                if lst[i][j] == 'MEND':
                    templst = lst[i]
                    tempTemplst = [MDTC,templst]
                    lstMDT.append(tempTemplst)
                    MDTC += 1
                
print('-----[MDT]-----')
print('[MDTC,MDT entry]')     
for items in lstMDT:
    print(items)
with open('MDT.txt','w')as f:
    for line in lstMDT:
        for words in line:
            f.write(f'{words}')
            f.write(' ')
        f.write('\n')
print('-----[MNT]-----')
print('[MNTC,MNT entry]')     
for items in lstMNT:
    print(items)
with open('MNT.txt','w')as f:
    for line in lstMNT:
        for words in line:
            f.write(f'{words}')
            f.write(' ')
        f.write('\n')
print('-----[ALA]-----')
print('[INDEX,ALA entry]')     
for items in lstALA:
    print(items)
with open('ALA.txt','w')as f:
    for line in lstALA:
        for words in line:
            f.write(f'{words}')
            f.write(' ')
        f.write('\n')