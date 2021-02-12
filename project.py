word = input('Enter the word\n')
length = len(word)
middle_no = int(length/2) 
print(word[int(length/2)])
ref = ''
j = 0
for i in range(0,length-1):
    if middle_no + i < length-1:
        print(word[middle_no:middle_no+i+2])
        ref = word[middle_no:middle_no+i+2]
    else:
        ref += word[j]
        j += 1
        print(ref)

