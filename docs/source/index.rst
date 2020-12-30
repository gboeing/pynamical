pynamical |version|
===================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   pynamical

**pynamical** is a Python package for modeling, simulating, visualizing, and animating discrete nonlinear dynamical systems and chaos. It uses pandas, numpy, and numba for fast simulation, and matplotlib for beautiful visualizations and animations to explore system behavior.

**Citation information**: Boeing, G. 2016. "`Visual Analysis of Nonlinear Dynamical Systems: Chaos, Fractals, Self-Similarity and the Limits of Prediction`_." *Systems*, 4 (4), 37. doi:10.3390/systems4040037.


Installation
------------

You can install pynamical with conda:

.. code-block:: shell

    conda config --prepend channels conda-forge
    conda create -n pynamical --strict-channel-priority jupyterlab pynamical

Alternatively, you can run pynamical + Jupyter directly from its `Docker container`_, or you can install it with pip.


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
