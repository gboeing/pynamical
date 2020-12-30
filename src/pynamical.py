#################################################################################################################
# pynamical
# Description: Model, simulate, and visualize discrete nonlinear dynamical systems and chaos
# Author: Geoff Boeing
# Web: https://geoffboeing.com/
# Code repo: https://github.com/gboeing/pynamical
# Documentation: https://pynamical.readthedocs.io/
#
# The MIT License (MIT)
#
# Copyright (c) 2019 Geoff Boeing https://geoffboeing.com/
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#################################################################################################################

import os, pandas as pd, numpy as np
import matplotlib.pyplot as plt, matplotlib.cm as cm, matplotlib.font_manager as fm
from mpl_toolkits.mplot3d import Axes3D
from numba import jit




def get_title_font(family='Helvetica', style='normal', size=20, weight='normal', stretch='normal'):
    """
    Define fonts to use for image titles.
    
    Arguments
    ---------
    family : string
    style : string
    size : numeric
    weight : string
    stretch : string
    
    Returns
    -------
    matplotlib.font_manager.FontProperties
    """
    
    if family=='Helvetica':
        family = ['Helvetica', 'Arial', 'sans-serif']
    fp = fm.FontProperties(family=family, style=style, size=size, weight=weight, stretch=stretch)
    return fp

def get_label_font(family='Helvetica', style='normal', size=16, weight='normal', stretch='normal'):
    """
    Define fonts to use for image axis labels.
    
    Arguments
    ---------
    family : string
    style : string
    size : numeric
    weight : string
    stretch : string
    
    Returns
    -------
    matplotlib.font_manager.FontProperties
    """
    
    if family=='Helvetica':
        family = ['Helvetica', 'Arial', 'sans-serif']
    fp = fm.FontProperties(family=family, style=style, size=size, weight=weight, stretch=stretch)
    return fp


def save_fig(filename='image', folder='images', dpi=300, bbox_inches='tight', pad=0.1):
    """
    Save the current figure as a file to disk.
    
    Arguments
    ---------
    filename: string
        filename of image file to be saved
    folder: string
        folder in which to save the image file
    dpi: int
        resolution at which to save the image
    bbox_inches: string
        tell matplotlib to figure out the tight bbox of the figure
    pad: float
        inches to pad around the figure
    
    Returns
    -------
    None
    """
    
    if not os.path.exists(folder):
        os.makedirs(folder)
    plt.savefig('{}/{}.png'.format(folder, filename), dpi=dpi, bbox_inches=bbox_inches, pad_inches=pad)

    
    
    
def save_and_show(fig, ax, save, show, filename='image', folder='images', dpi=300, bbox_inches='tight', pad=0.1):
    """
    Consistently handle plot completion by saving then either displaying or returning the figure.
    
    Arguments
    ---------
    fig: matplotlib figure
    ax: matplotlib axis
    save: bool
        whether to save the image to disk, or not
    show: bool
        whether to display the image or instead just return the figure and axis
    filename: string
        filename of image file to be saved
    folder: string
        folder in which to save the image file
    dpi: int
        resolution at which to save the image
    bbox_inches: string
        tell matplotlib to figure out the tight bbox of the figure
    pad: float
        inches to pad around the figure
    
    Returns
    -------
    tuple 
        (fig, ax) if show=False, otherwise returns None
    """
    
    if save:  
        save_fig(filename=filename, folder=folder, dpi=dpi, bbox_inches=bbox_inches, pad=pad)
        
    if show:
        plt.show()   
    else:
        return fig, ax
    
    
    

@jit(cache=True, nopython=True) # pragma: no cover
def logistic_map(pop, rate):
    """
    Define the equation for the logistic map.
    
    Arguments
    ---------
    pop: float
        current population value at time t
    rate: float
        growth rate parameter values
    
    Returns
    -------
    float
        scalar result of logistic map at time t+1
    """
    
    return pop * rate * (1 - pop)
    
    
    

