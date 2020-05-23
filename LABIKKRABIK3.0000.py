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
n,m = map(int, input("Введите индексы старта:").split())
k,l = map(int, input("Введите индексы финиша:").split())
lab[n][m],lab[k][l] = 0,2


def neighbor(closed, arr, indexI, indexJ):
    neighborindex = []
    if (indexI == 0):
        neighborindex.append([indexI + 1, indexJ])
        neighborindex.append([indexI, indexJ + 1])
        neighborindex.append([indexI, indexJ - 1])
    elif (indexI == len(arr)-1):
        neighborindex.append([indexI - 1, indexJ])
        neighborindex.append([indexI, indexJ + 1])
        neighborindex.append([indexI, indexJ - 1])
    elif (indexJ == 0):
        neighborindex.append([indexI - 1, indexJ])
        neighborindex.append([indexI + 1, indexJ])
        neighborindex.append([indexI, indexJ + 1])
    elif (indexJ == len(arr))-1:
        neighborindex.append([indexI - 1, indexJ])
        neighborindex.append([indexI + 1, indexJ])
        neighborindex.append([indexI, indexJ - 1])
    else:
        neighborindex.append([indexI - 1, indexJ])
        neighborindex.append([indexI + 1, indexJ])
        neighborindex.append([indexI, indexJ + 1])
        neighborindex.append([indexI, indexJ - 1])
    for i in range(len(neighborindex)):
        el = arr[neighborindex[i][0]][neighborindex[i][1]]
        if  ([neighborindex[i][0],neighborindex[i][1]] in closed):
            neighborindex[i] = 0
    while 0 in neighborindex:
        for el in neighborindex:
            if el == 0:
                del neighborindex[neighborindex.index(el)]
    return neighborindex


def h(j2,j1,i2,i1):
    return sqrt((j2-j1)**2+(i2-i1)**2)

def back_Up(closed,lab,pathi):
    for i in range(len(closed)):
        neib = neighbor(closed,lab,closed[len(closed)-i-1][0],closed[len(closed)-i-1][1])
        pathi[closed[len(closed)-i-1][0]][closed[len(closed)-i-1][1]] = ' '
        if len(neib)==0:
            pass
        else:
            return [closed[len(closed)-i-1][0],closed[len(closed)-i-1][1]]
def minf(fmatr,gmatr,indI,indJ,closed,cur,pathi):
    f_arr = []
    neib = neighbor(closed,lab,cur[0],cur[1])
    if len(neib)==1:
        gmatr[neib[0][0]][neib[0][1]] = gmatr[cur[0]][cur[1]] + 1
        fmatr[neib[0][0]][neib[0][1]] = gmatr[neib[0][0]][neib[0][1]] + h(indI, neib[0][0], indJ, neib[0][1])
        indexI = neib[0][0]
        indexJ = neib[0][1]
        pathi[indexI][indexJ] = 1
        return [indexI, indexJ]
    elif len(neib)>1:
        for neibhor in neib:
            if lab[neibhor[0]][neibhor[1]] == 'x':
                gmatr[neibhor[0]][neibhor[1]] = gmatr[cur[0]][cur[1]] + 5
                fmatr[neibhor[0]][neibhor[1]] = gmatr[neibhor[0]][neibhor[1]] + h(indI, neibhor[0], indJ, neibhor[1])
                f_arr.append(fmatr[neibhor[0]][neibhor[1]])
            else:
                gmatr[neibhor[0]][neibhor[1]] = gmatr[cur[0]][cur[1]] + 1
                fmatr[neibhor[0]][neibhor[1]] = gmatr[neibhor[0]][neibhor[1]] + h(indI, neibhor[0], indJ, neibhor[1])
                f_arr.append(fmatr[neibhor[0]][neibhor[1]])
        el = min(f_arr)
        for i in range(len(fmatr)):
            for j in range(len(fmatr[i])):
                if fmatr[i][j] == el and [i,j] != cur:
                    indexI = i
                    indexJ = j
                    break
        pathi[indexI][indexJ] = 1
        return [indexI, indexJ]
    elif len(neib)==0:
        pathi[cur[0]][cur[1]] = " "
        curent = back_Up(closed,lab,pathi)
        pathi[curent[0]][curent[1]]=1
        return curent


def AZIRKA(indIstart,indJstart,indIend,indJend,labirint):
    closed=[]
    open=[[indIstart,indJstart]]
    path = labirint
    g = [[0 for i in range(len(lab))] for j in range(len(lab))]
    g[indIstart][indJstart] = 0
    f = [[0 for i in range(len(lab))] for j in range(len(lab))]
    f_arr = []
    f[indIstart][indJstart] = h(indJend, indJstart, indIend, indIstart)
    curr=[indIstart, indJstart]
    goal=[indIend,indJend]
    while open:
        if curr == goal:
            path[curr[0]][curr[1]] = 2
            for line in path:
                print()
                for el in line:
                    print(el, end=' ')
            break
        curr = minf(f,g,indIend,indJend,closed,curr,path)
        open.append(curr)
        closed.append(open[0])
        del open[0]
AZIRKA(n,m,k,l,lab)