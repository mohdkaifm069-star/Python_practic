st=input("enter words: ")
words=""
largest=""
for i in range(len(st)):
        if st[i]!=" ":
                words+=st[i]
        else:
                if len(words)>len(largest):
                        largest=words
                words=""
if len(words)>len(largest):
        largest=words

print("largest word:",largest)
print("length",len(largest))
        
        
