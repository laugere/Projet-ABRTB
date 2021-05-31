import random

import abr

###############################################################################################
# Generate, save and display ABRTB section


def CreateABRTBFromFile(path='defaultABRTB.txt'):
    if path == '':
        path = 'defaultABRTB.txt'
    file = open(path, 'r')
    if file == None:
        return "Le fichier n'a pas été trouvé"

    Lines = file.readlines()

    if Lines == None:
        return "Le fichier est vide"

    count = 0
    for line in Lines:
        splittedString = line.split(';')
        ABRvalues = splittedString[0].split(':')
        Tvalues = splittedString[1].strip('\n').split(':')
        T = []
        for i in range(0, len(Tvalues)):
            T.append(int(Tvalues[i]))
        m = int(ABRvalues[0])
        M = int(ABRvalues[1])

        if count == 0:
            abrtb = abr.Noeud_ABRTB(m, M, T)
            count += 1
        else:
            abrtb.insertImport(m, M, T)

    return abrtb


def ExportABRTBToFile(ABRTB, path='defaultExport.txt'):
    if path == '':
        path = 'defaultExport.txt'
    file = open(path, 'w')
    tableau = ABRTB.getParcours_prefixe_str([])
    file.writelines(tableau)
    file.close


def DisplayABRTB(ABRTB):
    tableau = ABRTB.getParcours_prefixe_str([])
    for line in tableau:
        print(line.replace('\n', ''))


def PairList(l):
    return [l[i:i+2] for i in range(0, len(l), 2)]


def fo(z, a, b):
    intervals = [(0, 0)]
    while not all(x[1]-x[0] >= random.randint(1, 15) for x in intervals):
        intervals = PairList(sorted(random.sample(range(a, b), z*2)))
    return intervals


def RandomABRTB(p, q):
    random.seed(104724738)
    ABRTB = None
    nbNoeuds = p
    min_m = 1
    max_M = q
    intervals = fo(nbNoeuds, min_m, max_M)
    for interval in intervals:
            m = interval[0]
            M = interval[1]
            T = []
            for i in range(random.randint(1, 10)):
                T.append(random.randint(m, M))
            if ABRTB is None:
                ABRTB = abr.Noeud_ABRTB(m, M, T)
            else:
                ABRTB.insertImport(m, M, T)
    return ABRTB


def VerifABRTB(ABRTB):
    isOk = True
    if ABRTB.isABR() == False:
        isOk = False
        print("Ce n'est pas un ABR")

    if IsIntervalDisjoint(ABRTB) == True:
        isOk = False
        print("Les intervalles se chevauchent")

    if IsVerifIntervalTasOk(ABRTB) == False:
        isOk = False
        print("Les max tas binaire ne sont pas corrects ou ne sont pas compris dans les intervalles")

    if isOk == True:
        print("L'ABRTB est correct")


def IsIntervalDisjoint(noeud):
    if noeud == None:
        return False

    if(noeud.parent != None):
        if (noeud.m > noeud.parent.m and noeud.m < noeud.parent.M) or (noeud.M > noeud.parent.m and noeud.M < noeud.parent.M):
            return True

    return IsIntervalDisjoint(noeud.sag) or IsIntervalDisjoint(noeud.sad)


def IsVerifIntervalTasOk(noeud):
    isOk = True

    if noeud == None:
        return True
    
    n = len(noeud.T) - 1
    isMaxTas = IsMaxTasBinaire(noeud.T, 0, n)

    if isMaxTas == False:
        isOk = False
    else:
        max = noeud.T[0]
        min = noeud.T[0]
        for val in noeud.T:
            if val < min:
                min = val
        if (min >= noeud.m and min <= noeud.M) and (max >= noeud.m and max <= noeud.M):
            isOk = True
        else:
            isOk = False

    return IsVerifIntervalTasOk(noeud.sag) and IsVerifIntervalTasOk(noeud.sad) and isOk
    

def IsMaxTasBinaire(tab, i, n):
    if i >= int((n - 2) / 2):
        return True
     
    if(tab[i] >= tab[2 * i + 1] and
       tab[i] >= tab[2 * i + 2] and
       IsMaxTasBinaire(tab, 2 * i + 1, n) and
       IsMaxTasBinaire(tab, 2 * i + 2, n)):
        return True
     
    return False
###############################################################################################

###############################################################################################
# Manipulate ABRTB section


def SearchInteger(ABRTB, value):
    ABRTBTemp = ABRTB.searchValue(value)
    if ABRTBTemp:
        print("La valeur {0} est contenu dans l'intervalle m = {1}, M = {2}.".format(
            value, ABRTBTemp.m, ABRTBTemp.M))
        print("T = {0}".format(ABRTBTemp.T))
    else:
        print("Aucun intervalle ne contient {0}.".format(value))


def DeleteInteger(ABRTB, value):
    ABRTB.delete(value)
    DisplayABRTB(ABRTB)


def InsertInteger(ABRTB, value):
    ABRTB.insert(value)
    DisplayABRTB(ABRTB)


def ABRTBToABR(ABRTB):
    tableau = ABRTB.getParcours_prefixe([])
    abr_result = None
    for value in tableau:
        if abr_result is None:
            abr_result = abr.Noeud_ABR(value)
        else:
            abr_result.insert(value)
    print("Parcours préfixe (SP (A)) : ")
    print(abr_result.prefixe([]))
    print("Parcours infixe (SI(A)) : ")
    print(abr_result.infixe([]))


def ABRTBToABRkieme(ABRTB, k):
    abr_result = None
    abr_result = NewABR(ABRTB, k, abr_result)
    print("Parcours préfixe (SP (A)) : ")
    print(abr_result.prefixe([]))
    print("Parcours infixe (SI(A)) : ")
    print(abr_result.infixe([]))


def NewABR(ABRTB, k, newAbr):
    tas = ABRTB.T
    TriParTas(tas)
    keme = -1
    if len(tas) - k >= 0:
        keme = tas[len(tas) - k]

    if keme != -1:
        if newAbr is None:
            newAbr = abr.Noeud_ABR(keme)
        else:
            newAbr.insert(keme)

    if ABRTB.sag:
        NewABR(ABRTB.sag, k, newAbr)

    if ABRTB.sad:
        NewABR(ABRTB.sad, k, newAbr)

    return newAbr

def SiftDown(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
 
        SiftDown(arr, n, largest)
 
 
def TriParTas(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        SiftDown(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        SiftDown(arr, i, 0)
###############################################################################################
