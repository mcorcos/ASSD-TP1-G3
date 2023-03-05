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

        self.updatePlots()

        # Configuración de las pestañas y clicks
        self.sliderSignalFreq.sliderMoved.connect(self.sliderSigToDouble)
        self.signalFreq.valueChanged.connect(self.doubleToSliderSig)
        self.sliderSampleFreq.sliderMoved.connect(self.sliderSampleToDouble)
        self.sampleFreq.valueChanged.connect(self.doubleToSliderSample)


    def updatePlots(self):
        self.plotRuler()

    def plotRuler(self):
        fSig = self.signalFreq.value()
        fSample = self.sampleFreq.value()
        fMax = self.scaleSlider.value()

        f0, fS, fAlias, harmonics = self.cuentas.getFrequencies(fSig, fSample, fMax)
        self.rulerPlot.plot(f0, fS, fAlias, harmonics, fMax)


    # Configuración de las pestañas y clicks
    def sliderSigToDouble(self, value):
        val = float(value) / 100
        self.signalFreq.setValue(val)
        self.updatePlots()

    def doubleToSliderSig(self, value):
        val = int(value*100)
        self.sliderSignalFreq.setValue(val)
        self.updatePlots()

    def sliderSampleToDouble(self, value):
        val = float(value) / 100
        self.sampleFreq.setValue(val)
        self.updatePlots()

    def doubleToSliderSample(self, value):
        val = int(value*100)
        self.sliderSampleFreq.setValue(val)
        self.updatePlots()
