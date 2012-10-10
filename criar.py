from wx._misc import Sleep
import os
Sleep(10)
for raiz,diretorios,arquivos in os.walk('/home/jato/python'):
    for arquivo in arquivos:
        if arquivo.endswith('.txt'):
            os.remove(os.path.join(raiz,arquivo))

f = open("/home/jato/python/lol.txt","a+")
Sleep(10)
os.remove("/home/jato/python/lol.txt")