@jit(cache=True, nopython=True) # pragma: no cover 
def cubic_map(pop, rate):
    """
    Define the equation for the cubic map.
    
    Arguments
    ---------
    pop: float
        current population value at time t
    rate: float
        growth rate parameter values
    
    Returns
    -------
    float
        scalar result of cubic map at time t+1
    """
    
    return rate * pop ** 3 + pop * (1 - rate)
    

    
    
@jit(cache=True, nopython=True) # pragma: no cover
def singer_map(pop, rate):
    """
    Define the equation for the singer map.
    
    Arguments
    ---------
    pop: float
        current population value at time t
    rate: float
        growth rate parameter values
    
    Returns
    -------
    float
        scalar result of singer map at time t+1
    """
    
    return rate * (7.86 * pop - 23.31 * pop ** 2 + 28.75 * pop ** 3 - 13.3 * pop ** 4)

    
    
    
def simulate(model=logistic_map, num_gens=50, rate_min=0.5, rate_max=4, num_rates=8, num_discard=0, initial_pop=0.5, jit=True):
    """
    Call simulator (either JIT compiled or not) to create a DataFrame with columns for each growth rate, row labels for each time step, and values computed by the model.
    
    Arguments
    ---------
    model: function
        the function defining an iterated map to simulate; default is the logistic map
    num_gens: int
        number of iterations to run the model
    rate_min: float
        the first growth rate for the model, between 0 and 4
    rate_max: float
        the last growth rate for the model, between 0 and 4
    num_rates: int
        how many growth rates between min and max to run the model on
    num_discard: int
        number of generations to discard before keeping population values
    initial_pop: float
        starting population when you run the model, between 0 and 1
    jit: bool
        if True, use jit compiled simulator function to speed up simulation, if False, use uncompiled simulator function
    
    Returns
    -------
    DataFrame
    """
    
    if jit:
        return simulate_jit(model=model, num_gens=num_gens, rate_min=rate_min, rate_max=rate_max, num_rates=num_rates, num_discard=num_discard, initial_pop=initial_pop)
    else:
        return simulate_no_compile(model=model, num_gens=num_gens, rate_min=rate_min, rate_max=rate_max, num_rates=num_rates, num_discard=num_discard, initial_pop=initial_pop)
    
    
    
    
def simulate_no_compile(model, num_gens, rate_min, rate_max, num_rates, num_discard, initial_pop):
    """
    Create a DataFrame with columns for each growth rate, row labels for each time step, and values computed by the model (without JIT compilation).
    
    Arguments
    ---------
    model: function
        the function defining an iterated map to simulate
    num_gens: int
        number of iterations to run the model
    rate_min: float
        the first growth rate for the model, between 0 and 4
    rate_max: float
        the last growth rate for the model, between 0 and 4
    num_rates: int
        how many growth rates between min and max to run the model on
    num_discard: int
        number of generations to discard before keeping population values
    initial_pop: float
        starting population when you run the model, between 0 and 1
    
    Returns
    -------
    DataFrame
    """
    
    pops = []
    rates = np.linspace(rate_min, rate_max, num_rates)
    
    # for each rate, run the function repeatedly, starting at the initial_pop
    for rate in rates:
        pop = initial_pop
        
        # first run it num_discard times and ignore the results
        for _ in range(num_discard):
            pop = model(pop, rate)
        
        # now that those gens are discarded, run it num_gens times and keep the results
        for _ in range(num_gens):
            pops.append([rate, pop])
            pop = model(pop, rate)
    
    # return a DataFrame with one column for each growth rate and one row for each timestep (aka generation)
    df = pd.DataFrame(data=pops, columns=['rate', 'pop'])
    df.index = pd.MultiIndex.from_arrays([num_rates * list(range(num_gens)), df['rate'].values])
    return df.drop(labels='rate', axis=1).unstack()['pop']

    
    
    
