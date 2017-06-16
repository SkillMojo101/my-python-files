##this is a file renamer script that I made to create a certain naming
##convention for sequenced files, namely rendered sequence images.
##A simple GUI is yet to be added for it with more options for the user.

import glob2, os

namer = 0
formatter = '0'
numOfFiles = 0
decimals = 0

for num in range (0, len(glob2.glob("*.txt"))):
    numOfFiles += 1

while (numOfFiles > 0):    
    decimals +=1
    numOfFiles /= 10

formatter += str(decimals)

try:

    for file in glob2.glob("*.txt"):
        os.rename(file, (str(format(namer, formatter))+".txt"))
        namer += 1
        
except:
    print "FAILED: Duplicate Files"
    os.system("pause")
