from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import matplotlib.patches as mpatches


class MplCanvas(FigureCanvas):
    """
        MplCanvas
    """
    def __init__(self, parent=None):
        self.fig = Figure()
        super().__init__(self.fig)

        self.axes = self.fig.add_subplot()
        self.fig.set_tight_layout(True)
        #self.navToolBar = NavigationToolbar(self, parent=parent)
        #parent.layout().addWidget(self.navToolBar)
        parent.layout().addWidget(self)


class RulerPlot(MplCanvas):
    """
        RulerPlot
    """
    def __init__(self, parent=None):
        if parent is not None:
            super().__init__(parent)

    def plot(self, f0, fS, fAlias, harmonics, maxF):

        self.axes.clear()
        self.axes.set_xlim([0, maxF])    # fijar el eje x
        self.axes.set_ylim([0, 1])   # fijar el eje x
        self.axes.spines['top'].set_visible(False)  # sacobordearriba
        self.axes.spines['left'].set_visible(False)  # eliminar el eje y
        self.axes.spines['right'].set_visible(False)  # eliminar el eje x

        # hide y-axis
        self.axes.get_yaxis().set_visible(False)

        # creo las deltas para cada caso
        if len(harmonics[0]) > 0:
            self.axes.stem(harmonics[0], harmonics[1], 'm', '^m')

        self.axes.stem(f0, 0.6, 'b', '^b')
        self.axes.stem(fS, 0.6, '--r', 'r')

        if fAlias is not None:
            self.axes.stem(fAlias, 0.6, 'g', '^g')

        self.axes.stem(fS/2, 0.6, '--k', 'k')

        # stems labeling

        fS_patch = mpatches.Patch(color='r', label='fS='+str(fS)+'Hz')
        f0_patch = mpatches.Patch(color='b', label='f0='+str(f0)+'Hz')
        fAlias_patch = mpatches.Patch(color='g', label='fAlias='+str(fAlias)+'Hz')
        fH_patch = mpatches.Patch(color='m', label='Harmonics')
        fNy_patch = mpatches.Patch(color='k', label='f.Nyquist='+str(fS/2)+'Hz')


        self.axes.legend(handles=[fS_patch, f0_patch, fAlias_patch, fH_patch, fNy_patch],
                         ncol=5, prop={'size': 7})

        self.fig.canvas.draw()


class TempPlot(MplCanvas):
    """
        TempPlot
    """
    def __init__(self, parent=None):
        if parent is not None:
            super().__init__(parent)

    def plot(self, array_f0, array_fS, array_fAlias, maxT):

        self.axes.clear()

        self.axes.set_xlim([0, maxT])   # fijar el eje x
        self.axes.set_ylim([-1.3, 1.3])  # fijar el eje x

        # hide y-axis
        self.axes.get_yaxis().set_visible(False)
        self.axes.axhline(y=0, color='black')

        # grafico la frecuencia de la señal
        self.axes.plot(array_f0[0], array_f0[1], color='b')

        # grafico los samples
        if len(array_fS[0]) > 0:
            self.axes.stem(array_fS[0], array_fS[1], 'r', 'or')

        # grafico Alias
        if array_fAlias[0] is not None:
            self.axes.plot(array_fAlias[0], array_fAlias[1], color='g', linestyle='dashed')
            #grafico el label de alias

            # fAlias_patch = mpatches.Patch(color='g', label='fAlias='+str(array_fAlias[2])+'Hz')

            # self.axes.legend(handles=[fAlias_patch],
            #            ncol=5, prop={'size': 7}, loc='upper center')
        

        self.fig.canvas.draw()
