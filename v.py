import numpy as np

# Read a file
f = open("CRJ700_SLC1.rpt","r") # Open file for reading
lines = f.readlines()
f.close()

for line in lines:
    print(line)
