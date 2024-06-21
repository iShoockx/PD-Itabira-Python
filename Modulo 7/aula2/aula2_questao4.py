senha = input("Digite sua senha: ")
a=0
if len(senha)>=8:
    for i in senha:
        if a == 0:
            if 65<=ord(i)<=90:
                a=1
        if a == 1:
            if 97<=ord(i)<=122:
                a=2
        if a == 2:
            if 48<=ord(i)<=57:
                a=3
        if a == 3:
            if 33<=ord(i)<=47 or 58<=ord(i)<=64 or 91<=ord(i)<=96 or 123<=ord(i)<=127:
                a = 4

if a==4:
    print(True)
else:
    print(False)
    