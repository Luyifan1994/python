# itemscoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt, centerpt, parentpt, nodetype):
    createplot.ax1.annotate(nodeTxt,xytext=centerpt,xy=parentpt,nodeTxt)


def createplot():
    fig = plt.figure(1,facecolor='white')
    fig.clf()
    createplot.ax1 = plt.subplot(111,frameon=False)
