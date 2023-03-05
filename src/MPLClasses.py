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

    def plot(self, f0, fS, fAlias, harmonics):
        self.axes.set_ylim([0,1]) #fijar el eje y
        self.axes.spines['top'].set_visible(False) #sacobordearriba
        self.axes.spines['bottom'].set_visible(False) #sacobordeabajo

        #creo la regla
        start = 0
        end = 100
        steps = end/10

        for i in range(int((end-start)/10) +1):
            self.axes.axvline(x=start+i*steps,linewidth=0.5,color='k') #crear lineas
            self.axes.text(start+i*steps,-1,str(start+i*steps),ha='center',fontsize=8) # crear los numeritos bajo cada linea


        #creo las deltas para cada caso 
    
        






        self.fig.canvas.draw_idle()


