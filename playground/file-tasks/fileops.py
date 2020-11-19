lineMessage = "Printing Entire File"
print(lineMessage)
print("-" * len(lineMessage))
with open('test.txt') as file_object:
    #contents = file_object.readlines()
    contents = file_object.read()
    print(contents)

print("\n")
lineMessage = "Printing Entire File Line by Line"
print(lineMessage)
print("-" * len(lineMessage))
with open('test.txt') as file_object:
    line_num = 1
    for line in file_object:
        print("{} {}".format(line_num,line.rstrip()))
        line_num += 1


# Write to file
try:
    with open('drive-spces.txt', 'r') as file_object:
        file_object.write("This is output from df command\n")
except:
    print("File Issues")