def simulate_jit(model, num_gens, rate_min, rate_max, num_rates, num_discard, initial_pop):
    """
    Create a DataFrame with columns for each growth rate, row labels for each time step, and values computed by the model (with JIT compilation).
    
    You can't pass a jitted function to a jitted function unless you turn off 'nopython' mode (which makes it slow)
    In other words, you can't pass different model functions directly to the simulate function. Instead, use a closure:
    The make_jit_simulator function returns a jitted simulator function that receives the jitted model function,
    without it being an argument passed to the simulator function, because of the closure local scope
    
    Arguments
    ---------
    model: function
        the function defining an iterated map to simulate
    num_gens: int
        number of iterations to run the model
    rate_min: float
        the first growth rate for the model, between 0 and 4
    rate_max: float
        the last growth rate for the model, between 0 and 4
    num_rates: int
        how many growth rates between min and max to run the model on
    num_discard: int
        number of generations to discard before keeping population values
    initial_pop: float
        starting population when you run the model, between 0 and 1
    
    Returns
    -------
    DataFrame
    """
    
    # make the jitted simulator
    jit_simulator = make_jit_simulator(model=model, num_gens=num_gens, rate_min=rate_min, rate_max=rate_max, 
                                       num_rates=num_rates, num_discard=num_discard, initial_pop=initial_pop)
    
    # run the jit_simulator to create the pops to pass to the DataFrame
    pops = jit_simulator()
    
    # return a DataFrame with one column for each growth rate and one row for each timestep (aka generation)
    df = pd.DataFrame(data=pops, columns=['rate', 'pop'])
    df.index = pd.MultiIndex.from_arrays([num_rates * list(range(num_gens)), df['rate'].values])
    return df.drop(labels='rate', axis=1).unstack()['pop']
    
    
    
    
def make_jit_simulator(model, num_gens, rate_min, rate_max, num_rates, num_discard, initial_pop):
    """
    Create a jitted simulator function that receives the jitted model function, without it being an argument passed to the simulator function, because of the closure local scope.
    
    Arguments
    ---------
    model: function
        the function defining an iterated map to simulate
    num_gens: int
        number of iterations to run the model
    rate_min: float
        the first growth rate for the model, between 0 and 4
    rate_max: float
        the last growth rate for the model, between 0 and 4
    num_rates: int
        how many growth rates between min and max to run the model on
    num_discard: int
        number of generations to discard before keeping population values
    initial_pop: float
        starting population when you run the model, between 0 and 1
    
    Returns
    -------
    function
    """
    
    @jit(cache=True, nopython=True) # pragma: no cover
    def jit_simulator(num_gens=num_gens, rate_min=rate_min, rate_max=rate_max, num_rates=num_rates, 
                      num_discard=num_discard, initial_pop=initial_pop):
        
        pops = np.empty(shape=(num_gens*num_rates, 2), dtype=np.float64)
        rates = np.linspace(rate_min, rate_max, num_rates)

        # for each rate, run the function repeatedly, starting at the initial_pop
        for rate_num, rate in zip(range(len(rates)), rates):
            pop = initial_pop

            # first run it num_discard times and ignore the results
            for _ in range(num_discard):
                pop = model(pop, rate)

            # now that those gens are discarded, run it num_gens times and keep the results
            for gen_num in range(num_gens):
                row_num = gen_num + num_gens * rate_num
                pops[row_num] = [rate, pop]
                pop = model(pop, rate)
        
        return pops
    
    return jit_simulator
    
    
    
    
def get_bifurcation_plot_points(pops):
    """
    Convert a DataFrame of values from the model into a set of xy points that you can plot as a bifurcation diagram.
    
    Arguments
    ---------
    pops: DataFrame
        population data output from the model
    
    Returns
    -------
    DataFrame
    """
    
    # create a new DataFrame to contain our xy points
    xy_points = pd.DataFrame(columns=['x', 'y'])
    
    # for each column in the populations DataFrame
    for rate in pops.columns:
        # append the growth rate as the x column and all the population values as the y column
        xy_points = xy_points.append(pd.DataFrame({'x':rate, 'y':pops[rate]}))
    
    # reset the index and drop the old index before returning the xy point data
    xy_points = xy_points.reset_index().drop(labels='index', axis=1)
    return xy_points

    
    
    
