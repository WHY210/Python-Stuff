from os import strerror
srcname = input("Open a file: ")
dstname = input("Select a dst file: ")
try:
    src = open(srcname, 'rt')
    dst = open(dstname, 'wt')
except IOError as e:
    print("Cannot open the file: ",strerror(e.errno))
    
alpha = 'abcdefghijklmnopqrstuvwxyz'
dataDict ={}
for letter in alpha:
    dataDict.update({letter:0})
    
data = src.read().strip()
data2 = data.lower()

for ch in data2:
    if ch.isalpha():
        temp = {ch:dataDict[ch]+1}
        dataDict.update(temp)

# ======================================================

valueList = list(dataDict.values())
valueList.sort()
sortedValue = list(filter(lambda x: x > 0, valueList))

acendValue = []
for i in range(0,len(sortedValue)):
    acendValue.append(sortedValue.pop())

for item in acendValue:
    for letter in list(dataDict.keys()):
        if dataDict[letter] == item:
            print(letter, ' -> ', item)
            newData = letter + ' -> ' + str(item) + '\n'
            dst.write(newData)
            del dataDict[letter]
            
src.close()
dst.close()