#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

""" This module contains functions which allows you to quickly make graphs to inspect your data"""

def PlotPeak(Freq,S21,Fc=-1,HalfWidth=-1):
    """This function plots the magnitude as a function of frequency. 
    A central frequency and width (in frequency space) can be defined such that only part of the data is plotted.
    
    Parameters
    -------------------------------------
    Freq = Vector of length(N) containing frequency data
    S21 = Vector of length(N) containing magnitude data
    Fc [optional] = Central frequency of the range to plot (same unit as Freq)
    HalfWidth [optional] = Halfwidth of the range to plot (same unit as Freq)
    
    If Fc or HalfWidth is <=0 then the entire range is plotted.
    """
    
    if (Fc>0) and (HalfWidth>0):
        FrangeIdx = np.empty((len(Freq),2),dtype=bool)
        FrangeIdx[:,0] = Freq >= Fc - HalfWidth
        FrangeIdx[:,1] = Freq < Fc + HalfWidth
        plt.plot(Freq[np.all(FrangeIdx,axis=1)],S21[np.all(FrangeIdx,axis=1)],'b.')
        plt.show()
    else:
        plt.plot(Freq,S21,'b.')
        plt.show()
        
def QuickOverview(Freq,S21,Fwidth=-1):
    """This function gives a quick overview of the data that you have.
    It plots the total frequency span as well as the data chopped in widths of Fwidth.
    
    Parameters
    ------------------------------------
    Freq = Vector of length(N) containing frequency data
    S21 = Vector of length(N) containing magnitude data
    Fwidth [optional] = width of frequency bins to show. If <=0 data is chopped into 10 equal size parts.
    """
    
    if Fwidth<=0:
        Nsteps = 10
        Fwidth = (max(Freq)-min(Freq))/10
    else:
        Nsteps = np.ceil((max(Freq)-min(Freq))/Fwidth)
        
    Fcentral = np.linspace(min(Freq),max(Freq),Nsteps+1)+0.5*Fwidth

    for p in Fcentral[:-1]:
        PlotPeak(Freq,S21,Fc=p,HalfWidth=0.5*Fwidth)
            