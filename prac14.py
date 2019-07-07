

f=open('pic.jpg','rb')
f1=open('pic3.jpg','wb')

for i in f:
    f1.write(i)
