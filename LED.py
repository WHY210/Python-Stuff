zero = '''
###
# #
# #
# #
###
'''
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

list = [zero, one, two, three, four, five, six, seven, eight, nine]

checknumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
newlist = []

check = False
while(check != True):
    check = True
    userinput = input()
    for item in userinput:
        if item not in checknumbers:
            check = False
        else:
            newlist.append(list[int(item)].strip("\n").split("\n"))

newstring = ""

for j in range (5):
    for i in range(len(newlist)):
        newstring += (newlist[i][j] + " ")
    newstring += "\n"

print(newstring)



