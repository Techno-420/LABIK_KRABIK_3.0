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


'''
def min_f(open):
    
    ці дві функції доробить
    
def reconstruct_path(cameFrom, current)
'''

def AZIRKA(indIstart,indJstart,indIend,indJend):
    closed=[]
    open=[[indIstart,indJstart]]
    matrixfrom = [[0 for i in range(len(lab))] for j in range(len(lab))]
    g = [['inf' for i in range(len(lab))] for j in range(len(lab))]
    g[indIstart][indJstart]=0
    f=[[True for i in range(len(lab))] for j in range(len(lab))]
    f[indIstart][indJstart] = h(indJend, indJstart, indIend, indIstart)
    for i in matrixfrom:
        print()
        for j in i:
            print('%3s'%j, end=' ')
    for i in g:
        print()
        for j in i:
            print('%3s'%j, end=' ')
    for i in f:
        print()
        for j in i:
            print('%0.2f'%j, end=' ')
    curr=min_f(open)                                     ##min_f(open) треба зробить
    goal=[indIend,indJend]
    while open:
        if curr==goal:
            return reconstruct_path(cameFrom, current)   ##reconstruct_path(cameFrom, current) треба зробить

        del open[open.index(curr)]
        for neighbour in neighbor(open, closed, lab, curr[0], curr[1]):
            temp_g=g[curr[0]][curr[1]]+1
            if neighbour not in open or temp_g<g[neighbour[0]][neighbour[1]]:
                matrixfrom[neighbour[0]][neighbour[1]]=curr
                g[neighbour[0]][neighbour[1]]=temp_g
                f[neighbour[0]][neighbour[1]]=g[neighbour[0]][neighbour[1]]+h(indJend,neighbour[1],indIend,neighbour[0])
                if neighbour not in open:
                    open.append(neighbour)

AZIRKA(6,1,1,6,)