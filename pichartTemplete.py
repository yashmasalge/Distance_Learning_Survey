import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os


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
        plt.pie(self.data, autopct='%1.2f%%')
        plt.legend(self.lables)
        plt.title(label='title',fontstyle='italic')
        if not os.path.exists('./chart/'):
            os.mkdir('./chart/')
        plt.savefig('./chart/'+self.outputImage)