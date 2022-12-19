
def frequency(l=[]):
    freq = {}
    for item in l:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    mx = max(freq.items(),key = lambda x:x[1])
    maxi =[i[0] for i in freq.items() if i[1]==mx[1]]

    mn = min(freq.items(),key = lambda x:x[1])
    mini =[i[0] for i in freq.items() if i[1]==mn[1]]
    tup=(mini,maxi)
    return tup

############ALTERNATIVE###########################
def frequency(l):
    unique_l = list(set(l))
    freq_list = [l.count(x) for x in unique_l]
    min_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == min(freq_list)]
    max_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == max(freq_list)]
    min_freq_list.sort()
    max_freq_list.sort()
    return (min_freq_list, max_freq_list)


frequency([13,12,11,13,14,13,7,11,13,14,12])
#([7], [13])

frequency([13,12,11,13,14,13,7,11,13,14,12,14,14])
#([7], [13, 14])

frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7])
#([7, 11, 12], [13, 14])