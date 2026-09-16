name=input("Enter to sting:")
reverse=""
for i in range(len(name)-1,-1,-1):
        reverse+=name[i]
if name==reverse:
        print("palindrome")
else:
        print("not palindrome")



                        
                

                