# Q: Check if given no is Strong Number or not

# strong no is one which has sum of factorial of each digit equal to no itself.
# eg 145 --> 1! + 4! + 5! --> 145
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

num = 145
sum = 0
temp = num
while temp>0:
    ld = temp%10
    sum += fact(ld)
    temp = temp//10

if num == sum:
    print("It is strong No")
else:
    print("Not a strong no")

