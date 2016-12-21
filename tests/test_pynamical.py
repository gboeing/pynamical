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
