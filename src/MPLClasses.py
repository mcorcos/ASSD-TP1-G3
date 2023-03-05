from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas,\
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class MplCanvas(FigureCanvas):
    """
        MplCanvas
    """
    def __init__(self, parent=None):
        self.fig = Figure()
        super().__init__(self.fig)

        self.axes = self.fig.add_subplot()
        self.fig.set_tight_layout(True)
        self.navToolBar = NavigationToolbar(self, parent=parent)
        parent.layout().addWidget(self.navToolBar)
        parent.layout().addWidget(self)


class RulerPlot(MplCanvas):
    """
        RulerPlot
    """
    def __init__(self, parent=None):
        if parent is not None:
            super().__init__(parent)

    def plot(self, f0, fS, fAlias, harmonics, maxF):

        self.axes.set_xlim([0,maxF]) #fijar el eje y

        self.axes.spines['top'].set_visible(False) #sacobordearriba
        self.axes.spines['left'].set_visible(False)  # eliminar el eje y
        self.axes.spines['right'].set_visible(False)  # eliminar el eje x

        #hide y-axis 
        self.axes.get_yaxis().set_visible(False)

       
        #creo las deltas para cada caso 
        self.axes.stem(f0,0.9,'b','b')
        self.axes.stem(fS,0.9,'r','r')
        self.axes.stem(fAlias,0.9,'--g','g')
        for i in range(len(harmonics)):
            self.axes.stem(harmonics[i],0.9,'-.m','m')



        self.fig.canvas.draw_idle()


