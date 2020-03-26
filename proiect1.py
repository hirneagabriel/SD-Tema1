import random
import math

def verificare(v, arr):
    if len(v) != len(arr):
        return 0
    x = sorted(arr)
    for i in range(len(arr)):
        if v[i] != x[i]:
            return 0
    return 1

def CountSort(v):
    MAX = max(v)
    output = [0] * len(v)
    if MAX <= 10**10:
        n = len(v)
        j = 0
        vf = [0 for i in range(MAX+1)]
        for i in range(n):
            vf[v[i]] += 1
        for i in range(MAX+1):
            while vf[i] > 0:
                output[j] = i
                j += 1
                vf[i] -= 1
    return output

def CountSortRadix(vector, nrcifre, baza):
    lungime = len(vector)
    output = [0]*lungime
    vf = [0] * int(baza)
    for i in range(lungime):
        cifra = (vector[i] // baza ** nrcifre) % baza
        vf[cifra] = vf[cifra] + 1
    for i in range(1,baza):
        vf[i] = vf[i] + vf[i-1]
    for m in range(lungime-1, -1, -1):
        cifra = (vector[m] // baza ** nrcifre) % baza
        vf[cifra] = vf[cifra] - 1
        output[vf[cifra]] = vector[m]
    return output

def RadixSort(v, baza):
    MAX = max(v)
    output= v
    nrcifre = int(math.floor(math.log(MAX,baza)+1))
    for i in range(nrcifre):
        output = CountSortRadix(output,i,baza)
    return output


def interclasare(lst, ldr):
    i = 0
    j = 0
    rez=[]
    while i < len(lst) and j < len(ldr):
        if lst[i] <= ldr[j]:
            rez.append(lst[i])
            i += 1
        else:
            rez.append(ldr[j])
            j += 1
    rez.extend(lst[i:])
    rez.extend(ldr[j:])
    return rez

def MergeSort(ls):
    if len(ls) <= 1:
        return ls
    else:
        mij = len(ls)//2
        lst = MergeSort(ls[:mij])
        ldr = MergeSort(ls[mij:])
        return interclasare(lst,ldr)

def BFPRT(arr):
    n=len(arr)
    if n <= 5:
        return sorted(arr)[n//2]
    sbl = [sorted(arr[i:i+5]) for i in range(0, n, 5)]
    med = [x[len(x)//2] for x in sbl]
    return BFPRT(med)

def QuickSort(v):
    n = len(v)
    if n == 0:
        return []
    if n == 1:
        return v
    pivot = BFPRT(v)
    lst = []
    egal = []
    ldr = []
    for x in v:
        if x < pivot:
            lst.append(x)
        elif x == pivot:
            egal.append(x)
        else:
            ldr.append(x)
    lst = QuickSort(lst)
    ldr = QuickSort(ldr)
    lst.extend(egal)
    lst.extend(ldr)
    return lst

def BubbleSort(v):
    output = [i for i in v]
    n = len(v)
    if n>10000:
        return [0]
    for i in range(n):
        ok = False
        for j in range(0, n - i - 1):
            if output[j] > output[j+1]:
                c=output[j]
                output[j] = output[j+1]
                output[j+1] = c
                ok = True
        if ok == False:
            break
    return output

print("cate baze doriti sa testati pentru RadixSort?")
nrb = int(input("numar baze:"))
print("introduce-ti bazele:")
baze=[int(input()) for i in range(nrb)]

h = open("vectorisortati.txt","w")
f=open("vectoritext.txt","r")
date=f.readline().split()
g=open("output.txt","w")
while date:
    numbers = []
    for x in range(int(date[0])):
        numbers.append(random.randint(1, int(date[1])))
    g.write("Sortari pentru " + date[0] + " de numere cu valori pana in " + date[1] + '\n')
    sortari = [sorted, BubbleSort, CountSort, MergeSort, QuickSort,RadixSort]
    from datetime import datetime

    for sortare in sortari:
        g.write(str(sortare) + '\n')
        if sortare == RadixSort:
            for i in range(nrb):
                start = datetime.now()
                x = RadixSort(numbers, baze[i])
                g.write("RadixSort pentru baza "+str(baze[i]) + '\n')
                g.write(str(datetime.now() - start) + '\n')
                if verificare(x,numbers)==1:
                    g.write("sortarea a trecut testul de validare" + '\n')
                else:
                    g.write("eroare de validare" +'\n')
            g.write('\n')
        else:
            start = datetime.now()
            x = sortare(numbers)
            t = datetime.now() - start
            g.write(str(datetime.now() - start) + '\n')
            if verificare(x, numbers) == 1:
                g.write("sortarea a trecut testul de validare" + '\n')
            else:
                g.write("eroare de validare" + '\n')
            g.write('\n')
    h.write(str(x)+'\n')
    h.write('\n')
    date = f.readline().split()
    g.write('\n')
    g.write('\n')
h.close()
g.close()
f.close()










