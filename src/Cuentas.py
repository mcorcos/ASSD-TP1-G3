##############################################################
#   Cuentas:
#
#
#############################################################
class Cuentas:

    def __init__(self, fS=27, f0=100, maxF=1000):
        self.fS = fS
        self.f0 = f0
        self.fAlias = self.calculateAliasFrequency()
        self.harmonics = self.calculateHarmonics(maxF)

    ###################################################################################
    # getFrequencies
    ###################################################################################
    def getFrequencies(self, fS=27, f0=100, maxF=1000):
        self.fS = fS
        self.f0 = f0
        self.fAlias = self.calculateAliasFrequency()
        self.harmonics = self.calculateHarmonics(fS, f0, maxF)

        return self.f0, self.fS, self.fAlias, self.harmonics

    ###################################################################################
    # getOriginalSignal
    #
    ###################################################################################
    def getSignal(self):
        t = []
        y = []
        return t,y

    ###################################################################################
    # getAliasSignal
    #
    ###################################################################################
    def getAliasSignal(self):
        t = []
        y = []
        return t, y

    ###################################################################################
    # getAliasSignal
    #
    ###################################################################################
    def getAliasSignal(self):
        t = []
        y = []
        return t, y

    ###################################################################################
    ###################################################################################
    #  Private Methods
    #
    ###################################################################################
    ###################################################################################

    ###########################################################################
    # calculateAliasFrequency
    ###########################################################################
    def calculateAliasFrequency(self):
        if self.f0 < self.fS / 2:
            fAlias = None
        else:
            delta = self.f0 % self.fS
            if delta < self.fS / 2:
                fAlias = delta
            else:
                fAlias = self.fS - delta

        return fAlias

    ###################################################################################
    # calculateHarmonics
    ###################################################################################
    def calculateHarmonics(self, maxF=1000):
        delta = self.f0 % self.fS
        if delta > self.fS / 2:
            delta = self.fS - delta

        harmonics = []

        f1 = delta
        f2 = self.fS - delta
        while f1 < maxF:
            harmonics.append(f1)
            harmonics.append(f2)
            f1 += self.fS
            f2 += self.fS

        return harmonics
