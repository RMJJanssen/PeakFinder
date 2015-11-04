"""Module extracts data from .txt into numpy array"""

import numpy as np

def extract(filename):
    """Function extracts data from .txt into numpy array
    
    Parameters
    ==========
    filename : path to file in string
    
    Returns
    =======
    data : 1D numpy array
    """
    fileID=open(filename,'r')

    A=[]
    for line in fileID:
        floats = [float(x[0:len(x)-1]) for x in line.split()]
        A+=(floats)
        
    fileID.close()
    return np.array(A)
    