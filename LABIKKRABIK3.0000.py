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
lab[n][m],lab[k][l] = 0,1


def neighbor(open, closed, arr, indexI, indexJ):
    neighborindex = []
    neighborindex.append([indexI - 1,indexJ])
    neighborindex.append([indexI + 1,indexJ])
    neighborindex.append([indexI,indexJ+1])
    neighborindex.append([indexI,indexJ-1])
    for i in range(len(neighborindex)):
        el = arr[neighborindex[i][0]][neighborindex[i][1]]
        if  ([neighborindex[i][0],neighborindex[i][1]] in closed) or (isinstance(el, str)==True and el != ' '):
            neighborindex[i] = 0
    while 0 in neighborindex:
        for el in neighborindex:
            if el == 0:
                del neighborindex[neighborindex.index(el)]
    return neighborindex


def h(j2,j1,i2,i1):
    return sqrt((j2-j1)**2+(i2-i1)**2)


def minf(fmatr,gmatr,neib,indI,indJ,closed,cur):
    f_arr = []
    if len(neib)==1:
        gmatr[neib[0][0]][neib[0][1]] = gmatr[cur[0]][cur[1]] + 1
        fmatr[neib[0][0]][neib[0][1]] = gmatr[neib[0][0]][neib[0][1]] + h(indI, neib[0][0], indJ, neib[0][1])
        indexI = neib[0][0]
        indexJ = neib[0][1]
    else:
        for neibhor in neib:
            gmatr[neibhor[0]][neibhor[1]] = gmatr[cur[0]][cur[1]] + 1
            fmatr[neibhor[0]][neibhor[1]] = gmatr[neibhor[0]][neibhor[1]] + h(indI, neibhor[0], indJ, neibhor[1])
            f_arr.append(fmatr[neibhor[0]][neibhor[1]])
        el = min(f_arr)
        for i in range(len(fmatr)):
            for j in range(len(fmatr[i])):
                if fmatr[i][j] == el:
                    indexI = i
                    indexJ = j
        for neibhor in neib:
            if neibhor != [indexI, indexJ]:
                closed.append(neibhor)
    return [indexI,indexJ]


def AZIRKA(indIstart,indJstart,indIend,indJend,labirint):
    closed=[]
    open=[[indIstart,indJstart]]
    g = [[0 for i in range(len(lab))] for j in range(len(lab))]
    g[indIstart][indJstart] = 0
    f = [[0 for i in range(len(lab))] for j in range(len(lab))]
    f_arr = []
    count = 0
    f[indIstart][indJstart] = h(indJend, indJstart, indIend, indIstart)
    curr=[indIstart, indJstart]
    goal=[indIend,indJend]
    while open:
        if curr == goal:
            labirint[goal[0]][goal[1]] = chr(87+count)
            for line in labirint:
                print()
                for el in line:
                    print(el, end=' ')
            break
        neibh = neighbor(open,closed,labirint,curr[0],curr[1])
        curr = minf(f,g,neibh,indIend,indJend,closed,curr)
        open.append(curr)
        closed.append(open[0])
        del open[0]
        if count<9:
            labirint[curr[0]][curr[1]] = chr(49+count)
        else:
            labirint[curr[0]][curr[1]] = chr(88+count)
        count+=1


AZIRKA(n,m,k,l,lab)





