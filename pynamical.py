import pandas as pd, numpy as np, matplotlib.pyplot as plt
import matplotlib.cm as cm, matplotlib.font_manager as fm


# define the fonts to use for plots
family = 'Myriad Pro'
title_font = fm.FontProperties(family=family, style='normal', size=20, weight='normal', stretch='normal')
label_font = fm.FontProperties(family=family, style='normal', size=16, weight='normal', stretch='normal')
ticks_font = fm.FontProperties(family=family, style='normal', size=12, weight='normal', stretch='normal')
annot_font = fm.FontProperties(family=family, style='normal', size=12, weight='normal', stretch='normal')

# function to save plots to disk
def save_fig(plt, filename='image', dpi=96, bbox_inches='tight', pad=0.1):
    plt.savefig('images/{}.png'.format(filename), dpi=dpi, bbox_inches=bbox_inches, pad_inches=pad)

# function returns the result of logistic map: pop[t + 1] = pop[t] * rate * (1 - pop[t])
def logistic_map(pop, rate):
    return pop * rate * (1 - pop)
    
def logistic_model(num_gens=50, rate_min=0.5, rate_max=4, num_rates=8, num_discard=0, initial_pop=0.5):
    """
    returns a dataframe with columns for each growth rate, row labels for each time step, and values computed by logistic map
    
    num_gens = number of iterations to run the model
    rate_min = the first growth rate for the model, between 0 and 4
    rate_max = the last growth rate for the model, between 0 and 4
    num_rates = how many growth rates between min and max to run the model on
    num_discard = number of generations to discard before keeping population values
    initial_pop = starting population when you run the model, between 0 and 1
    """
    pops = []
    rates = np.linspace(rate_min, rate_max, num_rates)
    
    # for each rate, run the logistic map repeatedly, starting at the initial_pop
    for rate in rates:
        pop = initial_pop
        
        # first run it num_discard times and ignore the results
        for _ in range(num_discard):
            pop = logistic_map(pop, rate)
        
        # now that those gens are discarded, run it num_gens times and keep the results
        for _ in range(num_gens):
            pops.append([rate, pop])
            pop = logistic_map(pop, rate)
    
    # return a dataframe with one column for each growth rate and one row for each timestep (aka generation)
    df = pd.DataFrame(data=pops, columns=['rate', 'pop'])
    df.index = pd.MultiIndex.from_arrays([num_rates * range(num_gens), df['rate'].values])
    return df.drop(labels='rate', axis=1).unstack()['pop']
    
def get_plot_points(pops):
    """
    convert a dataframe of values from the logistic model into a set of xy points that you can plot as a bifurcation diagram
    
    pops = population data output from the model
    """
    
    # create a new dataframe to contain our xy points
    points = pd.DataFrame(columns=['x', 'y'])
    
    # for each column in the logistic populations dataframe
    for rate in pops.columns:
        # append the growth rate as the x column and all the population values as the y column
        points = points.append(pd.DataFrame({'x':rate, 'y':pops[rate]}))
    
    # reset the index and drop the old index before returning the xy point data
    points = points.reset_index().drop(labels='index', axis=1)
    return points
    
def bifurcation_plot(pops, xmin=0, xmax=4, ymin=0, ymax=1, height=6, width=10, filename='image'):
    """
    plot the results of the logistic model as a bifurcation diagram
    
    pops = population data output from the model
    xmin = minimum value on the x axis
    xmax = maximum value on the x axis
    ymin = minimum value on the y axis
    ymax = maximum value on the y axis
    height = the height of the figure to plot, in inches
    width = the width of the figure to plot, in inches
    """
    # create a new matplotlib figure and axis and set its size
    fig, ax = plt.subplots()
    fig.set_size_inches(width, height)
    
    # plot the xy data
    points = get_plot_points(pops)
    bifurcation_scatter = ax.scatter(points['x'], points['y'], c='b', edgecolor='None', alpha=1, s=1)
    
    # set x and y limits, title, and x and y labels
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_title('Logistic Map Bifurcation Diagram', fontproperties=title_font)
    ax.set_xlabel('Growth Rate', fontproperties=label_font)
    ax.set_ylabel('Population', fontproperties=label_font)
    
    save_fig(plt, filename)
    plt.show()