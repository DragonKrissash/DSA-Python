def isSubstring(word1,word2):
    for i in range(len(word1)):
        if word2==(word1[i:]+word1[:i]):
            return True
        
    return False

word1=input('Enter word 1: ')
word2=input('Enter word 2: ')
print(isSubstring(word1,word2))
# print(word1[3:]+word1[:3])