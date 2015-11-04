"""Module determines the widht of your window for detecting your peaks on at a time"""
import numpy as np

def BGsubstraction(y, box_pts):
    """Function smooths your data by averaging over a certain window 
    and extracts this from original data.
    
    Parameter
    =========
    y : y data
    box_pts : width of your window in datapoints
    
    Returns
    =======
    smoothened data in numpy array
    """
    
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return (y-y_smooth)

def window(y_noBG):
    """Function determines the width of the window to scan for peaks
    in number of datapoints
    
    Parameter
    =========
    y_noBG : background corrected data
    
    Returns
    =======
    width of window to scan for peaks in datapoints as an int
    """
    
    peak=max(abs(y_noBG))
    peakpos=max(y_noBG)

    if not peak == peakpos:
        peak=-1*peak
    
    sigma = np.std(y_noBG)

    for i in range(list(y_noBG).index(peak),len(y_noBG)-list(y_noBG).index(peak)):
        if abs(y_noBG[i])<sigma:
            width=(i-list(y_noBG).index(peak))*4
            break
    return(int(width))