---
title: 'Pynamical: Model and visualize discrete nonlinear dynamical systems, chaos, and fractals'
tags:
  - math
  - physics
  - chaos
  - nonlinear
  - fractal
  - logistic map
  - visualization
  - modeling
  - simulation
authors:
  - name: Geoff Boeing
    orcid: 0000-0003-1851-6411
    affiliation: 1
affiliations:
  - name: University of California, Berkeley
    index: 1
date: 20 June 2018
bibliography: paper.bib
repository: https://github.com/gboeing/pynamical
---

# Summary

Pynamical is an educational Python package for introducing the modeling, simulation, and visualization of discrete nonlinear dynamical systems and chaos, focusing on one-dimensional maps (such as the logistic map and the cubic map). Pynamical facilitates defining discrete one-dimensional nonlinear models as Python functions with just-in-time compilation for fast simulation. It comes packaged with the logistic map, the Singer map, and the cubic map predefined. The models may be run with a range of parameter values over a set of time steps, and the resulting numerical output is returned as a pandas DataFrame. Pynamical can then visualize this output in various ways, including with bifurcation diagrams [@may_simple_1976], two-dimensional phase diagrams [@packard_geometry_1980], three-dimensional phase diagrams, and cobweb plots [@hofstadter_mathematical_1985]. These visualizations enable simple qualitative assessments of system behavior including phase transitions [@feigenbaum_universal_1983], bifurcation points [@sander_many_2015], attractors and limit cycles [@grebogi_chaos_1987], basins of attraction [@sprott_classifying_2015], and fractals [@mandelbrot_how_1967; @mandelbrot_fractal_1983].

Although most real-world systems are nonlinear dynamical systems, their mathematical analysis is notoriously difficult because they cannot be simply broken down into individual parts then recombined linearly [@strogatz_nonlinear_2014]. Instead, researchers have long relied on visualization techniques to make system behavior comprehensible [@alpigini_dynamical_2004; @layek_introduction_2015]. Such visualization is useful for exploring nonlinear time series data [@bradley_nonlinear_2015; @boeing_visual_2016]. Pynamical facilitates the modeling, visualization, and exploration of this rich nonlinear behavior, as demonstrated in Figures 1 and 2. Accordingly this package has various applications in research, engineering, and particularly pedagogy. For instance, it allows students to explore and model any well-defined discrete nonlinear dynamical system (with just one line of code) and then simulate its behavior over *n* generations in time (with just one more line of code). This facilitates easy experimentation in parameter space and sensitivity analysis. Moreover, Pynamical easily produces publication-quality visualizations to illustrate findings without having to reinvent the wheel with ad hoc algorithms to produce, reshape, and plot simulation data. Finally, it enables the animation of such systems, to explore and present their qualitative behavior and evolution.

The latest release of the software can be installed via `conda` or `pip` and full documentation can be found at https://pynamical.readthedocs.io.

# Statement of Need

These visualization methods are useful for introducing nonlinearity to students, and Pynamical fills a current need: the existing software landscape typically requires that such tools either a) be developed ad hoc from scratch or b) exist as add-ons to expensive closed-source commercial packages like MATLAB [@tomida_matlab_2008]. Pynamical addresses the need for a fast, simple, extensible, free, and open-source Python package for the analysis of such systems in natural and social science education and research. It depends on the pandas, numpy, numba, and matplotlib Python packages for fast simulation and attractive visualizations to explore system behavior. This software was developed for two purposes: 1) as a pedagogy tool and 2) to produce figures, diagrams, and animations. It has been used in the classroom to introduce students to the basics of nonlinearity, unpredictable system behavior, simple parameter space exploration, and the geometric logic of fractals. This has proven particularly useful for students outside the traditional domains of mathematics and physics to approach these topics that are also relevant to the social sciences, such as modeling and understanding systems and patterns in geography and urban planning. As it focuses primarily on one-dimensional maps, this software could be most useful at the beginning of an introductory course on dynamical systems (e.g., following Strogatz's textbook [@strogatz_nonlinear_2014]). It can also be used to generate publication-quality figures for lessons and tutorials, as well as animated visualizations of system behavior and patterns.

![Figure 1. Bifurcation diagram of the logistic map's chaotic regime.](figure_01.png)
*Figure 1. Bifurcation diagram of the logistic map's chaotic regime.*

![Figure 2. Phase diagram of the logistic map's chaotic regime.](figure_02.png)
*Figure 2. Phase diagram of the logistic map's chaotic regime.*

# References
