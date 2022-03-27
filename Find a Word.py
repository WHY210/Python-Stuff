userinput1 = str(input("Enter your word:"))
userinput2 = str(input("Enter your text:"))

FindWord = userinput2.find(userinput1, 0, len(userinput2))

if FindWord != -1:
    print("Yes")
else: 
    print("No")
