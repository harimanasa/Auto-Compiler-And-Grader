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
import shutil

for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.cc') :
            thefile = os.path.join(dirname,filename)
            test_string = filename            

            object_name = test_string.replace(".cc",".o")
  
            #cppcmd0 = "gcc -c "+dirname+"/Main.cpp "+ thefile +" >> compiletest.txt"
            cppcmd0 = "g++ -c "+dirname+"/Main.cpp "+ thefile +" >> compiletest.txt"
            os.system(cppcmd0)
            cppcmd1 = "g++ Main.o "+object_name +" >> compiler_log.txt" 
            os.system(cppcmd1)

            cppcmd2 = "./a.out >> "+dirname+"/"+dirname+"_output.txt"
            os.system(cppcmd2)
            #cppcmd3 = "echo \" \"; echo \" ====================== \" " + "\n "+ filename + "\n >> Finaloutputresults.txt "
            cppcmd3 = "echo \" \"; echo \" ====================== \" >> Finaloutputresults.txt "
            os.system(cppcmd3)
            cppcmd4 = "ls " + thefile + " >> Finaloutputresults.txt"
            os.system(cppcmd4)
            cppcmd5 = "diff ideal.txt "+dirname+"/"+dirname+"_output.txt >> Finaloutputresults.txt"
            os.system(cppcmd5)
            
            os.remove('./a.out')
            print("File a.out removed")




            
