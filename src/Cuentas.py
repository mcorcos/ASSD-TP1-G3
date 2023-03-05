##############################################################
#   Cuentas:
#
#
#############################################################

class Cuentas:

    def __init__(self, fS = 27, f0 = 100, maxF = 1000):
        self.fS = fS
        self.f0 = f0
        self.fAlias = self.calculateAliasFrequency(fS, f0)
        self.harmonics = self.calculateHarmonics(fS, f0, maxF)

    ###########################################################################
    # calculateAliasFrequency
    ###########################################################################
    def calculateAliasFrequency(self, fS, f0):
        if f0 < fS / 2:
            fAlias = None
        else:
            delta = f0 % fS
            if delta < fS/2:
                fAlias = delta
            else:
                fAlias = fS - delta

        return fAlias

    ###################################################################################
    # calculateHarmonics
    ###################################################################################
    def calculateHarmonics(self, fS, f0, maxF = 1000):
        delta = f0 % f0
        if delta > fS / 2:
            delta = fS - delta

        harmonics = []

        f1 = delta
        f2 = fS - delta
        while(f1 < maxF):
            harmonics.append(f1)
            harmonics.append(f2)
            f1 += fS
            f2 += fS

        return harmonics

    ###################################################################################
    # setFrequencies
    ###################################################################################
    def setFrequencies(self, fSign = 27, fSamp = 100):
        self.fS = fSign
        self.fO = fSamp

    ###################################################################################
    # getFrequencies
    ###################################################################################
    def getFrequencies(self, ):


        return self.f0, self.fS, self.fAlias, self.harmonics