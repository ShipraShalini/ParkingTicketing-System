"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import cStringIO
import math
import numpy as np

import matplotlib.pyplot as plt
from src.common.constants import *


class BarChartClass():
    bar_width = 0.35
    opacity = 0.4
    bario = cStringIO.StringIO()

    def set_ylim(self,num):
        ylim= int(math.ceil(num / 10.0)) * 10
        if ylim == num:
            ylim = ylim+10
        return ylim

    def usedata(self, data):
        xaxis=[]
        yaxis=[]
        for k,v in data.iteritems():
            xaxis.append(k)
            yaxis.append(v)
        index = np.arange(len(xaxis))
        ylim = self.set_ylim(max(yaxis))
        return tuple(xaxis), tuple(yaxis), index , ylim

    def drawchart(self, data):
        xaxis, yaxis, index, ylim = self.usedata(data)
        plt.bar(index, yaxis, self.bar_width,
                 alpha=self.opacity,
                 color='b',
                 label='Colours')

        plt.ylim(0,ylim)
        plt.xlabel('Colour')
        plt.ylabel('Number')
        plt.title('Numbers of cars of each colour')
        plt.xticks(index + (self.bar_width/2), xaxis)
        plt.legend()
        plt.tight_layout()
        plt.show()
        plt.savefig(self.bario, format=FORMAT)
        return self.bario.getvalue().encode("base64").strip()

barchart = BarChartClass()