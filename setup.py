from setuptools import setup
setup(name='pynamical',
      version='0.1',
      description='Model, simulate, and visualize discrete nonlinear dynamical systems',
      url='https://github.com/gboeing/pynamical',
      author='Geoff Boeing',
      author_email='gboeing@berkeley.edu',
      license='MIT',
      packages=['pynamical'],
      install_requires=['pandas>=0.19',
                        'numpy>=1.11',
                        'matplotlib>=1.5',
                        'numba>=0.29'])