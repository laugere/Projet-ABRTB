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


def list_to_pairs(l):
    return [l[i:i+2] for i in range(0, len(l), 2)]


def f(z, a, b):
    intervals = [(0, 0)]
    while not all(x[1]-x[0] >= random.randint(1, 15) for x in intervals):
        intervals = list_to_pairs(sorted(random.sample(range(a, b), z*2)))
    return intervals


# suffix order
f(6, 1, 100)


def RandomABRTB(p, q):
    random.seed(104724738)
    ABRTB = None
    nbNoeuds = p
    min_m = 1
    max_M = q
    intervals = f(nbNoeuds, min_m, max_M)
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
    if ABRTB.isABR() == False:
        print("Ce n'est pas un ABR")

    tab = []
    if IsIntervalDisjoint(ABRTB, tab) == False:
        print("Les intervalles ne sont pas disjoints")


def IsIntervalDisjoint(noeud, tab):
    if noeud == None:
        return False

    for interval in tab:
        if noeud.m > interval[0] and noeud.m < interval[1]:
            return False
        if noeud.M > interval[0] and noeud.M > interval[1]:
            return False

    interval = []
    interval.append(noeud.m)
    interval.append(noeud.M)
    tab.append(interval)

    return IsIntervalDisjoint(noeud.sag, tab) or IsIntervalDisjoint(noeud.sad, tab)
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


def ABRTBToABRkieme():
    print("Coming Soon")
###############################################################################################