def bifurcation_plot(pops, xmin=0, xmax=4, ymin=0, ymax=1, figsize=(10,6),
                     title='Bifurcation Diagram', xlabel='Growth Rate', ylabel='Population', 
                     color='#003399', filename='image', save=True, show=True, title_font=None, label_font=None,
                     folder='images', dpi=300, bbox_inches='tight', pad=0.1):
    """
    Plot the results of the model as a bifurcation diagram.
    
    Arguments
    ---------
    pops: DataFrame
        population data output from the model
    xmin: float
        minimum value on the x axis
    xmax: float
        maximum value on the x axis
    ymin: float
        minimum value on the y axis
    ymax: float
        maximum value on the y axis
    figsize: tuple
        (width, height) of figure
    title: string
        title of the plot
    xlabel: string
        label of the x axis
    ylabel: string
        label of the y axis
    color: string
        color of the points in the scatter plot
    filename: string
        name of image file to be saved, if applicable
    save: bool
        whether to save the image to disk or not
    show: bool
        whether to display the image on screen or not
    title_font: matplotlib.font_manager.FontProperties
        font properties for figure title
    label_font: matplotlib.font_manager.FontProperties
        font properties for axis labels
    folder: string
        folder in which to save the image file
    dpi: int
        resolution at which to save the image
    bbox_inches: string
        tell matplotlib to figure out the tight bbox of the figure
    pad: float
        inches to pad around the figure
    
    Returns
    -------
    tuple 
        (fig, ax) if show=False, otherwise returns None
    """
    
    if title_font is None:
        title_font = get_title_font()
        
    if label_font is None:
        label_font = get_label_font()
    
    # create a new matplotlib figure and axis and set its size
    fig, ax = plt.subplots(figsize=figsize)
    
    # plot the xy data
    points = get_bifurcation_plot_points(pops)
    bifurcation_scatter = ax.scatter(points['x'], points['y'], c=color, edgecolor='None', alpha=1, s=1)
    
    # set x and y limits, title, and x and y labels
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_title(title, fontproperties=get_title_font())
    ax.set_xlabel(xlabel, fontproperties=get_label_font())
    ax.set_ylabel(ylabel, fontproperties=get_label_font())
    
    return save_and_show(fig=fig, ax=ax, save=save, show=show, filename=filename, folder=folder, dpi=dpi, bbox_inches=bbox_inches, pad=pad)


    
    
def get_phase_colors(color_request, length=1, color_reverse=False, default_color='#003399'):
    """
    Return a list of colors based on a request that could be a list, string color name, or string colormap name.
    
    Arguments
    ---------
    color_request: string or list
        what color the caller wants, could be a list, string color name, or string colormap name
    length: int
        how many total colors to return in the list
    color_reverse: bool
        reverse the returned list of colors if True
    default_color: string
        if the list is shorter than the specified length, pad it out with default_color
    
    Returns
    -------
    list
    """
    
    color_list = []
    if isinstance(color_request, list):
        # if they passed a list, then just use it
        color_list = color_request
        
    elif isinstance(color_request, str):
        # if they passed a string, it could be a color name or a colormap name
        if len(color_request) == 1 or color_request.startswith('#'):
            # if it's only 1 character long or starts with a #, then it's a color name or hex code
            color_list = [color_request]
            default_color = color_request
        else:
            # if it's more than 1 character and doesn't start with #, then it's the name of a colormap
            color_map = cm.get_cmap(color_request)
            color_list = color_map([x/float(length) for x in range(length)]).tolist()
            
    # make sure list is same length as specified in length argument - if not, pad it out with default_color, that way, each scatterplot gets a color
    color_list = color_list + [default_color for n in range(length-len(color_list))] if len(color_list) < length else color_list
    
    # if the color_reverse=True, reverse the list of colors before returning it
    if color_reverse:
        color_list.reverse()
    
    return color_list

    
    
    
