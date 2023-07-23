string = str(input("Pls enter the string: "))
l1=list(string)
freq={}
def most_frequent(freq):
    print(freq)
for i in l1:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1


most_frequent(freq)    
