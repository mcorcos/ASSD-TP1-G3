# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QMessageBox

# Project modules
from src.ui.mainwindow import Ui_MainWindow
from src.Cuentas import Cuentas
from src.MPLClasses import RulerPlot, TempPlot


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.cuentas = Cuentas()
        self.rulerPlot = RulerPlot(self.frequencyPlot)
        self.tempPlot = TempPlot(self.temporalPlot)

        self.updatePlots()

        # Configuración de las pestañas y clicks
        self.sliderSignalFreq.sliderMoved.connect(self.sliderSigToDouble)
        self.signalFreq.valueChanged.connect(self.doubleToSliderSig)
        self.sliderSampleFreq.sliderMoved.connect(self.sliderSampleToDouble)
        self.sampleFreq.valueChanged.connect(self.doubleToSliderSample)
        self.scaleSlider.sliderMoved.connect(self.scaleSliderMoved)
        self.filterCheck.clicked.connect(self.filterCheckClicked)
        self.aliasCheck.clicked.connect(self.aliasCheckClicked)
        self.plotButton.clicked.connect(self.maxTimeIntervalChanged)


    def updatePlots(self):
        self.plotRuler()
        self.plotTemp()

    def plotRuler(self):
        fSig = self.signalFreq.value()
        fSample = self.sampleFreq.value()
        fMax = self.scaleSlider.value()
        f0, fS, fAlias, harmonics = self.cuentas.getFrequencies(fSig, fSample, fMax)

        if not self.filterCheck.isChecked():
            harmonics = [[], []]

        self.rulerPlot.plot(f0, fS, fAlias, harmonics, fMax)

    def plotTemp(self):
        order = self.orderValue.value()
        array_f0 = self.cuentas.getSignal(self.strToFloat(self.maxIntervalDouble.text()))
        array_fAlias = self.cuentas.getLPSignal(n=order)
        array_fS = self.cuentas.getSamplingPoints()
        maxTimeInterval = self.cuentas.getMaxTimeInterval()

        if not self.aliasCheck.isChecked():
            array_fAlias = [None, None, None]

        self.tempPlot.plot(array_f0, array_fS, array_fAlias, maxTimeInterval)

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

    def filterCheckClicked(self):
        self.updatePlots()

    def aliasCheckClicked(self):
        self.updatePlots()

    def maxTimeIntervalChanged(self):
        self.updatePlots()


    def strToFloat(self, string):
        res = 0
        try:
            if string == '':
                res = 0
            else:
                res = float(string)

        except ValueError:
            res = 0
            self.warningNotFloat()

        return res

    def warningNotFloat(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("Ingrese un número valido")
        msgBox.setWindowTitle("Advertencia")
        msgBox.exec()
        return

