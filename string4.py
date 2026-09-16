st=input("enter string:")
for i in range(len(st)):
        count=0
        for j in range(len(st)):
                if st[i]==st[j]:
                        count+=1
        if st[i] not in st[:i]:
                print(st[i],"=",count,end=" ")
                
                
                        
                        
                
        



        
        


        