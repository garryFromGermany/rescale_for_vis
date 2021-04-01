import numpy as np
from .rescale import rescale_for_vis

__all__ = ["mediate","verify_order"]

def mediate(original, rescaled, parameter=0.5):
    """linearly interpolate between original niveaus and the results of rescale_for_vis,
    parameter (float): in the interval [0,1], if zero, then the original values are returned"""
    original = np.array(original)
    original -= original.min()
    original /= original.max()
    original *= rescaled.max()
    return original*(1-parameter) + rescaled*parameter

def verify_order(niveaus, levels):
    """verify the integrity of the results of rescale_for_vis"""
    E1, E2 = np.meshgrid(niveaus,niveaus, indexing="ij")
    M_ini = E1 - E2
    E1, E2 = np.meshgrid(levels,levels, indexing="ij")
    M_fin = E1 - E2
    #quicksort does not preserve order
    a = np.around(M_ini,14).flatten().argsort(kind="mergesort")
    b = np.around(M_fin,14).flatten().argsort(kind="mergesort")
    return (a == b).all()
