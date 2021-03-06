#!/usr/bin/env python
#-*- encoding:utf-8 -*-

"""
Refactor Inventory
------------------

The following code represents a working solution to the inventory exercise,
with two additional features:

1. Log files are read in from disk
2. The resulting data structure is printed

Refactor this script into separate functions that can be called to process log
files and print out the final total for each part (you should end up with 4-6
functions). Keep an eye out for the following code smells:

1. Repeated code -> turn it into a single function
2. Inline comments -> turn them into names
3. Bad names -> object names should clearly describe what they do
4. Magic numbers -> replace them with named constants
5. Global objects -> encapsulate them inside functions
6. Temporal coupling -> separate ordered steps into a main block or function
"""

# Import statements
from glob import glob
from io import open
import os


def findAdditionalFiles():

    root=os.path.dirname(__file__)
    log_files=glob(os.path.join(root,'data', '*.log'))
    return log_files   
    
    

def readInventory(log_file):
     
    transactions = []           
    with open(log_file, 'r', encoding='utf-8') as f:
        read_log_file = f.read()    
    for line in read_log_file.strip().splitlines(): # split string on lines
        if len(line.split()) != 2: 
            warning="{} is not valid".format(line)
            print(warning)
        else: 
            part, count_str= line.split()
            transactions.append([part, int(count_str)]) # append line
    return transactions
    
          
    
def displayWarehouseLog(warehouse_log_dict, column_width=10): 
    template = "{name:^{w}.{w}s}|{number:^{w}.{w}s}"
    
    log_output='\n'+template.format(w=column_width,name="Part Name", number="Count")+'\n'+'|'.join(['-' * 10] * 2)
    for part_name, count in warehouse_log_dict.items():
        log_output+="\n"+template.format(w=column_width, name=part_name, number=str(count)) 
    log_output+="\n"

    print(log_output)
    
def updateWarehouseLog():
    transactions = []
    warehouse_log_dict = {}
     
    for log_file in findAdditionalFiles():
        transactions.extend(readInventory(log_file))
        
    for transaction in transactions:
        warehouse_log_dict[transaction[0]] = warehouse_log_dict.get(transaction[0], 0) + transaction[1] # increment 
    
    displayWarehouseLog(warehouse_log_dict)

    
updateWarehouseLog()



             
        


    

    
