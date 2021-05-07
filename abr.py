import random

import functions


class Noeud_ABRTB:
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
                self.sag = Noeud_ABRTB(m, M, T)
                self.sag.parent = self
            else:
                self.sag.insertImport(m, M, T)
        else:
            if self.sad is None:
                self.sad = Noeud_ABRTB(m, M, T)
                self.sad.parent = self
            else:
                self.sad.insertImport(m, M, T)

    # Parcours infixe
    def infixe(self, tableau):
        if self.sag:
            self.sag.infixe(tableau)
        tableau.append(self.m)
        if self.sad:
            self.sad.infixe(tableau)
        return tableau

    # Parcours suffixe
    def suffixe(self, tableau):
        if self.sag:
            self.sag.suffixe(tableau)
        if self.sad:
            self.sad.suffixe(tableau)
        tableau.append(self.m)
        return tableau

    # Parcours préfixe
    def prefixe(self, tableau):
        tableau.append(self.m)
        if self.sag:
            self.sag.prefixe(tableau)
        if self.sad:
            self.sad.prefixe(tableau)
        return tableau

    # Return Prefixe tab with display
    # Args tableau require empty tab
    # Because of a memory bug
    def getParcours_prefixe_str(self, tableau):
        tableau.append(str(self.m) + ':' + str(self.M) +
                       ';' + ':'.join(map(str, self.T)) + '\n')
        if self.sag:
            self.sag.getParcours_prefixe_str(tableau)
        if self.sad:
            self.sad.getParcours_prefixe_str(tableau)
        return tableau

    def getParcours_prefixe(self, tableau):
        tableau.extend(self.T)
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


class Noeud_ABR:
    def __init__(self, value):
        self.value = value
        self.sag = None
        self.sad = None
        self.parent = None

    def __str__(self):
        return str(self.value)

    def insert(self, value):
        if value < self.value:
            if self.sad is None:
                self.sad = Noeud_ABR(value)
                self.sad.parent = self
            else:
                self.sad.insert(value)
        elif value > self.value:
            if self.sag is None:
                self.sag = Noeud_ABR(value)
                self.sag.parent = self
            else:
                self.sag.insert(value)

    # Print ABR with display
    def pprint(self, level=0):
        if self.sad:
            self.sad.pprint(level + 1)
        print(f"{' ' * 4 * level}{self.value}")
        if self.sag:
            self.sag.pprint(level + 1)

        # Parcours infixe
    def infixe(self, tableau):
        if self.sag:
            self.sag.infixe(tableau)
        tableau.append(self.value)
        if self.sad:
            self.sad.infixe(tableau)
        return tableau

    # Parcours suffixe
    def suffixe(self, tableau):
        if self.sag:
            self.sag.suffixe(tableau)
        if self.sad:
            self.sad.suffixe(tableau)
        tableau.append(self.value)
        return tableau

    # Parcours préfixe
    def prefixe(self, tableau):
        tableau.append(self.value)
        if self.sag:
            self.sag.prefixe(tableau)
        if self.sad:
            self.sad.prefixe(tableau)
        return tableau
