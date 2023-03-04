##############################################################
#   Cuentas:
#
#
#############################################################

class Cuentas:

    def __init__(self, fS = 27, f0 = 100):
        self.fS = fS
        self.f0 = f0
        self.fAlias = self.calculateAliasFrequency(fS, f0)
        self.harmonics = self.calculatesHarmonics(fS, f0)

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
    # calculatesHarmonics
    ###################################################################################
    def calculatesHarmonics(self,fS, f0):
        return

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