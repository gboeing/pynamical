"""
pynamical tests
-------
"""

import matplotlib as mpl
mpl.use('Agg') #use agg backend so you don't need a display on travis

from pynamical import simulate, logistic_map, cubic_map
from pynamical import bifurcation_plot, cobweb_plot, phase_diagram, phase_diagram_3d

def test_imports():
    import os, pandas as pd, numpy as np
    import matplotlib.pyplot as plt, matplotlib.cm as cm, matplotlib.font_manager as fm
    from mpl_toolkits.mplot3d import Axes3D
    from numba import jit
    
def test_simulate():
    pops = simulate(model=logistic_map, num_gens=200, rate_min=3.7, rate_max=3.9, num_rates=100, num_discard=100, jit=True)
    pops = simulate(model=logistic_map, num_gens=200, rate_min=3.7, rate_max=3.9, num_rates=100, num_discard=100, jit=False)

def test_bifurcation_plot():
    pops = simulate(model=logistic_map, num_gens=200, rate_min=0, rate_max=4, num_rates=100, num_discard=100)
    bifurcation_plot(pops, save=False)
    
def test_phase_diagram():
    pops = simulate(model=logistic_map, num_gens=200, rate_min=3.6, rate_max=4.0, num_rates=50, num_discard=100)
    phase_diagram(pops, xmin=0.25, xmax=0.75, ymin=0.8, ymax=1.01, size=7, color='viridis', save=False)

def test_phase_diagram_3d():    
    pops = simulate(model=cubic_map, num_gens=200, rate_min=3.5, num_rates=30, num_discard=100)
    phase_diagram_3d(pops, xmin=-1, xmax=1, ymin=-1, ymax=1, zmin=-1, zmax=1, alpha=0.2, color='viridis', azim=330, save=False)
    
def test_cobweb_plot():
    cobweb_plot(r=3.9, save=False)
    
