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
# import load_workbook
#from openpyxl import load_workbook
#import subprocess

for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       #print(dirname + "\n")
       if filename.endswith('.cc') :
            thefile = os.path.join(dirname,filename)
                        
            #fin = open(thefile, 'rb')      
            string1 = re.search(r"[a-zA-Z]+",filename)
            print(string1.group(0))

            cppcmd1 = "mkdir ../sorted_dirs/"+string1.group(0)
            os.system(cppcmd1)
            cppcmd2 = "mv "+string1.group(0)+"_*.*"+" ../sorted_dirs/"+string1.group(0)+"/."
            os.system(cppcmd2)




           

           
