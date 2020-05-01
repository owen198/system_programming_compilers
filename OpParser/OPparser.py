# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 23:55:43 2020
@author: yeshw
"""
#required list initializations
lst = []#the whole program is converted to a 2d list [->lines[->words]]
lst_var,lst_terminal = [],[]#list for terminal and nonterminal variables
lst_opt,lst_idt = [],[]#list for operator and identifier terminal
with open('input.txt') as f:#the input file will be read and copied to a list
    for line in f:#the words from the lines are appended by splitting spaces
        lst.append(line.split())
tmp_var,tmp_terminal = [],[]
for i in range(len(lst)):#fetching variables,terminals from input file
    for j in range(len(lst[i])):
        if lst[i][j].isupper():
            tmp_var.append(lst[i][j])
        else:
            tmp_terminal.append(lst[i][j])
lst_var,lst_terminal = list(set(tmp_var)),list(set(tmp_terminal))
for element in lst_terminal:#seperating operator terminal and identifier
    if element.isalpha():
        lst_idt.append(element)
    else:
        lst_opt.append(element)
lst_terminal.append('$')
print('//IDENTIFYING ELEMENTS FROM THE INPUT//\n')
for items in lst:print(items)
print('\nVARIABLES : ',lst_var)
print('TERMINALS : ',lst_terminal)
print('OPERATOR TERMINALS : ',lst_opt)
print('IDENTIFIER TERMINALS : ',lst_idt)
print('\n//CONSTRUCTING THE PRECEDENCE TABLE//\n')
N = len(lst_terminal) + 1#length of the table
tbl = [['-' for j in range(N)] for i in range(N)]#initializing table
dVal = {'id':5,'*':4,'+':3,'$':0}#dict of variable values
for i in range(1,len(tbl)):
    for j in range(1,len(tbl[0])):#creating the table
        tbl[0][1] = tbl[1][0] = lst_terminal[2]
        tbl[0][2] = tbl[2][0] = lst_terminal[1]
        tbl[0][3] = tbl[3][0] = lst_terminal[0]
        tbl[0][4] = tbl[4][0] = lst_terminal[3]        
        a,b = tbl[i][0],tbl[0][j]
        #rules
        if dVal[a] == dVal[b] == 0:
            tbl[i][j] = 'accept'
        elif dVal[a] == dVal[b] == 5:
            tbl[i][j] = '-'
        elif dVal[a] == dVal[b] == 4 or dVal[a] == dVal[b] == 3:
            tbl[i][j] = '>'
        elif dVal[a] > dVal[b]:
            tbl[i][j] = '>'
        elif dVal[a] < dVal[b]:
            tbl[i][j] = '<'
        else:
            tbl[i][j] = '='           
for items in tbl:print(items)
print('\n//RUNNING OPERATOR PRECEDENCE PARSER//\n')
print("ENTER A STRING FOR PARSER",end='')
buffer= list(input().split())#taking input string and converting to list
buffer.append('$')#initializing buffer
stack = ['$']#initializing stacktop
k,result = 0,0#pointer[stacktop] k = 0, and result is false
action = 'none'
print('\n[[STACK]  [BUFFER]  [ACTION]]')
while True:#infinite loop
    a = stack[k]#initialize a to stack element
    b = buffer[0]#b is the input symbol from the buffer
    tmp = [stack,buffer,action]
    print(tmp)
    if a == b == '$':#string accept state
        result = 1#set result true
        action = 'ACCEPT'
        break#exit out of loop
    elif dVal[a] < dVal[b] or dVal[a] == dVal[b]:#if a<b or a==b
        stack.append(b)#push a onto stack
        action = 'SHIFT'
        buffer.remove(b)#read next ip symbol from buffer
        k += 1#increment k
    elif dVal[a] > dVal[b]:
        stack.pop()#pop top of stack
        action = 'REDUCE'
        k -= 1#decrement k
    else:
        print('\nERROR WHILE PARSING!')
        break# result is false break out of loop

if result == 1:
    print('\nSTRING ACCEPTED!')
    print('STRING HAS BEEN PARSED SUCESSFULLY!')        