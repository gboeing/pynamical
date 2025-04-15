[![PyPI Version](https://badge.fury.io/py/pynamical.svg)](https://badge.fury.io/py/pynamical)
[![Anaconda Downloads](https://anaconda.org/conda-forge/pynamical/badges/downloads.svg)](https://anaconda.org/conda-forge/pynamical)
[![Documentation](https://readthedocs.org/projects/pynamical/badge/?version=latest)](https://pynamical.readthedocs.io/)
[![Tests](https://github.com/gboeing/pynamical/actions/workflows/tests.yml/badge.svg)](https://github.com/gboeing/pynamical/actions/workflows/tests.yml)
[![Coverage](https://codecov.io/gh/gboeing/pynamical/branch/main/graph/badge.svg)](https://codecov.io/gh/gboeing/pynamical)

# pynamical

**Python package for modeling, simulating, visualizing, and animating discrete nonlinear dynamical systems and chaos**

Pynamical uses pandas, numpy, and numba for fast simulation, and matplotlib for visualizations and animations to explore system behavior.

Pynamical comes packaged with the logistic map, the Singer map, and the cubic map predefined. The models may be run with a range of parameter values over a set of time steps, and the resulting numerical output is returned as a pandas DataFrame. Pynamical can then visualize this output in various ways, including with bifurcation diagrams, two-dimensional phase diagrams, three-dimensional phase diagrams, and cobweb plots.

**Citation info**: Boeing, G. 2016. "[Visual Analysis of Nonlinear Dynamical Systems: Chaos, Fractals, Self-Similarity and the Limits of Prediction](https://geoffboeing.com/publications/nonlinear-chaos-fractals-prediction/)." *Systems*, 4 (4), 37. doi:10.3390/systems4040037.

## Install:

You can install pynamical with [conda](https://anaconda.org/conda-forge/pynamical):

```
conda config --prepend channels conda-forge
conda create -n pynamical --strict-channel-priority jupyterlab pynamical
```

Alternatively, you can run pynamical + Jupyter directly from its [Docker container](https://hub.docker.com/r/gboeing/pynamical), or you can install it with pip.

## Documentation:

Available on [readthedocs](https://pynamical.readthedocs.io/).

## Demos/tutorial:
  1. [Pynamical: quick overview](examples/pynamical-quick-overview.ipynb)
  1. [Pynamical: the logistic model and bifurcation diagrams](examples/pynamical-demo-logistic-model.ipynb)
  1. [Pynamical: 2D and 3D phase diagrams](examples/pynamical-demo-phase-diagrams.ipynb)
  1. [Pynamical: static and animated cobweb plots](examples/pynamical-demo-cobweb-plots.ipynb)
  1. [Pynamical: animated 3D phase diagrams](examples/pynamical-demo-3d-animation.ipynb)
  1. [Pynamical: demonstrating other models](examples/pynamical-demo-other-models.ipynb)

## Quick walkthrough:

First import pynamical. Then simulate some model and visualize its bifurcation diagram in just 2 lines of code:

```python
from pynamical import logistic_map, simulate, bifurcation_plot
pops = simulate(model=logistic_map, num_gens=100, rate_min=0, rate_max=4, num_rates=1000, num_discard=100)
bifurcation_plot(pops)
```

![](examples/readme/logistic-map-bifurcation-1.png)

Zoom into a slice of this bifurcation diagram to see its [fractal structure](examples/pynamical-demo-logistic-model.ipynb):

```python
pops = simulate(model=logistic_map, num_gens=100, rate_min=3.7, rate_max=3.9, num_rates=1000, num_discard=100)
bifurcation_plot(pops, xmin=3.7, xmax=3.9)
```
![](examples/readme/logistic-map-bifurcation-3.png)

Plot a two-dimensional [phase diagram](examples/pynamical-demo-phase-diagrams.ipynb) of the logistic map:

```python
from pynamical import phase_diagram
pops = simulate(model=logistic_map, num_gens=4000, rate_min=3.6, rate_max=4.0, num_rates=50, num_discard=100)
phase_diagram(pops, xmin=0.25, xmax=0.75, ymin=0.8, ymax=1.01, size=7, color='viridis')
```

![](examples/readme/logisitic-map-2d-phase.png)

Or a three-dimensional phase diagram of the [cubic map](examples/pynamical-demo-other-models.ipynb):

```python
from pynamical import cubic_map, phase_diagram_3d
pops = simulate(model=cubic_map, num_gens=3000, rate_min=3.5, num_rates=30, num_discard=100)
phase_diagram_3d(pops, xmin=-1, xmax=1, ymin=-1, ymax=1, zmin=-1, zmax=1, alpha=0.2, color='viridis', azim=330)
```

![](examples/readme/cubic-map-3d-phase.png)

Animate the 3D phase diagram of the logistic map [to reveal](examples/pynamical-demo-3d-animation.ipynb) the strange attractor's structure:

![](examples/readme/05-logistic-3d-phase-diagram-chaotic-regime.gif)

Animate a cobweb plot of the logistic map's parameter space [to explore](examples/pynamical-demo-cobweb-plots.ipynb) sensitivity and behavior:

![](examples/readme/animated-logistic-cobweb.gif)

Or define your [own model](https://github.com/gboeing/pynamical/blob/main/examples/pynamical-demo-other-models.ipynb) and simulate it with pynamical.
