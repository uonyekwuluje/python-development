### Python-Exercises
This repository cointains python code for a myriad of things in python. I have comme across
concepts in books, blogs, journals, discussions etc. The truth is that knowledge is scattered 
everywere. <br>
Python Exercises helps me keep track of unique concepts that I seldom encounter and makes access
to them faster for me.

### Table of Contents ###
* [Tests in Python](/Testing/)


### Python Tips and Cheetsheet

# Convert a string to a list
```
s = "sdmfjrt"
sList = [xter for xter in s]
```

# Convert a List to a string
```
s = ''.join(sList)
```

# Break String into equal chunks
```
str = 'CarBadBoxNumKeyValRayCppSan'
n = 3
chunks = [str[i:i+n] for i in range(0, len(str), n)]
print(chunks)
```

# Reversing a string
```
strInput = 'CarBadBoxNumKeyValRayCppSan'
print(strInput[::-1])
```
