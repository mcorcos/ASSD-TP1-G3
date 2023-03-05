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


        self.axes.clear()
        self.axes.set_xlim([0,maxF]) #fijar el eje x
        self.axes.set_ylim([0,1]) #fijar el eje x
        self.axes.spines['top'].set_visible(False) #sacobordearriba
        self.axes.spines['left'].set_visible(False)  # eliminar el eje y
        self.axes.spines['right'].set_visible(False)  # eliminar el eje x

        #hide y-axis 
        self.axes.get_yaxis().set_visible(False)

       
        #creo las deltas para cada caso 
        self.axes.stem(harmonics[0],0.7,'-.m','m',label='harmonics')
        for i in range(len(harmonics)):
            self.axes.stem(harmonics[i],0.7,'-.m','m')    
            plt.annotate(str(harmonics[i]) , xy=(harmonics[i],-0.1)   )
        self.axes.stem(f0,0.7,'b','b',label='f0')
        self.axes.stem(fS,0.7,'r','r',label='fS')

        if fAlias is not None:
            self.axes.stem(fAlias,0.7,'--g','g',label='fAlias')


        #labels de stems

        self.axes.legend(ncol=4, loc='upper right' ,prop={'size': 7})



 


        self.fig.canvas.draw_idle()


