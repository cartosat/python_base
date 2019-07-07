

f=open('pic.jpg','rb')

f2=open('pic2.txt','wb')

for data in f:
    f2.write(data)

f2=open('pic2.txt','rb')
f3=open('pic3.jpg','wb')

for data in f2:
    f3.write(data)