def get_phase_diagram_points(pops, discard_gens=1, dimensions=2):
    """
    Convert a DataFrame of values from the model into a set of xy(z) points to plot.
    
    Arguments
    ---------
    pops: DataFrame
        population data output from the model
    discard_gens: int
        number of rows to discard before keeping points to plot
    dimensions: int
        {2, 3}, number of dimensions specifying if we want points for a 2-D or 3-D plot: (t, t+1) vs (t, t+1, t+2)
    
    Returns
    -------
    DataFrame
    """

    # drop the first row by default because every run has the same starting value, it leaves a visual artifact
    # if specified by the argument, drop the initial n rows to show only the eventual attractor the system settles on
    if discard_gens > 0 and len(pops) > discard_gens:
        discard_gens = np.arange(0, discard_gens)
        pops = pops.drop(labels=pops.index[discard_gens])
        pops = pops.reset_index().drop(labels='index', axis=1)

    # a point is defined by the name of its model run then its spatial coordinates
    points = []
    point_columns = ['name', 'x', 'y', 'z']
    
    # for each column in the populations DataFrame, where the label is the 'name' of the model run
    for name in pops.columns:
        
        # for each row in the column
        for label, row in pops.iterrows():
            
            # we can only create points up up to row dimensions-1 because we need future time steps to create each point
            if label < len(pops)-(dimensions-1):
                
                point = [name]
                for n in range(dimensions):
                    # append the value at the current time (aka row) as x, t+1 as y (and t+2 as z if dimensions=3)
                    point.append(pops[name][label + n])
                
                # append this point to the list of points
                points.append(point)
    
    # convert the list of points to a MultiIndex DataFrame 
    # with a level in the index called 'name' to represent each model run
    df = pd.DataFrame(points, columns=point_columns[0:dimensions+1])
    df.index = pd.MultiIndex.from_tuples(list(zip(df['name'], df.index)), names=['name', ''])
    df = df.drop(labels='name', axis=1)
    return df
    
    
    
    
def phase_diagram(pops, discard_gens=0, figsize=(6,6), xmin=0, xmax=1, ymin=0, ymax=1,
                  title='', xlabel='Population (t)', ylabel='Population (t + 1)',
                  marker='.', size=5, alpha=0.7, color='#003399', color_reverse=False, legend=False, 
                  filename='image', save=True, show=True, title_font=None, label_font=None,
                  folder='images', dpi=300, bbox_inches='tight', pad=0.1):
    """
    Draw a 2D phase diagram for one or more time series by plotting the value at time t on the x-axis and the value at t+1 on the y-axis.
    
    Arguments
    ---------
    pops: DataFrame
        population data output from the model
    discard_gens: int
        number of rows to discard before keeping points to plot
    figsize: tuple
        (width, height) of figure
    xmin: float
        minimum value on the x axis
    xmax: float
        maximum value on the x axis
    ymin: float
        minimum value on the y axis
    ymax: float
        maximum value on the y axis
    title: string
        title of the plot
    xlabel: string
        label of the x axis
    ylabel: string
        label of the y axis
    marker: string
        the type of point to use in the plot
    size: float
        the size of the marker
    alpha: float
        the opacity of the marker
    color: string
        color of the points in the scatter plot
    color_reverse: bool
        reverse the returned list of colors if True
    legend: bool
        if we should display a legend or not
    filename: string
        name of image file to be saved, if applicable
    save: bool
        whether to save the image to disk or not
    show: bool
        whether to display the image on screen or not
    title_font: matplotlib.font_manager.FontProperties
        font properties for figure title
    label_font: matplotlib.font_manager.FontProperties
        font properties for axis labels
    folder: string
        folder in which to save the image file
    dpi: int
        resolution at which to save the image
    bbox_inches: string
        tell matplotlib to figure out the tight bbox of the figure
    pad: float
        inches to pad around the figure
    
    Returns
    -------
    tuple 
        (fig, ax) if show=False, otherwise returns None
    """
    
    if title_font is None:
        title_font = get_title_font()
        
    if label_font is None:
        label_font = get_label_font()
        
    # first get the xy points to plot
    points = get_phase_diagram_points(pops, discard_gens, dimensions=2)
    plots = []
    
    # get_phase_diagram_points() returns a MultiIndexed DataFrame, each run of the model has its own 'name' in the index
    index = points.index.get_level_values('name')
    names = np.unique(index)
    
    # create a new matplotlib figure and axis and set its size
    fig, ax = plt.subplots(figsize=figsize)
    
    # set the plot title, x- and y-axis limits, and x- and y-axis labels
    ax.set_title(title, fontproperties=get_title_font())
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_xlabel(xlabel, fontproperties=get_label_font())
    ax.set_ylabel(ylabel, fontproperties=get_label_font())
    
    # make sure we have a list of colors as long as the number of model runs
    color_list = get_phase_colors(color, len(names), color_reverse)
        
    # plot the xy data for each run of the model that appears in the MultiIndex
    for n in range(len(names)):
        xy = points.iloc[index == names[n]]
        plots.append(ax.scatter(xy['x'], xy['y'], marker=marker, c=[color_list[n]], edgecolor='none', s=size, alpha=alpha))
        
    # add a legend if argument is True
    if legend:
        ax.legend(plots, names.tolist(), loc=1, frameon=True, framealpha=1)
    
    if filename == '':
        filename = title.replace(' ', '-').replace('=', '-').replace(',', '-').replace('.', '').replace('--', '-')
    
    return save_and_show(fig=fig, ax=ax, save=save, show=show, filename=filename, folder=folder, dpi=dpi, bbox_inches=bbox_inches, pad=pad)
    
    
    
    
