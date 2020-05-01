from math import sqrt
labirint = open('labirint.txt','r')
lab = []
for lines in labirint:
    lab.append([lines])
for i in range(len(lab)):
    for el in lab[i][0]:
        if el != '\n' :
            lab[i].append(el)
    del lab[i][0]
n,m = map(int, input("Введите индексы старта").split())
k,l = map(int, input("Введите индексы финиша").split())
lab[n][m],lab[k][l] = 0,1
for line in lab:
    print()
    for el in line:
        print(el,end=' ')

def h(j2,j1,i2,i1):
    return sqrt((j2-j1)**2+(i2-i1)**2)


