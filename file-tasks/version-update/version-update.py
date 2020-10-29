#!/usr/bin/python
import os,re
from random import randint

# Function to Generate Random Number set
def random_with_N_digits():
    n = 5
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


findString = "AssemblyVersion"
baseVersion = ""

with open("Version.cs") as inFile:
    #original_version = infile.read()
    for line in inFile:
       if findString in line:
           baseVersion = line.strip("\n")

# Retrieve version and strip spaces and quotes
print("The Base Line => {}".format(baseVersion))
semVer = re.search(r'\((.*?)\)',baseVersion).group(1).replace('"',"").replace(' ',"") 
print("Version = {}".format(semVer))

versionSplitList = semVer.split('.')
print(versionSplitList)
print("The List is Lenght => {}".format(len(versionSplitList)))

# Substitute last index with build number
versionSplitList[-1] = random_with_N_digits()
print(versionSplitList)

# Convert versionSplitList back to string
seperator = "."
newSemVer = seperator.join([str(item) for item in versionSplitList])
print("New Version => {}".format(newSemVer))

# Update Version In Version.cs
tmpVersionFile = open("Version.cs", "rt") 
fileContent = tmpVersionFile.read()
fileContent = fileContent.replace(semVer, newSemVer)
tmpVersionFile.close()

newVersionFile = open("Version2.cs", "wt")
newVersionFile.write(fileContent)
newVersionFile.close()
