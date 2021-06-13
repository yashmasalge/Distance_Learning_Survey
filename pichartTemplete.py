import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class piChart:
    lables = []
    data = []
    outputImage = str
    def __init__(self,labels,data,outputImage):
        self.lables = labels
        self.data = data
        self.outputImage = outputImage
        self.showChart()

    def showChart(self):
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('equal')
        plt.pie(self.data, labels=self.lables, autopct='%1.2f%%')
        plt.savefig(self.outputImage)