def phase_diagram_3d(pops, discard_gens=0, figsize=(10,8), xmin=0, xmax=1, ymin=0, ymax=1, zmin=0, zmax=1,
                     remove_ticks=True, title='', elev=25, azim=240, dist=10,
                     xlabel='Population (t)', ylabel='Population (t + 1)', zlabel='Population (t + 2)',
                     marker='.', size=5, alpha=0.7, color='#003399', color_reverse=False, legend=False, 
                     legend_bbox_to_anchor=None, filename='image', save=True, show=True, title_font=None, label_font=None,
                     folder='images', dpi=300, bbox_inches='tight', pad=0.1):
    """
    Draw a 3D phase diagram for one or more time series by plotting the value at time t on the x-axis, the value at t+1 on the y-axis, and the value of t+2 on the z-axis.
    
    Arguments
    ---------
    pops: DataFram
        population data output from the model
    discard_gens: int
        number of rows to discard before keeping points to plot
    figsize: tuple
        (width, height) of figure
    xmin: float
        minimum value on the x axis
    xmax: float
        maximum value on the x axis
    ymin: float
        minimum value on the y axis
    ymax: float
        maximum value on the y axis
    zmin: float
        minimum value on the z axis
    zmax: float
        maximum value on the z axis 
    remove_ticks: bool
        remove axis ticks or not
    title: string
        title of the plot
    elev: float
        the elevation of the viewing perspective
    azim: float
        the azimuth of the viewing perspective
    dist: float
        the distance of the viewing perspective
    xlabel: string
        label of the x axis
    ylabel: string
        label of the y axis
    zlabel: string
        label of the z axis
    marker: string
        the type of point to use in the plot
    size: float
        the size of the marker
    alpha: float
        the opacity of the marker
    color: string
        color of the points in the scatter plot
    color_reverse: bool
        reverse the returned list of colors if True
    legend: bool
        if we should display a legend or not
    legend_bbox_to_anchor: float
        amount to offset the legend from its natural position
    filename: string
        name of image file to be saved, if applicable
    save: bool
        whether to save the image to disk or not
    show: bool
        whether to display the image on screen or not
    title_font: matplotlib.font_manager.FontProperties
        font properties for figure title
    label_font: matplotlib.font_manager.FontProperties
        font properties for axis labels
    folder: string
        folder in which to save the image file
    dpi: int
        resolution at which to save the image
    bbox_inches: string
        tell matplotlib to figure out the tight bbox of the figure
    pad: float
        inches to pad around the figure
    
    Returns
    -------
    tuple 
    (fig, ax) if show=False, otherwise returns None
    """
    
    if title_font is None:
        title_font = get_title_font()
        
    if label_font is None:
        label_font = get_label_font()
        
    # first get the xyz points to plot
    points = get_phase_diagram_points(pops, discard_gens, dimensions=3)
    plots = []
    
    # get_phase_diagram_points() returns a MultiIndexed DataFrame, each run of the model has its own 'name' in the index
    index = points.index.get_level_values('name')
    names = np.unique(index)
    
    # create a new figure, set its size, and create an axis with a 3-D projection
    fig = plt.figure(figsize=figsize)
    ax = fig.gca(projection='3d')
    ax.xaxis.set_pane_color((1,1,1,1))
    ax.yaxis.set_pane_color((1,1,1,1))
    ax.zaxis.set_pane_color((1,1,1,1))

    # configure the perspective from which to view the 3D plot
    ax.elev = elev
    ax.azim = azim
    ax.dist = dist
    
    # set the plot title, axis limits, and axis labels
    ax.set_title(title, fontproperties=get_title_font())
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_zlim(zmin, zmax)
    ax.set_xlabel(xlabel, fontproperties=get_label_font())
    ax.set_ylabel(ylabel, fontproperties=get_label_font())  
    ax.set_zlabel(zlabel, fontproperties=get_label_font())
    
    #remove all ticks if argument is True
    if remove_ticks:
        ax.tick_params(reset=True, axis='both', which='both', pad=0, width=0, length=0,
                       bottom=False, top=False, left=False, right=False, 
                       labelbottom=False, labeltop=False, labelleft=False, labelright=False)
    else:
        ax.tick_params(reset=True)
        
    # make sure we have a list of colors as long as the number of model runs
    color_list = get_phase_colors(color, len(names), color_reverse)
    
    # plot the xyz data for each run of the model that appears in the MultiIndex
    for n in range(len(names)):
        xyz = points.iloc[index == names[n]]
        plots.append(ax.scatter(xyz['x'], xyz['y'], xyz['z'], 
                                marker=marker, c=[color_list[n]], edgecolor=[color_list[n]], s=size, alpha=alpha))
        
    # add a legend if argument is True
    if legend:
        ax.legend(plots, names.tolist(), loc=1, frameon=True, framealpha=1, bbox_to_anchor=legend_bbox_to_anchor)
    
    if filename == '':
        filename = title.replace(' ', '-').replace('=', '-').replace(',', '-').replace('.', '').replace('--', '-')
    
    return save_and_show(fig=fig, ax=ax, save=save, show=show, filename=filename, folder=folder, dpi=dpi, bbox_inches=bbox_inches, pad=pad)
    

    
    
