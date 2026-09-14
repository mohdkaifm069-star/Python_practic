arr=[10,50,30,34,78,56,90]
g=arr[0]
sg=arr[0]
tg=arr[0]
for i in range(len(arr)):
        if arr[i]>g:
                tg=sg
                sg=g
                g=arr[i]
        elif arr[i]>sg and arr[i]!=g:
                tg=sg
                sg=arr[i]
               
        
        elif arr[i]>tg and arr[i]!=sg and arr[i]!=g:
                tg=arr[i]
print("greatest=",g)
print("second greatest=",sg)
print("third greatest=",tg)
        



        