import random
v = []
ifm,tfm = 0,0
ifa,tfa = 0,0
for i in range(20):
    v.append(random.randint(-10,10))

for i in range(len(v)):
    if v[i] < 0:
        tfa+=1
        if tfa == 1:
            ifa = i
    else:
        if tfa > tfm:
            tfm = tfa 
            ifm = ifa
        tfa = 0
print(v)
print(tfm,ifm)
del v[ifm:ifm+tfm]
print(v)

    
