.. pynamical documentation master file, created by
   sphinx-quickstart on Tue Jan 31 13:34:32 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pynamical documentation
=======================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   pynamical

pynamical is a Python package for modeling, simulating, visualizing, and animating discrete nonlinear dynamical systems and chaos. It uses pandas, numpy, and numba for fast simulation, and matplotlib for beautiful visualizations and animations to explore system behavior. Compatible with Python 2 and 3.

You can read/cite the journal article about pynamical: Boeing, G. 2016. "`Visual Analysis of Nonlinear Dynamical Systems: Chaos, Fractals, Self-Similarity and the Limits of Prediction`_." *Systems*, 4 (4), 37. doi:10.3390/systems4040037.

Installation
------------

You can install pynamical with conda:

.. code-block:: shell

    conda install -c conda-forge pynamical

Alternatively, you can run pynamical + Jupyter directly from this
`docker container`_, or you can install it with pip:

.. code-block:: shell

    pip install pynamical
    
Examples
--------

For examples and demos, see the GitHub repo: `https://github.com/gboeing/pynamical`_
    
Support
-------

Issue tracker: `https://github.com/gboeing/pynamical/issues`_

License
-------

The project is licensed under the MIT license.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _docker container: https://hub.docker.com/r/gboeing/pynamical
.. _https://github.com/gboeing/pynamical: https://github.com/gboeing/pynamical
.. _https://github.com/gboeing/pynamical/issues: https://github.com/gboeing/pynamical/issues
.. _Visual Analysis of Nonlinear Dynamical Systems\: Chaos, Fractals, Self-Similarity and the Limits of Prediction: http://geoffboeing.com/publications/nonlinear-chaos-fractals-prediction/
