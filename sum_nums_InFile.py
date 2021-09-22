import re
file_name = input('Enter file name: ')
if len(file_name) < 1: file_name = 'C3_1.txt'

try:
    fop = open(file_name)
except:
    print('Non-existing file!')
    quit()

li = list()
#strip text and look for numbers
for lines in fop:
    line = lines.rstrip()
    data = re.findall('[0-9]+', line) #look for strings that contain numbers
    #print(data) # check if it works
    if len(data) == 0: #eliminate the blank spaces wich are lines without numbers
        continue
    #take every key from the list and convert it from string to integer
    #add the integers in li list
    for k in data:
        x = int(k)
        li.append(x)
#print(li)
#print sum of the extracted numbers
Sum = sum(li)
print(Sum)
