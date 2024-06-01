def compress(chars) -> int:
    s = ""
    count = 1
    for i in range(len(chars)):
        if chars[i] not in s:
            if(count!=1):
                s = s + str(count)
            s = s + str(chars[i])
            count = 1
        else:
            count += 1
    s=s+str(count)
    chars=list(s)
    print(chars)
    return len(s)
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))