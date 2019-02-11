import os
import glob
import re
from pprint import pprint
with open('TableNames.txt', 'r') as f:
 myNames = [line.strip() for line in f]
 for root, dirs, files in os.walk('C:/Users/Yuge/Desktop/aspoutput/'):
     for filename in files:
         if filename.endswith(".asp"):   
             inputfile = os.path.join(root, filename)       
             destinationpath = os.path.join(root, filename)
             print('Conversion is ongoing for:'+inputfile)
             with open(inputfile,'r') as inputfile:
                    filedata = inputfile.read()
                    i=0
                    while i < 280:
                             x=myNames[i]
                             i=i+1
                             pattern = re.compile('FROM '+x, re.IGNORECASE)
                             filedata = pattern.sub('FROM '+x.lower(), filedata)
             with open(destinationpath,'w') as filename:
                     filename.write(filedata)

#Notes: Since classic asp isn't case sensitive, our developers accidently wrote names in both upper case and lower case randomly in asp files. 
#Case sensitivity of database table names could be different under different operating systems.
#So the purpose of this script file is to make all tablenames lowercase in the asp files. 