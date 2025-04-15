"""Install pynamical."""

import os

from setuptools import setup

# provide a long description using reStructuredText
LONG_DESCRIPTION = r"""
**pynamical** is a Python package for modeling, simulating, visualizing, and animating discrete
nonlinear dynamical systems and chaos. pynamical uses pandas, numpy, and numba for fast simulation,
and matplotlib for beautiful visualizations and animations to explore system behavior. See the
examples and demos on `GitHub`_.

You can read/cite the journal article about pynamical: Boeing, G. 2016.
"`Visual Analysis of Nonlinear Dynamical Systems: Chaos, Fractals, Self-Similarity and the Limits of Prediction`_."
*Systems*, 4 (4), 37. doi:10.3390/systems4040037.

.. _GitHub: https://github.com/gboeing/pynamical
.. _Visual Analysis of Nonlinear Dynamical Systems\: Chaos, Fractals, Self-Similarity and the Limits of Prediction: http://geoffboeing.com/publications/nonlinear-chaos-fractals-prediction/
"""

# list of classifiers from the PyPI classifiers trove
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Intended Audience :: Education",
    "Intended Audience :: Science/Research",
    "Topic :: Scientific/Engineering :: GIS",
    "Topic :: Scientific/Engineering :: Visualization",
    "Topic :: Scientific/Engineering :: Physics",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
]

# only specify install_requires if not in RTD environment
if os.getenv("READTHEDOCS") == "True":
    INSTALL_REQUIRES = []
else:
    with open("requirements.txt") as f:
        INSTALL_REQUIRES = [line.strip() for line in f.readlines()]

setup(
    name="pynamical",
    version="0.3.3",
    description="Model, simulate, and visualize discrete nonlinear dynamical systems",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    classifiers=CLASSIFIERS,
    url="https://github.com/gboeing/pynamical",
    author="Geoff Boeing",
    author_email="boeing@usc.edu",
    license="MIT",
    platforms="any",
    packages=["pynamical"],
    python_requires=">=3.8",
    install_requires=INSTALL_REQUIRES,
)