def get_cobweb_points(model, r, x, n):
    """
    Calculate the vertices of cobweb lines for a cobweb plot. 
        
    Steps in the calculation:
    1) Let x = 0.5
    2) Start on the x-axis at the point (x, 0).
    3) Draw a vertical line to the red function curve: this point has the coordinates (x, f(x)).
    4) Draw a horizontal line from this point to the gray diagonal line: this point has the coordinates (f(x), f(x)).
    5) Draw a vertical line from this point to the red function curve: this point has the coordinates (f(x), f(f(x))).
    6) Repeat steps 4 and 5 recursively one hundred times.
    
    Arguments
    ---------
    model: function
        defining an iterated map to simulate
    r: float
        growth rate parameter value to pass to the map
    x: float
        starting population value
    n: int
        number of iterations to run
    
    Returns
    -------
    tuple
        cobweb_x_vals, cobweb_y_vals
    """
    
    cobweb_points = [(x, 0)]
    for _ in range(n):
        y1 = model(x, r)
        cobweb_points.append((x, y1))
        cobweb_points.append((y1, y1))
        y2 = model(y1, r)
        cobweb_points.append((y1, y2))
        x = y1
    return zip(*cobweb_points)
    
    
    
    
def get_function_points(model, r, n, start, end):
    """
    Calculate model results for n population values evenly spaced between start and end values.
    
    Arguments
    ---------
    model: function
        defining an iterated map to simulate
    r: float
        growth rate parameter value to pass to the map
    n: int
        number of iterations to run
    start: float
        lower limit of the function range
    end: float
        upper limit of the function range
    
    Returns
    -------
    tuple
        x_vals, y_vals
    """
    
    x_vals = np.linspace(start, end, n)
    y_vals = [model(x, r) for x in x_vals]
    return x_vals, y_vals
    
    

    
