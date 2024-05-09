val={
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15
}
word=input()
num=0
for i in range(len(word)):
    c=word[len(word)-1-i]
    if c in val.keys():
        num=num+val[c]*pow(16,i)
    else:
        c=int(c)
        num=num+c*pow(16,i)
print(num)