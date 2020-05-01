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


def neighbor(open, closed, arr, indexI, indexJ):
    neighborindex = []
    neighborindex.append([indexI - 1,indexJ])
    neighborindex.append([indexI + 1,indexJ])
    neighborindex.append([indexI,indexJ+1])
    neighborindex.append([indexI,indexJ-1])
    for i in range(len(neighborindex)):
        el = arr[neighborindex[i][0]][neighborindex[i][1]]
        if (el in open) or (el in closed) or (el=='x'):
            neighborindex[i] = 0
    while 0 in neighborindex:
        for el in neighborindex:
            if el == 0:
                del neighborindex[neighborindex.index(el)]
    return neighborindex


def h(j2,j1,i2,i1):
    return sqrt((j2-j1)**2+(i2-i1)**2)

