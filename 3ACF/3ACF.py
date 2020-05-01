# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 01:07:09 2020
@author: yeshw
"""
print('✖️'*20)#margin
print('3ACF Intermediate Code Generator!')#sample input : b+c*d-p or b*-c+b*-c
ip_str = input('ENTER INPUT STRING : ')#taking input string
ip_lst = list(map(str,ip_str))#converting input string into a list
prio_dict = {'-':1,'+':2,'*':3,'/':4}#dictionary for maintaining priority
op_lst = []#empty list for storing output
op_lst.append(['op','arg1','arg2','result'])
def find_top_prio(lst):
    top_prio = 1#finding highest priority operator from input
    count_ops = 0#initial number of operators
    for ops in lst:#scan all ele from list
        if ops in prio_dict:#scan ele if its present in dict
            count_ops += 1#increment to find count of the list
            if prio_dict[ops] > 1:#check base priority
                top_prio = prio_dict[ops]#update priority if greater
    return top_prio,count_ops
top_prio,count_ops = find_top_prio(ip_lst)#use function to get the top op
ip = ip_lst#creating a dummy list to work with
i,res = 0,0#maintains counter of the temp variable and while loop
while i in range(len(ip)):#dynamic while loop which chnages with length of ip
    if ip[i] in prio_dict:#check operator
        op = ip[i]#get the operator
        if (prio_dict[op]>=top_prio) and (ip[i+1] in prio_dict):#for singleop
            res += 1#incr res
            op_lst.append([ip[i+1],ip[i+2],' ','t'+str(res)])#append to output
            ip[i+1] = 't'+str(res)#make temp var
            ip.pop(i+2)#remove operand 1
            i = 0#reset counter
            top_prio,count_ops = find_top_prio(ip)#get updated data
        elif prio_dict[op]>=top_prio:#check priority of op
            res += 1#incr res
            op_lst.append([op,ip[i-1],ip[i+1],'t'+str(res)])#append to output
            ip[i] = 't'+str(res)#make temp var
            ip.pop(i-1)#remove operand 1
            ip.pop(i)#remove operand 2
            i = 0#reset counter
            top_prio,count_ops = find_top_prio(ip)#get updated data
        if len(ip) == 1:#if list is almost empty
            op_lst.append(['=',ip[i],' ','a'])#final output append
    i += 1#increment i for while loop i.e check next element
print('3ACF Intermediate Code!')#printing the final table
for items in op_lst: print(items)#print outputlist line by line
print('✖️'*20)#done!
