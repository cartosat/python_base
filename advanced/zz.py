def isValid(s):
    dict_ = {
        ')' : '(',
        ']' : '[',
        '}' : '{'

    }
    lis = []
    for i in s1:
        if i == '(' or i == '[' or i == '{':
            lis.append(i)
        else:
            print(i, dict_[i], lis)
            try:
                lis.remove(dict_[i])
            except:
                return False
    return True

s = "()[]{}"
s1 = "(]"
print(isValid(s))