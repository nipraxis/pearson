"""
This will be your new module with the Pearson correlation function

First try to fill in the "pearson_1d" function.

When you are done with "pearson_1d", you should be able to run the following
command (from the day5 directory) and see no errors or failures::

    python3 -m pytest test_pearson_1d.py

Then, if you are feeling brave, fill in the "pearson_2d" function.  Test with::

    python3 -m pytest test_pearson_2d.py
"""

import numpy as np


def pearson_1d(x, y):
    """ Pearson product-moment correlation of vectors `x` and `y`

    Parameters
    ----------
    x : array shape (N,)
        One-dimensional array to correlate with `y`
    y : array shape (N,)
        One dimensional array to correlate with `x`

    Returns
    -------
    r_xy : scalar
        Pearson product-moment correlation of vectors `x` and `y`.
    """
    mc_x,mc_y = x-x.mean(), y-y.mean()
    a = np.sum(mc_x*mc_y)
    b = np.sum(mc_x*mc_x)
    c = np.sum(mc_y*mc_y)
    return a / (np.sqrt(b)*np.sqrt(c))



def pearson_2d(x, Y):
    """ Pearson product-moment correlation of vectors `x` and array `Y`

    Parameters
    ----------
    x : array shape (N,)
        One-dimensional array to correlate with every column of `Y`
    Y : array shape (N, P)
        2D array where we correlate each column of `Y` with `x`.

    Returns
    -------
    r_xy : array shape (P,)
        Pearson product-moment correlation of vectors `x` and the columns of
        `Y`, with one correlation value for every column of `Y`.
    """
    mc_x = x-x.mean()   # (12,)
    mc_y = Y-Y.mean(axis=0)[None,:]     # (22,12) = (22,12)-(1,12) 
    a = np.sum(mc_x[:,None]*mc_y,axis=0)    #  (12,)  << sum on axis 0 << ( (22,12)  << (1,12)*(22,12) )
    b = np.sum(mc_x*mc_x)   #   rank 0 << ()
    c = (mc_y*mc_y).sum(axis=0)     #   (12,)  <<  sum on axis 0 << (22,12)*(22,12)
    return a / (np.sqrt(b)*np.sqrt(c))
