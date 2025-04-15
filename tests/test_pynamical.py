"""
pynamical tests
"""

import matplotlib as mpl

mpl.use("Agg")  # use agg backend so you don't need a display on travis

import matplotlib.cm as cm
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from numba import jit

from pynamical import bifurcation_plot
from pynamical import cobweb_plot
from pynamical import cubic_map
from pynamical import logistic_map
from pynamical import phase_diagram
from pynamical import phase_diagram_3d
from pynamical import simulate
from pynamical import singer_map

_img_folder = ".temp"


def test_simulate():

    pops = simulate(
        model=logistic_map,
        num_gens=200,
        rate_min=3.7,
        rate_max=3.9,
        num_rates=100,
        num_discard=100,
        jit=True,
    )
    assert isinstance(pops, pd.DataFrame)
    assert pops.shape == (200, 100)

    pops = simulate(
        model=logistic_map,
        num_gens=200,
        rate_min=3.7,
        rate_max=3.9,
        num_rates=100,
        num_discard=100,
        jit=False,
    )
    assert isinstance(pops, pd.DataFrame)
    assert pops.shape == (200, 100)


def test_bifurcation_plot():

    pops = simulate(
        model=logistic_map, num_gens=200, rate_min=0, rate_max=4, num_rates=100, num_discard=100
    )
    assert isinstance(pops, pd.DataFrame)
    assert pops.shape == (200, 100)

    # returns None
    bifurcation_plot(pops, save=True, folder=_img_folder, filename="")


def test_phase_diagram():

    pops = simulate(
        model=singer_map, num_gens=200, rate_min=3.6, rate_max=4.0, num_rates=50, num_discard=100
    )
    assert isinstance(pops, pd.DataFrame)
    assert pops.shape == (200, 50)

    # returns None
    phase_diagram(
        pops,
        xmin=0.25,
        xmax=0.75,
        ymin=0.8,
        ymax=1.01,
        size=7,
        discard_gens=10,
        color="b",
        color_reverse=True,
        legend=True,
        save=False,
        folder=_img_folder,
        filename="",
    )

    fig_ax = phase_diagram(
        pops,
        xmin=0.25,
        xmax=0.75,
        ymin=0.8,
        ymax=1.01,
        size=7,
        discard_gens=10,
        color=["b", "g"],
        legend=True,
        save=False,
        show=False,
        folder=_img_folder,
        filename="",
    )
    assert isinstance(fig_ax, tuple)


def test_phase_diagram_3d():

    pops = simulate(model=cubic_map, num_gens=200, rate_min=3.5, num_rates=30, num_discard=100)
    assert isinstance(pops, pd.DataFrame)
    assert pops.shape == (200, 30)

    # returns None
    phase_diagram_3d(
        pops,
        xmin=-1,
        xmax=1,
        ymin=-1,
        ymax=1,
        zmin=-1,
        zmax=1,
        alpha=0.2,
        color="viridis",
        azim=330,
        legend=True,
        save=False,
        folder=_img_folder,
        filename="",
    )

    # returns None
    phase_diagram_3d(
        pops,
        xmin=-1,
        xmax=1,
        ymin=-1,
        ymax=1,
        zmin=-1,
        zmax=1,
        alpha=0.2,
        color="inferno",
        azim=330,
        legend=True,
        remove_ticks=False,
        save=False,
        folder=_img_folder,
        filename="",
    )


def test_cobweb_plot():

    # returns None
    cobweb_plot(r=3.9, save=False, folder=_img_folder, filename="")
