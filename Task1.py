#Part 1: Fetching all the files and folders 
import os
from collections import OrderedDict
from datetime import datetime
import pathlib

#path = input("enter folder path: ")
#path = 'C:\\Users\\USER\\Python Stuff'
path = os.getcwd()
dir_list = os.listdir(path)


#Part 2:
#this is sor4
# ting according to dec order of file size
""""dir_list.sort()
print("--------sorted--------------")
print(dir_list)"""
def ByName(dir_list):
    return dir_list

list_date = {}
def ByLastModified(directory):
    for i in directory:
        list_date[datetime.fromtimestamp(os.path.getctime(i)).strftime('%d-%m-%y')] = i
        #list_date[i] = os.path.getctime(i)
    #print(sorted(list_date.items()))
    return sorted(list_date.items())

dir_size = {} 
def BySize(directory):
    for i in directory:
        dir_size[os.path.getsize(i)] = i
    #print(sorted(dir_size.items()))
    return sorted(dir_size.items())   
#print(dir_size)
#BySize(dir_list)

dir_ext = {} 
def ByType(directory):
    for i in directory:
        file_extension = pathlib.Path(i).suffix
        dir_ext[i] = file_extension
    sortedVal = {k: v for k, v in sorted(dir_ext.items(), key= lambda v: v[1])}
    #print(sortedVal)
    return sortedVal
'''   
#Part 2 Choose sorting strategy:
choice = input('Choose a number to sort by:\n1. Name\n2. Last Modified Date\n3. Size\n4. Type\n')
#print(type(choice)) --> string 
#defining functions names in dictionary 
choose = {'1':ByName,'2':ByLastModified,'3':BySize,'4':ByType}
#calling function by adding () to the dictname[key]() => choose[1]() => ByName()
final = choose[choice](dir_list) 
print("-----------SORTED LIST------------------")
print(final)
'''

cont = 'y'
while cont == 'y':
    choice = input('Choose a number to sort by:\n1. Name\n2. Last Modified Date\n3. Size\n4. Type\n')
    choose = {'1':ByName,'2':ByLastModified,'3':BySize,'4':ByType}
    final = choose[choice](dir_list) 
    print("-----------SORTED LIST------------------")
    print(final)
    cont = input('Do you want to continue y or n:')
