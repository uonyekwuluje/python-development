# Python Tips and Cheetsheet

### Convert a string to a list
```
s = "sdmfjrt"
sList = [xter for xter in s]
```

### Convert a List to a string
```
s = ''.join(sList)
```

### Break String into equal chunks
```
str = 'CarBadBoxNumKeyValRayCppSan'
n = 3
chunks = [str[i:i+n] for i in range(0, len(str), n)]
print(chunks)
```

### Reversing a string
```
strInput = 'CarBadBoxNumKeyValRayCppSan'
print(strInput[::-1])
```
