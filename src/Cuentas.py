import numpy as np


class Cuentas:
    """
        Cuentas:

    """

    def __init__(self, f0=20, fS=22, maxTimeInterval=1, maxF=5):
        self.fS = fS
        self.f0 = f0
        self.masxTimeInterval = maxTimeInterval
        self.fAlias = self.calculateAliasFrequency()
        self.harmonics = self.calculateHarmonics(maxF)

    def getFrequencies(self, f0, fS, maxF):
        """
        @param fS:
        @param f0:
        @param maxF:
        @return:
        """
        self.fS = fS
        self.f0 = f0
        self.fAlias = self.calculateAliasFrequency()
        self.harmonics = self.calculateHarmonics(maxF)

        return self.f0, self.fS, self.fAlias, self.harmonics

    def getMaxTimeInterval(self):
        return self.maxTimeInterval

    def getSignal(self, maxTimeInterval, n=500):
        """
        @return:
        """

        # periodos * (1/f0) es cuenta tiene q dar mayor a 1. si es menor a uno poner 1
        self.maxTimeInterval = maxTimeInterval
        '''if(maxT<1):
            t = np.linspace(0,1,n)
        else:
            t = np.linspace(0,maxT, n)'''

        t = np.linspace(0, self.maxTimeInterval, n)
        y = np.sin(2 * np.pi * self.f0 * t)
        return [t, y]

    def getAliasSignal(self, n=500):
        """

        @return:
        """
        if self.fAlias is None:
            return None, None

        '''if(maxT<1):
            t = np.linspace(0,1,n)
        else:
            t = np.linspace(0,maxT, n)'''

        t = np.linspace(0, self.maxTimeInterval, n)

        delta = self.f0 % self.fS

        if delta < self.fS / 2:
            y = np.sin(2 * np.pi * self.fAlias * t)
        else:
            y = -np.sin(2 * np.pi * self.fAlias * t)

        return [t, y,self.fAlias]

    def getSamplingPoints(self):
        """

        @return:
        """

        '''if(maxT<1):
            t = np.arange(0,1, 1/ self.fS)
        else:
            t = np.arange(0,maxT, 1/ self.fS)'''

        t = np.arange(0, self.maxTimeInterval, 1 / self.fS)
        y = np.sin(2 * np.pi * self.f0 * t)
        return [t, y]

    ###################################################################################
    ###################################################################################
    #  Private Methods
    #
    ###################################################################################
    ###################################################################################

    def calculateAliasFrequency(self):
        """

        @return:
        """
        if self.f0 < self.fS / 2:
            fAlias = None
        else:
            delta = self.f0 % self.fS
            if delta < self.fS / 2:
                fAlias = delta
            else:
                fAlias = self.fS - delta

        return fAlias

    def calculateHarmonics(self, maxF):
        """

        @param maxF:
        @return:
        """
        delta = self.f0 % self.fS
        if delta > self.fS / 2:
            delta = self.fS - delta

        x = []
        y = []
        harmonics = [x, y]

        f1 = delta
        f2 = self.fS - delta
        while f1 < maxF:
            harmonics[0].append(f1)
            harmonics[0].append(f2)
            harmonics[1].append(0.6) 
            harmonics[1].append(0.6)           
            f1 += self.fS
            f2 += self.fS

        return harmonics
