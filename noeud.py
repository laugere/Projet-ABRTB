import random

import main
import noeud
import functions


class Noeud:
    def __init__(self, m, M, T):
        self.M = M
        self.m = m
        self.T = T
        self.sag = None
        self.sad = None
        self.parent = None

    def __str__(self):
        return str(self.m)

    # Insert new value in ABRTB
    def insert(self, value):
        if value >= self.m and value <= self.M:
            print("Insertion effectuée dans l'intervalle m = {0}, M = {1}".format(
                self.m, self.M))
            self.T.append(value)
        if value > self.M:
            if self.sad is None:
                print("Insertion impossible")
            else:
                self.sad.insert(value)
        if value < self.m:
            if self.sag is None:
                print("Insertion impossible")
            else:
                self.sag.insert(value)
    
    # Delete value in ABRTB
    def delete(self, value):
        noeud = self.searchValue(value)
        if noeud:
            noeud.T.remove(value)


    # Insert Noeud with all value and T TBR
    def insertImport(self, m, M, T):
        if m < self.m:
            if self.sag is None:
                self.sag = Noeud(m, M, T)
                self.sag.parent = self
            else:
                self.sag.insertImport(m, M, T)
        else:
            if self.sad is None:
                self.sad = Noeud(m, M, T)
                self.sad.parent = self
            else:
                self.sad.insertImport(m, M, T)

    # Print ABRTB with display (Coming soon)
    def pprint(self, level=0):
        if self.sad:
            self.sad.pprint(level + 1)
        print(f"{' ' * 4 * level}{self.m}")
        if self.sag:
            self.sag.pprint(level + 1)

    # Parcours infixe
    def infixe(self, tab):
        if self.sag != None:
            self.sag.infixe(tab)
        tab.append(self.m)
        if self.sad != None:
            self.sad.infixe(tab)
        return tab

    # Return Prefixe tab with display
    # Args tableau require empty tab
    # Because of a memory bug
    def getParcours_prefixe(self, tableau):
        tableau.append(str(self.m) + ':' + str(self.M) +
                       ';' + ':'.join(map(str, self.T)) + '\n')
        if self.sag:
            self.sag.getParcours_prefixe(tableau)
        if self.sad:
            self.sad.getParcours_prefixe(tableau)
        return tableau

    # Search Value in ABRTB
    def searchValue(self, value):
        if value >= self.m and value <= self.M:
            if value in self.T:
                return self
            else:
                print("L'intervalle pouvant contenir cette valeur est m = {0}, M = {1}".format(
                    self.m, self.M))
                return None
        if value > self.M:
            return self.sad.searchValue(value) if self.sad else None
        if value < self.m:
            return self.sag.searchValue(value) if self.sag else None

    # Test if the ABRTB is an ABR
    def isABR(self):
        tab = []
        tab = self.infixe(tab)
        for i in range(0, len(tab)-1):
            if tab[i] > tab[i+1]:
                return False
        return True
