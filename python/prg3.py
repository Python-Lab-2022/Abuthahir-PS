string=input("enter the string:")
string=string.lower()
string=string.split(" ")
word_frequency={}
for i in string:
    if i in word_frequency:
        word_frequency[i]+=1
    else:
        word_frequency[i]=1
print(word_frequency)

  
