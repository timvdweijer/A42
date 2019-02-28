import numpy as np

# Read a file
f = open("CRJ700-19.inp","r") # Open file for reading
lines = f.readlines()
f.close()

a = []
d = np.zeros((3216,5))

for i in range(3206,6422):
    print(lines[i])
    a.append(lines[i])

for j in range(len(a)):
    b = (a[j].split(','))
    for i in range(len(b)):
        d[j][i] = (float(b[i]))

print(d)
