# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow

# Project modules
from src.ui.mainwindow import Ui_MainWindow
from src.Cuentas import Cuentas
from src.MPLClasses import RulerPlot,TempPlot


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.rulerPlot = RulerPlot(self.frequencyPlot)
        self.tempPlot = TempPlot(self.temporalPlot)
        self.cuentas = Cuentas()

        self.updatePlots()
                # Configuración de las pestañas y clicks
        self.sliderSignalFreq.sliderMoved.connect(self.sliderSigToDouble)
        self.signalFreq.valueChanged.connect(self.doubleToSliderSig)
        self.sliderSampleFreq.sliderMoved.connect(self.sliderSampleToDouble)
        self.sampleFreq.valueChanged.connect(self.doubleToSliderSample)
        self.scaleSlider.sliderMoved.connect(self.scaleSliderMoved)


    def updatePlots(self):
        self.plotRuler()
        self.plotTemp()

    def plotRuler(self):
        fSig = self.signalFreq.value()
        fSample = self.sampleFreq.value()
        fMax = self.scaleSlider.value()

        f0, fS, fAlias, harmonics = self.cuentas.getFrequencies(fSig, fSample, fMax)
        self.rulerPlot.plot(f0, fS, fAlias, harmonics, fMax)

    def plotTemp(self):

        array_f0_x,array_f0_y = self.cuentas.getSignal(10,500)
        array_fAlias_x , array_fAlias_y = self.cuentas.getAliasSignal(500)
        array_fS_x , array_fS_y = self.cuentas.getSamplingPoints()
        self.tempPlot.plot(array_f0_x , array_f0_y , array_fS_x , array_fS_y , array_fAlias_x, array_fAlias_y)


    # Configuración de las pestañas y clicks
    def sliderSigToDouble(self, value):
        val = float(value)
        self.signalFreq.setValue(val)
        self.updatePlots()

    def doubleToSliderSig(self, value):
        val = int(value)
        self.sliderSignalFreq.setValue(val)
        self.updatePlots()

    def sliderSampleToDouble(self, value):
        val = float(value)
        self.sampleFreq.setValue(val)
        self.updatePlots()

    def doubleToSliderSample(self, value):
        val = int(value)
        self.sliderSampleFreq.setValue(val)
        self.updatePlots()

    def scaleSliderMoved(self):
        self.updatePlots()
