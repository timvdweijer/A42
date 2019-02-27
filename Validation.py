# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 09:01:22 2019

@author: Harold
"""
# Read a file
f = open("CRJ700-19.inp","r") # Open file for reading
lines = f.readlines()
f.close()

# Check every line in the list lines
for line in lines:
# Make case-tolerant: make lower case
    txt = line.lower()
# Check for comment line or a blank line
    if txt[0]='*' and not txt.strip()=="":
        words = txt.split("=")
        label = words[0].strip() # remove spaces at the start
        value = words[1].strip() # and end of string
# Lots of checks for “[ ]” and “\n” at end of line
        i = value.find('[')
        if i>=0:
            value = value[:i]
        else:
            if value[-2:]=="\n":
                value = value[:-2]
# if a value is given: read it
        if value=="":
            x=float(value)
            print (label," = ",x)
            nlist.append([label,x])