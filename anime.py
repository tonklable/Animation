#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
from IPython.display import clear_output
imgs = [1000000000000000000000000001,
        1000000000000000000000000001,
        1000000000000000000000000001,
        1000000000000000000000000001,
        1000000000000000000000000001,
        1000055555000000000000000001,
        1000055155000000000000000001,
        1055555550000000000000000001,
        1005555000000000000000000001,
        1000550000000000000000000001]
imgs_ori = [1000000000000000000000000001,
        1000000000000000000000000001,
        1000000000000000000000000001,
        1000000000000000000000000001,
        1000000000000000000000000001,
        1000055555000000000000000001,
        1000055155000000000000000001,
        1055555550000000000000000001,
        1005555000000000000000000001,
        1000550000000000000000000001]


#power, class, copy
f=1
ff=0
fff=0
l=1
ll=0
cactus=[[27,1],[28,4]]

#set coordinates
print("Here is Mr.Dinosaur.\n")
for row in imgs:
    print(row)      # See the difference of indentation
put=int(input("Let's play with Mr.Dinosaur. I trust that Mr.Dinosaur can dodge your obstacles.\nWhich obstacle do you want to release?\n(1:cactus, 2:bird) "))
if put==1:
    printer="Release a cactus\n"
elif put==2:
    printer="Release a bird\n"
else:
    print("Oops. You took a wrong choice. Let's try again\n")
while put!=0:
    #coordinate=[[27,10]] #1<=x<=27, 1<=y<=10
    for x in range(31):
        if put==1:
            if x<25:
                frame=[[[26-x,1],[28-x,4]],[[25-x,3],[26-x,3]],[[28-x,2],[29-x,2]]]
            else:
                frame=[[]]
        elif put==2:
            if x<25:
                frame=[[[25-x,5],[26-x,5]],[[26-x,4],[30-x,5]],[[30-x,5],[31-x,5]]]
            elif x>=25 and x<=29:
                frame=[[[1,4],[30-x,5]],[[30-x,5],[31-x,5]]]
            elif x==30:
                frame=[[]]
            else:
                frame=[[]]
        if frame != [[]]:
            for c in frame:
                for i in range(27-c[0][0]):
                    f=f*10
                    ff=ff+f
                f=1
                for i in range(27-c[1][0]):
                    f=f*10
                    fff=fff+f
                f=1
                for h in range(10-c[1][1],11-c[0][1]):
                    imgs[h]=imgs[h]+ff-fff
                ff=0
                fff=0
        print(printer)
        for row in imgs:
            print(row)      # See the difference of indentation
        print()
        imgs = [1000000000000000000000000001,
        1000000000000000000000000001,
        1000000000000000000000000001,
        1000000000000000000000000001,
        1000000000000000000000000001,
        1000055555000000000000000001,
        1000055155000000000000000001,
        1055555550000000000000000001,
        1005555000000000000000000001,
        1000550000000000000000000001]
        if put==1:
            if x==15 or x==16 or x==24 or x==25:
                for u in range(10):
                    if u==8 or u==9:
                        imgs[u]=1000000000000000000000000001
                    else:
                        imgs[u]=imgs_ori[u+2]
            elif x==17 or x==23:
                for u in range(10):
                    if u==7 or u==8 or u==9:
                        imgs[u]=1000000000000000000000000001
                    else:
                        imgs[u]=imgs_ori[u+3]
            elif x==18 or x==19 or x==20 or x==21 or x==22:
                for u in range(10):
                    if u==6 or u==7 or u==8 or u==9:
                        imgs[u]=1000000000000000000000000001
                    else:
                        imgs[u]=imgs_ori[u+4]
        if put==2:
            if x>=15 and x<=24:
                imgs = [1000000000000000000000000001,
                    1000000000000000000000000001,
                    1000000000000000000000000001,
                    1000000000000000000000000001,
                    1000000000000000000000000001,
                    1000000000000000000000000001,
                    1000000000000000000000000001,
                    1055555555555000000000000001,
                    1005555555555000000000000001,
                    1000550000000000000000000001]


        time.sleep(0.05)     # in these two lines. It is important!
        clear_output(wait=True)
    put=int(input("See. Mr.Dinosaur could dodge easily.\nThe next obstacle is (1:cactus, 2:bird, 0:stop) "))
    if put==0:
        clear_output(wait=True)
        print("Thank you for playing. Mr.Dinosaur is taking a rest\n")
        imgs=[1000000000000000000000000001,
            1000000000000000000000000001,
            1000111111000000000000000001,
            1000011110000000000000222001,
            1000000000000000000000000001,
            1000000000000000000022000001,
            1000000000000000220000011001,
            1000000000000020000000111001,
            1005555555555000000000011101,
            1555555555155000000000011001]
        for row in imgs:
            print(row)      # See the difference of indentation
    elif put==1:
        printer="Release a cactus\n"
    elif put==2:
        printer="Release a bird\n"
    else:
        printer="Oops. You took a wrong choice. Let's try again\n"
    clear_output(wait=True)