def cobweb_plot(model=logistic_map, r=0, function_n=1000, cobweb_n=100, cobweb_x=0.5, num_discard=0, title='', filename='', show=True, save=True,
                start=0, end=1, figsize=(6,6), diagonal_linewidth=1.35, cobweb_linewidth=1, function_linewidth=1.5, title_font=None, label_font=None,
                folder='images', dpi=300, bbox_inches='tight', pad=0.1):
    """
    Draw a cobweb plot. 
    
    Run the map once each for 1000 population values evenly spaced between 0 and 1. 
    This gives us the results of the equation (y values) across the entire range of 
    possible population values (x values). The gray diagonal line is just a plot of y=x.
    
    Arguments
    ---------
    model: function
        defining an iterated map to simulate
    r: float
        growth rate parameter value to pass to the map
    function_n: int
        number of iterations of the function to run
    cobweb_n: int
        number of iterations of the cobweb line to run
    num_discard: int
        how many initial iterations of the cobweb line to throw away
    title: string
        title of the plot
    filename: string
        name of image file to be saved, if applicable
    save: bool
        whether to save the image to disk or not
    show: bool
        whether to display the image on screen or not
    start: float
        lower limit of the function range
    end: float
        upper limit of the function range
    figsize: tuple
        (width, height) of figure
    diagonal_linewidth: float
        width of y=x line
    cobweb_linewidth: float
        width of cobweb line
    function_linewidth: float
        width of function line
    title_font: matplotlib.font_manager.FontProperties
        font properties for figure title
    label_font: matplotlib.font_manager.FontProperties
        font properties for axis labels
    folder: string
        folder in which to save the image file
    dpi: int
        resolution at which to save the image
    bbox_inches: string
        tell matplotlib to figure out the tight bbox of the figure
    pad: float
        inches to pad around the figure
    
    Returns
    -------
    tuple
        (fig, ax) if show=False, otherwise returns None
    """
    
    if title_font is None:
        title_font = get_title_font()
        
    if label_font is None:
        label_font = get_label_font()
        
    func_x_vals, func_y_vals = get_function_points(model=model, r=r, n=function_n, start=start, end=end)
    cobweb_x_vals, cobweb_y_vals = get_cobweb_points(model=model, r=r, x=cobweb_x, n=cobweb_n)
    cobweb_x_vals = cobweb_x_vals[num_discard:]
    cobweb_y_vals = cobweb_y_vals[num_discard:]
    
    fig, ax = plt.subplots(figsize=figsize)
    diagonal_line = ax.plot((0,1), (0,1), color='gray', linewidth=diagonal_linewidth)
    function_line = ax.scatter(func_x_vals, func_y_vals, color='#cc0000', edgecolor='None', s=function_linewidth)
    cobweb_line = ax.plot(cobweb_x_vals, cobweb_y_vals, color='#003399', linewidth=cobweb_linewidth)
    
    ax.set_ylim((0, 1))
    ax.set_xlim((0, 1))
    if title == '':
        title = 'Cobweb Plot, r={}'.format(r)
    ax.set_title(title, fontproperties=get_title_font())
    
    if filename == '':
        filename = 'cobweb-plot-r{}-x{}'.format(r, cobweb_x).replace('.', '')
    
    return save_and_show(fig=fig, ax=ax, save=save, show=show, filename=filename, folder=folder, dpi=dpi, bbox_inches=bbox_inches, pad=pad)
    
    
    
    