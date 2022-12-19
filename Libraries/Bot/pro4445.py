def expanding(l=[]):
    res=[]
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            res.append(l[i]-l[i + 1])
        else:
            res.append(l[i + 1] - l[i])


    for k in range(len(res)-1):
        if res[k]<res[k+1]:
            pass
        else:
            return False

    return True




def accordian(l=[]):
    d=[]
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            d.append(l[i]-l[i + 1])
        else:
            d.append(l[i + 1] - l[i])


    for v in range(len(d)-1):
        if d[v]==d[v+1]:
            return False
            break



        if d[v]>d[v+1]:
            if d[v+1]<d[v+2]:
                if d[v+2]>d[v+3]:
                    return True
                    break

        if d[v]<d[v+1]:
            if d[v+1]>d[v+2]:
                if d[v+2]<d[v+3]:
                    if d[v+3]>d[v+4]:
                        return True
                        break


        if d[v]<d[v+1]:
            if d[v+1]>d[v+2]:
                if d[v+2]<d[v+3]:
                    if d[v+3]<d[v+4]:
                        return True
                        break












expanding([1,3,7,2,9])
expanding([1,3,7,2,-3])
expanding([1,3,7,10])


accordian([1,5,1])
accordian([1,5,2,8,3])
accordian([-2,1,5,2,8,3])
accordian([-2,1,5,2,8,1])
