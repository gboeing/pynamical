from setuptools import setup

# provide a long description using reStructuredText
long_description = """
**pynamical** is a Python package for modeling, simulating, visualizing, and animating discrete 
nonlinear dynamical systems and chaos. pynamical uses pandas, numpy, and numba for fast simulation, 
and matplotlib for beautiful visualizations and animations to explore system behavior. Compatible 
with Python 2 and 3. See the examples and demos on `GitHub`_.

You can read/cite the journal article about pynamical: Boeing, G. 2016. 
"`Visual Analysis of Nonlinear Dynamical Systems: Chaos, Fractals, Self-Similarity and the Limits of Prediction`_." 
*Systems*, 4 (4), 37. doi:10.3390/systems4040037.

.. _GitHub: https://github.com/gboeing/pynamical
.. _Visual Analysis of Nonlinear Dynamical Systems\: Chaos, Fractals, Self-Similarity and the Limits of Prediction: http://geoffboeing.com/publications/nonlinear-chaos-fractals-prediction/
"""

# list of classifiers from the PyPI classifiers trove
classifiers=['Development Status :: 5 - Production/Stable',
             'License :: OSI Approved :: MIT License',
             'Operating System :: OS Independent',
             'Intended Audience :: Science/Research',
             'Intended Audience :: Education',
             'Topic :: Scientific/Engineering :: Mathematics',
             'Topic :: Scientific/Engineering :: Visualization',
             'Topic :: Scientific/Engineering :: Physics',
             'Topic :: Scientific/Engineering :: Information Analysis',
             'Programming Language :: Python',
             'Programming Language :: Python :: 2',
             'Programming Language :: Python :: 3',
             'Programming Language :: Python :: 2.7',
             'Programming Language :: Python :: 3.5',
             'Programming Language :: Python :: 3.6',
             'Programming Language :: Python :: 3.7']

setup(name='pynamical',
      version='0.2.1',
      description='Model, simulate, and visualize discrete nonlinear dynamical systems',
      long_description=long_description,
      classifiers=classifiers,
      url='https://github.com/gboeing/pynamical',
      author='Geoff Boeing',
      author_email='g.boeing@northeastern.edu',
      license='MIT',
      platforms='any',
      packages=['pynamical'],
      install_requires=['pandas>=0.24',
                        'numpy>=1.15',
                        'matplotlib>=2.2',
                        'numba>=0.39'])
                        