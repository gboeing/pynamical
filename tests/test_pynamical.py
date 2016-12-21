"""
pynamical tests
-------
"""

def test_imports():
    from pynamical import simulate, logistic_map, cubic_map
    from pynamical import bifurcation_plot, cobweb_plot, phase_diagram, phase_diagram_3d
    
def test_simulate():
    import pynamical as pn
    pn.simulate()
    
def test_bifurcation_plot():
    import pynamical as pn
    pn.bifurcation_plot(pn.simulate(), show=False, save=False)
    
def test_phase_diagram_3d():
    import pynamical as pn
    pops = pn.simulate(model=pn.cubic_map, num_gens=200, rate_min=3.5, num_rates=30, num_discard=100)
    pn.phase_diagram_3d(pops, xmin=-1, xmax=1, ymin=-1, ymax=1, zmin=-1, zmax=1, alpha=0.2, color='viridis', azim=330, save=False, show=False)

def test_cobweb_plot():
    import pynamical as pn
    pn.cobweb_plot(r=3.9, save=False, show=False)

