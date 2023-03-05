# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow

# Project modules
from src.ui.mainwindow import Ui_MainWindow
from src.Cuentas import Cuentas
from src.MPLClasses import RulerPlot


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.rulerPlot = RulerPlot(self.frequencyPlot)

        self.cuentas = Cuentas()

        self.plot()

    def plot(self):
        self.plotRuler()

    def plotRuler(self):
        f0, fS, fAlias, harmonics = self.cuentas.getFrequencies()
        self.rulerPlot.plot(200, 400, 800, [300,500,600]   ,  maxF=1000)
