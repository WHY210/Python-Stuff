from os import strerror
import sys

data = bytearray(100)

for i in range(len(data)):
    data[i] = 65 + i


try:
    #{'a':3, 'b':2, 'c':1}
    file = 'src.txt'
    src = open(file, 'rt', encoding = 'utf-8')
    dest = open(file, 'rt', encoding = 'utf-8')
    dct = {}
    ch = src.read(1)
    while ch != '':
        if ch in dct: dct[ch] += 1
        else: dct[ch] = 1
        ch = src.read(1)
    print(dct)
    sorted()
    for k,v in dct.items():
        dest.write(k + '->' +str(v) + '\n')

    src.close()
    dest.close()
    print(sorted({'a':1, 'b':2, 'c':3}, reverse=True))



    dest = open(file[:-3] + 'hist', 'wt', encoding = 'utf-8')
    dct = {}
    ch = src.read(1)
    while ch != '':
        if ch in dct: dct[ch] += 1
        else: dct[ch] = 1
        ch = src.read(1)
    print(dct)
    dct = sorted()
    for k,v in dct.items():
        dest.write(k +'->' + str(v) + '\n')

    src.close()
    dest.close()
    print(sorted({'a':1, 'b':2, 'c':3}, reverse = True))

except IOError as e:
    print("I/O error occured:", strerror(e.errno))