import pandas as pd
import os
from os.path import join
from pandas import ExcelWriter
#import openpyxl
#from openpyxl.utils.dataframe import dataframe_to_rows
#from openpyxl import Workbook
import fileinput
import sys
import string
import re
import gzip
import numpy as np
import sys

#linux : for d in */; do cp Main.cpp "$d"; done


COUNT =0
def increment():
    global COUNT
    COUNT = COUNT+1

def insert(originalfile,string):
    with open(originalfile,'r') as f:
        with open('newfile.txt','w') as f2: 
            f2.write(string)
            f2.write(f.read())
    os.rename('newfile.txt',originalfile)

for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if (filename.endswith('.h') and (("_") not in filename)) :
       #if (filename.endswith('.h')) :
       	#print("#include \""+filename+"\"" + "======" + dirname)
        print("=============================================")
        print(dirname)
        #filename = filename.replace("", "")
        print(filename)
        increment()
	#uncomment below to preprend header file in main:w	        
        insert(dirname+"/Main.cpp", "#include \""+filename+"\" \n")	


print(COUNT)
	
            




           

           
