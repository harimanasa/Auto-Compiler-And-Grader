import pandas as pd
import os
from os.path import join
from pandas import ExcelWriter
import fileinput
import sys
import string
import re
import gzip
import numpy as np
import sys

for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.h') :
            thefile = os.path.join(dirname,filename)             
            string0 = re.search(r"[a-zA-Z0-9]+",filename)
            split_string_list = filename.split("_")
            file_end = "\.h"
            string1 = [x for x in split_string_list if re.search(file_end,x)]
            string2 = ''.join(string1)
            #print (string0.group(0))            
            string2 = re.sub(r"\-[0-9]","",string2)
            print (string2)
           
            cppcmd1 = "cp "+string0.group(0)+"/"+filename+" "+string0.group(0)+"/"+string2
            os.system(cppcmd1)




           

           
