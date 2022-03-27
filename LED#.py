zero = """
###
# #
# #
# #
###
"""
one = '''
  #
  #
  #
  #
  #
'''
two = '''
###
  #
###
#  
###
'''
three = '''
###
  #
###
  #
###
'''
four = '''
# #
# #
###
  #
  #
'''
five = '''
###
#  
###
  #
###
'''
six = '''
###
#  
###
# #
###
'''
seven = '''
###
  #
  #
  #
  #
'''

eight = '''
###
# #
###
# #
###
'''
nine = '''
###
# #
###
  #
###
'''
strNumbers = [zero, one, two, three, four, five, six, seven, eight, nine]
checkNumbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

check = False
while(check != True):
    check = True
    userInput = input("Enter numbers: ")
    for item in userInput:
        if item not in checkNumbers:
            check = False
strList = []
for i in userInput:
    if i == '0':
        strList.append(strNumbers[0].strip('\n').split('\n'))
    elif i == '1':
        strList.append(strNumbers[1].strip('\n').split('\n'))
    elif i == '2':
        strList.append(strNumbers[2].strip('\n').split('\n'))
    elif i == '3':
        strList.append(strNumbers[3].strip('\n').split('\n'))
    elif i == '4':
        strList.append(strNumbers[4].strip('\n').split('\n'))
    elif i == '5':
        strList.append(strNumbers[5].strip('\n').split('\n'))
    elif i == '6':
        strList.append(strNumbers[6].strip('\n').split('\n'))
    elif i == '7':
        strList.append(strNumbers[7].strip('\n').split('\n'))
    elif i == '8':
        strList.append(strNumbers[8].strip('\n').split('\n'))
    elif i == '9':
        strList.append(strNumbers[9].strip('\n').split('\n'))

newStr = ''
for i in range(5):
    for j in range(len(strList)):
        newStr += (strList[j][i] + ' ')
    newStr += '\n'

print(newStr)