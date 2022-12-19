#Question:- 1.Write a function intreverse(n) that takes as input a positive integer n and returns the integer
# obtained by reversing the digits in n.  Here are some examples of how your function should work.
#       >>> intreverse(783)
#       387
#       >>> intreverse(242789)
#       987242
#       >>> intreverse(3)
#       3

def intreverse(n):
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    return rev

#Question:- 2.Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")"
# in s are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it.
# Your function should ignore all other symbols that appear in s. Your function should return True if s has matched
# brackets and False if it does not.
#Here are some examples to show how your function should work.
#       >>> matched("zb%78")
#       True
#       >>> matched("(7)(a")
#       False
#       >>> matched("a)*(?")
#       False
#       >>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
#       True

def matched(s):
    p_list=[]
    for i in range(0,len(s)):
        if s[i] =='(':
            p_list.append('(')
        elif s[i] ==')' :
            if not p_list:
                return False
            else:
                p_list.pop()
    if not p_list:
        return True
    else:
        return False

#Question:-3.Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the
# prime numbers in l.Here are some examples to show how your function should work.
#       >>> sumprimes([3,3,1,13])
#       19
#       >>> sumprimes([2,4,6,9,11])
#       13
#       >>> sumprimes([-3,1,6])
#       0

def sumprimes(n):
    sum=0
    fact=[]
    for i in range (0,len(n)):
        num=n[i]
        if num>1:
            fact=[]
            for j in range (1,num+1):
                if num%j==0:
                    fact=fact+[j]
        if fact==[1,num]:
            sum=sum+num


    return sum