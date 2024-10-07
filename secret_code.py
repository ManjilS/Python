coding =input("Do you want to encode or decode: ")
str=input("Enter message : ")
words=str.split(" ")
# print(words)
if(coding.lower()=='encode'):
    encoding=[]
    for word in words:
        if len(word)>=3:
            r1='hdg'
            r2='iru'
            nstr=r1 + word[1:] + word[0] + r2
            encoding.append(nstr)
        else:
            encoding.append(word[::-1])
    print(" ".join(encoding))
else:
    encoding=[]
    for word in words:
        if len(word)>=3:
            nstr=word[3:-3]
            nstr=nstr[-1]+nstr[:-1]
            encoding.append(nstr)
        else:
            encoding.append(word[::-1])
    print(" ".join(encoding))