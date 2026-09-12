arr=[34,10,34,23,67,23,10,23,]
for i in range(len(arr)):
        count=0
        for j in range(i+1,len(arr)):
                if arr[i]==arr[j]:
                        count+=1
                        print("duplicate Value:",arr[i],count,"times")
       
                
                        

        
                
        
