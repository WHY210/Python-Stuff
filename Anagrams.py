userinput = input("Enter two of your texts. Seperate with blank space.")

userinput = userinput.split()

sorted_userinput = []
sorted_userinput.append(sorted(userinput[0]))
sorted_userinput.append(sorted(userinput[1]))

if sorted_userinput[0] == sorted_userinput[1]:
    print("Anagrams")
else:
    print("Not Anagrams")
