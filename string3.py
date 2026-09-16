st=input("enter to string:")
vow=0
cons=0
for i in range(len(st)):
        if st[i]=="a" or st[i]=="e" or st[i]=="i" or st[i]=="o" or st[i]=="u":
                vow+=1
        else:
                cons+=1
print("vowels",vow)
print("consonants",cons)
       
        
               


